# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token
# from database.database import SessionLocal  # Your existing DB setup
# from database.models.admin import Admin    # Your existing Admin model
# from flask_bcrypt import Bcrypt
# import requests # For making HTTP requests if needed
# from database.models.user import User  # Import User model if needed

# auth_bp = Blueprint('auth', __name__)
# bcrypt = Bcrypt()

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     # 1. Catch the JSON data sent from Vue (axios.post)
#     data = request.get_json()
    
#     if not data:
#         return jsonify({"msg": "Missing JSON in request"}), 400

#     email = data.get('email')
#     password = data.get('password')

#     # 2. Basic Validation
#     if not email or not password:
#         return jsonify({"msg": "Email and password are required"}), 400

#     # 3. Database Query using your SessionLocal
#     db = SessionLocal()
#     try:
#         # Querying your Admin table for the specific email
#         admin = db.query(Admin).filter(Admin.email == email).first()

#         # 4. Password Verification
#         # Using bcrypt to check if the provided password matches the hashed one in DB
#         if admin and bcrypt.check_password_hash(admin.password, password):
            
#             # 5. Create the JWT Token
#             # We store the email as identity and add role/name for the frontend
#             access_token = create_access_token(
#                 identity=admin.email, 
#                 additional_claims={
#                     "role": admin.role,
#                     "username": admin.username
#                 }
#             )

#             return jsonify({
#                 "success": True,
#                 "token": access_token,
#                 "admin": {
#                     "email": admin.email,
#                     "username": admin.username,
#                     "role": admin.role
#                 }
#             }), 200
        
#         # If admin not found or password wrong
#         return jsonify({
#             "success": False, 
#             "message": "Security Alert: Unauthorized Credentials"
#         }), 401

#     except Exception as e:
#         return jsonify({"success": False, "message": str(e)}), 500
#     finally:
#         db.close() # Always close the session to prevent memory leaks



# @auth_bp.route('/google', methods=['POST'])
# def google_login():
#     data = request.get_json()
#     google_access_token = data.get('token')

#     if not google_access_token:
#         return jsonify({"success": False, "message": "Google token is missing"}), 400

#     # 1. Verify the token with Google
#     google_response = requests.get(
#         'https://www.googleapis.com/oauth2/v3/userinfo',
#         headers={'Authorization': f'Bearer {google_access_token}'}
#     )

#     if google_response.status_code != 200:
#         return jsonify({"success": False, "message": "Invalid Google Token"}), 401

#     user_info = google_response.json()
#     email = user_info.get('email')
#     name = user_info.get('name')

#     db = SessionLocal()
#     try:
#         # Check if user exists
#         user = db.query(User).filter(User.email == email).first()

#         if not user:
#             # If user doesn't exist, create a new record
#             user = User(
#                 full_name=name,
#                 email=email,
#                 tier="Silver",
#                 loyalty_points=0,
#                 preferences={"mood": "Default"}
#             )
#             db.add(user)
#             db.commit()
#             db.refresh(user)

#         # 2. Fix the JWT Token attributes
#         # Since the User model doesn't have 'role', we pass "User" manually.
#         # Since it doesn't have 'username', we use 'full_name'.
#         access_token = create_access_token(
#             identity=user.email,
#             additional_claims={
#                 "role": "User",             # Fix: Use string "User" instead of user.role
#                 "username": user.full_name, # Fix: Use full_name instead of username
#                 "tier": user.tier           # Added: useful for luxury tier checks
#             }
#         )

#         # 3. Fix the JSON Response attributes
#         return jsonify({
#             "success": True,
#             "token": access_token,
#             "user": {
#                 "email": user.email,
#                 "username": user.full_name, # Fix: Use full_name
#                 "role": "User",             # Fix: Hardcode "User"
#                 "tier": user.tier           # Fix: Added tier
#             }
#         }), 200

#     except Exception as e:
#         return jsonify({"success": False, "message": str(e)}), 500
#     finally:
#         db.close()
















from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from database.database import SessionLocal
from database.models.admin import Admin
from database.models.user import User
from flask_bcrypt import Bcrypt
import requests
import logging
import os
import jwt 


# Configure logging for production auditing
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
jwt_secret = os.getenv("JWT_SECRET")

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@auth_bp.route('/admin-login', methods=['POST'])
def admin_login():
    """
    Dedicated secure endpoint for Admin Password Login.
    """
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"success": False, "message": "Email and password required"}), 400

    email = data.get('email').strip().lower()
    password = data.get('password')

    db = SessionLocal()
    try:
        # Search specifically in Admin table
        admin = db.query(Admin).filter(Admin.email == email, Admin.is_active == True).first()

        # Secure password check
        # Note: Ensure your DB column name is 'password_hash' as per schema
        if admin and bcrypt.check_password_hash(admin.password_hash, password):
            
            # Create token with necessary claims
            access_token = create_access_token(
                identity=admin.email, 
                additional_claims={
                    "is_admin": True,
                    "role": admin.role,
                    "username": admin.full_name
                }
            )

            logger.info(f"Successful Admin login: {email}")
            return jsonify({
                "success": True,
                "token": access_token,
                "user": {
                    #"id": admin.id,
                    "email": admin.email,
                    "username": admin.full_name,
                    "role": admin.role
                }
            }), 200
        
        # Security Best Practice: Use generic error message to prevent account enumeration
        return jsonify({
            "success": False, 
            "message": "Invalid credentials or unauthorized access"
        }), 401

    except Exception as e:
        logger.error(f"Admin Login Error: {str(e)}")
        return jsonify({"success": False, "message": "Internal server error"}), 500
    finally:
        db.close()

@auth_bp.route('/google', methods=['POST'])
def google_login():
    """
    Unified Google OAuth login. Checks Admin table first, then User table.
    """
    data = request.get_json()
    google_access_token = data.get('token')

    if not google_access_token:
        return jsonify({"success": False, "message": "OAuth token missing"}), 400

    # 1. Verify with Google API
    try:
        google_response = requests.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            headers={'Authorization': f'Bearer {google_access_token}'},
            timeout=5 # Set timeout for production stability
        )
    except requests.exceptions.RequestException:
        return jsonify({"success": False, "message": "Google Service Unreachable"}), 503

    if google_response.status_code != 200:
        return jsonify({"success": False, "message": "Invalid OAuth credentials"}), 401

    user_info = google_response.json()
    email = user_info.get('email').lower()
    name = user_info.get('name')

    db = SessionLocal()
    try:
        # 2. CHECK ADMINS TABLE FIRST (Waterfall Logic)
        admin = db.query(Admin).filter(Admin.email == email, Admin.is_active == True).first()
        
        if admin:
            token = create_access_token(
                identity=admin.email,
                additional_claims={
                    "is_admin": True,
                    "role": admin.role,
                    "username": admin.full_name
                }
            )
            return jsonify({
                "success": True,
                "token": token,
                "is_admin": True,
                "user": {
                    "email": admin.email,
                    "username": admin.full_name,
                    "role": admin.role
                }
            }), 200

        # 3. CHECK OR CREATE USER
        user = db.query(User).filter(User.email == email).first()

        if not user:
            user = User(
                full_name=name,
                email=email,
                tier="Silver",
                loyalty_points=0,
                preferences={"mood": "Default"}
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        access_token = create_access_token(
            identity=user.email,
            additional_claims={
                "is_admin": False,
                "role": "User",
                "username": user.full_name,
                "tier": user.tier
            }
        )

        return jsonify({
            "success": True,
            "token": access_token,
            "is_admin": False,
            "user": {
                "id": str(user.id),
                "email": user.email,
                "username": user.full_name,
                "role": "User",
                "tier": user.tier
            }
        }), 200

    except Exception as e:
        logger.error(f"Google Auth Error: {str(e)}")
        db.rollback()
        return jsonify({"success": False, "message": "Database transaction failed"}), 500
    finally:
        db.close()


# New route in auth.py
@auth_bp.route('/phone', methods=['POST'])
def phone_login():
    """
    Verifies Firebase ID token from phone auth, then issues your app JWT.
    """
    data = request.get_json()
    baas_token = data.get('baas_token')
    phone_number = data.get('phone_number')

    if not baas_token or not phone_number:
        return jsonify({"success": False, "message": "Missing credentials"}), 400

    try:
        # Firebase Admin verifies the token server-side
        decoded = jwt.decode(baas_token, jwt_secret, algorithms=["HS256"])
        if decoded.get('identifier') != phone_number:
            return jsonify({"success": False, "message": "Token identifier mismatch"}), 401

    except jwt.ExpiredSignatureError:
        return jsonify({"success": False, "message": "OTP session expired"}), 401
    except Exception as e:
        return jsonify({"success": False, "message": "Invalid BaaS token"})

    db = SessionLocal()
    try:
        # Find or create user by phone
        user = db.query(User).filter(User.phone == phone_number).first()

        if not user:
            placeholder_email = f"pending_{generate_uuid()}@pending.com"
            user = User(
                phone=phone_number,
                full_name="Pending",      # can be updated later in profile
                email=placeholder_email,
                tier="Silver",
                loyalty_points=0,
                preferences={"mood": "Default"}
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        access_token = create_access_token(
            identity=user.phone,
            additional_claims={
                "is_admin": False,
                "role": "User",
                "username": user.full_name,
                "tier": user.tier
            }
        )

        return jsonify({
            "success": True,
            "token": access_token,
            "user": {
                "id": str(user.id),
                "phone": user.phone,
                "username": user.full_name,
                "role": "User",
                "tier": user.tier
            }
        }), 200

    except Exception as e:
        logger.error(f"Phone Auth DB Error: {str(e)}")
        db.rollback()
        return jsonify({"success": False, "message": "Database error"}), 500
    finally:
        db.close()