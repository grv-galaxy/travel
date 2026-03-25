# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token
# from database.database import SessionLocal
# from database.models.admin import Admin
# from database.models.user import User
# from flask_bcrypt import Bcrypt
# import requests
# import logging
# import os
# import jwt
# import uuid

# def generate_uuid():
#     return str(uuid.uuid4())

# # Configure logging for production auditing
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# jwt_secret = os.getenv("JWT_SECRET")

# auth_bp = Blueprint('auth', __name__)
# bcrypt = Bcrypt()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @auth_bp.route('/admin-login', methods=['POST'])
# def admin_login():
#     """
#     Dedicated secure endpoint for Admin Password Login.
#     """
#     data = request.get_json()
    
#     if not data or not data.get('email') or not data.get('password'):
#         return jsonify({"success": False, "message": "Email and password required"}), 400

#     email = data.get('email').strip().lower()
#     password = data.get('password')

#     db = SessionLocal()
#     try:
#         # Search specifically in Admin table
#         admin = db.query(Admin).filter(Admin.email == email, Admin.is_active == True).first()

#         # Secure password check
#         # Note: Ensure your DB column name is 'password_hash' as per schema
#         if admin and bcrypt.check_password_hash(admin.password_hash, password):
            
#             # Create token with necessary claims
#             access_token = create_access_token(
#                 identity=admin.email, 
#                 additional_claims={
#                     "is_admin": True,
#                     "role": admin.role,
#                     "username": admin.full_name
#                 }
#             )

#             logger.info(f"Successful Admin login: {email}")
#             return jsonify({
#                 "success": True,
#                 "token": access_token,
#                 "user": {
#                     #"id": admin.id,
#                     "email": admin.email,
#                     "username": admin.full_name,
#                     "role": admin.role
#                 }
#             }), 200
        
#         # Security Best Practice: Use generic error message to prevent account enumeration
#         return jsonify({
#             "success": False, 
#             "message": "Invalid credentials or unauthorized access"
#         }), 401

#     except Exception as e:
#         logger.error(f"Admin Login Error: {str(e)}")
#         return jsonify({"success": False, "message": "Internal server error"}), 500
#     finally:
#         db.close()

# @auth_bp.route('/google', methods=['POST'])
# def google_login():
#     """
#     Unified Google OAuth login. Checks Admin table first, then User table.
#     """
#     data = request.get_json()
#     google_access_token = data.get('token')

#     if not google_access_token:
#         return jsonify({"success": False, "message": "OAuth token missing"}), 400

#     # 1. Verify with Google API
#     try:
#         google_response = requests.get(
#             'https://www.googleapis.com/oauth2/v3/userinfo',
#             headers={'Authorization': f'Bearer {google_access_token}'},
#             timeout=5 # Set timeout for production stability
#         )
#     except requests.exceptions.RequestException:
#         return jsonify({"success": False, "message": "Google Service Unreachable"}), 503

#     if google_response.status_code != 200:
#         return jsonify({"success": False, "message": "Invalid OAuth credentials"}), 401

#     user_info = google_response.json()
#     email = user_info.get('email').lower()
#     name = user_info.get('name')

#     db = SessionLocal()
#     try:
#         # 2. CHECK ADMINS TABLE FIRST (Waterfall Logic)
#         admin = db.query(Admin).filter(Admin.email == email, Admin.is_active == True).first()
        
#         if admin:
#             token = create_access_token(
#                 identity=admin.email,
#                 additional_claims={
#                     "is_admin": True,
#                     "role": admin.role,
#                     "username": admin.full_name
#                 }
#             )
#             return jsonify({
#                 "success": True,
#                 "token": token,
#                 "is_admin": True,
#                 "user": {
#                     "email": admin.email,
#                     "username": admin.full_name,
#                     "role": admin.role
#                 }
#             }), 200

#         # 3. CHECK OR CREATE USER
#         user = db.query(User).filter(User.email == email).first()

#         if not user:
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

#         access_token = create_access_token(
#             identity=user.email,
#             additional_claims={
#                 "is_admin": False,
#                 "role": "User",
#                 "username": user.full_name,
#                 "tier": user.tier
#             }
#         )

#         return jsonify({
#             "success": True,
#             "token": access_token,
#             "is_admin": False,
#             "user": {
#                 "id": str(user.id),
#                 "email": user.email,
#                 "username": user.full_name,
#                 "role": "User",
#                 "tier": user.tier
#             }
#         }), 200

#     except Exception as e:
#         logger.error(f"Google Auth Error: {str(e)}")
#         db.rollback()
#         return jsonify({"success": False, "message": "Database transaction failed"}), 500
#     finally:
#         db.close()


# # New route in auth.py
# @auth_bp.route('/phone', methods=['POST'])
# def phone_login():
#     """
#     Verifies Firebase ID token from phone auth, then issues your app JWT.
#     """
#     data = request.get_json()
#     baas_token = data.get('baas_token')
#     phone_number = data.get('phone_number') or data.get('phone')  # Accept either key for flexibility

#     if not baas_token or not phone_number:
#         return jsonify({"success": False, "message": "Missing credentials"}), 400

#     try:
#         # Firebase Admin verifies the token server-side
#         decoded = jwt.decode(
#             baas_token, 
#             jwt_secret, 
#             algorithms=["HS256"],
#             options={"verify_aud": False}
#         )
#         token_phone = decoded.get('sub')
#         if token_phone != phone_number:
#             logger.warning(f"Phone number mismatch: token {token_phone} vs request {phone_number}")
#             return jsonify({"success": False, "message": "Token phone number mismatch"}), 401

#     except jwt.ExpiredSignatureError:
#         return jsonify({"success": False, "message": "OTP session expired"}), 401
#     except jwt.InvalidTokenError as e:
#         logger.error(f"JWT decode error: {str(e)}")
#         return jsonify({"success": False, "message": "Invalid BaaS token"}), 401
#     except Exception as e:
#         logger.error(f"Unexpected token error: {str(e)}")
#         return jsonify({"success": False, "message": "Token verification failed"}), 500

#     db = SessionLocal()
#     try:
#         # Find or create user by phone
#         user = db.query(User).filter(User.phone == phone_number).first()

#         if not user:
#             placeholder_email = f"pending_{generate_uuid()}@pending.com"
#             user = User(
#                 phone=phone_number,
#                 full_name="Pending",      # can be updated later in profile
#                 email=placeholder_email,
#                 tier="Silver",
#                 loyalty_points=0,
#                 preferences={"mood": "Default"}
#             )
#             db.add(user)
#             db.commit()
#             db.refresh(user)

#         access_token = create_access_token(
#             identity=user.phone,
#             additional_claims={
#                 "is_admin": False,
#                 "role": "User",
#                 "username": user.full_name,
#                 "tier": user.tier
#             }
#         )

#         return jsonify({
#             "success": True,
#             "token": access_token,
#             "user": {
#                 "id": str(user.id),
#                 "phone": user.phone,
#                 "username": user.full_name,
#                 "role": "User",
#                 "tier": user.tier
#             }
#         }), 200

#     except Exception as e:
#         logger.error(f"Phone Auth DB Error: {str(e)}")
#         db.rollback()
#         return jsonify({"success": False, "message": "Database error"}), 500
#     finally:
#         db.close()
































from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from database.database import SessionLocal
from database.models.admin import Admin
from database.models.user import User
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
import requests
import logging
import os
import jwt
import uuid
import re

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ── Constants ─────────────────────────────────────────────────────────────────
auth_bp  = Blueprint('auth', __name__)
bcrypt   = Bcrypt()

# Fail loudly at startup if secret is missing
jwt_secret = os.getenv("JWT_SECRET")
if not jwt_secret:
    raise RuntimeError("JWT_SECRET environment variable is not set. Server cannot start.")

# ── Helpers ───────────────────────────────────────────────────────────────────
def generate_uuid() -> str:
    return str(uuid.uuid4())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def normalize_phone(phone: str) -> str | None:
    """Strip spaces/dashes, ensure E.164 format e.g. +911234567890"""
    if not phone:
        return None
    cleaned = re.sub(r'[\s\-\(\)]', '', phone.strip())
    if not re.match(r'^\+?[1-9]\d{7,14}$', cleaned):
        return None
    return cleaned

def normalize_email(email: str) -> str | None:
    if not email:
        return None
    cleaned = email.strip().lower()
    if not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', cleaned):
        return None
    return cleaned

def build_user_response(user: User) -> dict:
    """Consistent user payload across all auth methods."""
    return {
        "id":       str(user.id),
        "email":    user.email,
        "phone":    user.phone,
        "username": user.full_name,
        "role":     "User",
        "tier":     user.tier,
        "is_phone_verified": getattr(user, 'is_phone_verified', False),
        "is_email_verified": getattr(user, 'is_email_verified', False),
    }

def create_user_token(user: User) -> str:
    return create_access_token(
        identity=user.email or user.phone,
        additional_claims={
            "is_admin": False,
            "role":     "User",
            "username": user.full_name,
            "tier":     user.tier,
            "user_id":  str(user.id),
        }
    )

# ── Admin Login ───────────────────────────────────────────────────────────────
@auth_bp.route('/admin-login', methods=['POST'])
def admin_login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"success": False, "message": "Invalid JSON body"}), 400

    email    = normalize_email(data.get('email', ''))
    password = data.get('password', '').strip()

    if not email or not password:
        return jsonify({"success": False, "message": "Email and password are required"}), 400

    db = SessionLocal()
    try:
        admin = db.query(Admin).filter(
            Admin.email == email,
            Admin.is_active == True
        ).first()

        if not admin or not bcrypt.check_password_hash(admin.password_hash, password):
            logger.warning(f"Failed admin login attempt: {email}")
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        token = create_access_token(
            identity=admin.email,
            additional_claims={
                "is_admin": True,
                "role":     admin.role,
                "username": admin.full_name,
            }
        )
        logger.info(f"Admin login success: {email}")
        return jsonify({
            "success": True,
            "token": token,
            "user": {
                "email":    admin.email,
                "username": admin.full_name,
                "role":     admin.role,
            }
        }), 200

    except Exception as e:
        logger.error(f"Admin login error: {e}")
        return jsonify({"success": False, "message": "Internal server error"}), 500
    finally:
        db.close()


# ── Google OAuth Login ────────────────────────────────────────────────────────
@auth_bp.route('/google', methods=['POST'])
def google_login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"success": False, "message": "Invalid JSON body"}), 400

    google_token = data.get('token', '').strip()
    if not google_token:
        return jsonify({"success": False, "message": "OAuth token is required"}), 400

    # Verify with Google
    try:
        g_resp = requests.get(
            'https://www.googleapis.com/oauth2/v3/userinfo',
            headers={'Authorization': f'Bearer {google_token}'},
            timeout=5
        )
    except requests.exceptions.Timeout:
        return jsonify({"success": False, "message": "Google service timeout"}), 504
    except requests.exceptions.RequestException:
        return jsonify({"success": False, "message": "Google service unreachable"}), 503

    if g_resp.status_code != 200:
        return jsonify({"success": False, "message": "Invalid Google token"}), 401

    user_info = g_resp.json()
    email = normalize_email(user_info.get('email', ''))
    name  = user_info.get('name', 'User')

    if not email:
        return jsonify({"success": False, "message": "Could not retrieve email from Google"}), 400

    db = SessionLocal()
    try:
        # Check admin first
        admin = db.query(Admin).filter(
            Admin.email == email,
            Admin.is_active == True
        ).first()

        if admin:
            token = create_access_token(
                identity=admin.email,
                additional_claims={
                    "is_admin": True,
                    "role":     admin.role,
                    "username": admin.full_name,
                }
            )
            return jsonify({
                "success":  True,
                "token":    token,
                "is_admin": True,
                "user": {
                    "email":    admin.email,
                    "username": admin.full_name,
                    "role":     admin.role,
                }
            }), 200

        # Find or create regular user
        user = db.query(User).filter(User.email == email).first()

        if user:
            # Existing user — update provider if needed
            if getattr(user, 'auth_provider', None) == 'phone':
                # Phone user is now linking Google — update email verified
                user.is_email_verified = True
                db.commit()
        else:
            # New user via Google
            user = User(
                full_name=name,
                email=email,
                tier="Silver",
                loyalty_points=0,
                preferences={"mood": "Default"},
                auth_provider="google",
                is_email_verified=True,
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        token = create_user_token(user)
        return jsonify({
            "success":  True,
            "token":    token,
            "is_admin": False,
            "user":     build_user_response(user),
        }), 200

    except IntegrityError:
        db.rollback()
        return jsonify({"success": False, "message": "Account conflict. Try logging in differently."}), 409
    except Exception as e:
        db.rollback()
        logger.error(f"Google auth error: {e}")
        return jsonify({"success": False, "message": "Authentication failed"}), 500
    finally:
        db.close()


# ── Phone OTP Login ───────────────────────────────────────────────────────────
@auth_bp.route('/phone', methods=['POST'])
def phone_login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"success": False, "message": "Invalid JSON body"}), 400

    baas_token   = data.get('baas_token', '').strip()
    raw_phone    = data.get('phone_number') or data.get('phone', '')
    phone_number = normalize_phone(raw_phone)

    # ── Input validation ──────────────────────────────────────────────────────
    if not baas_token:
        return jsonify({"success": False, "message": "BaaS token is required"}), 400
    if not phone_number:
        return jsonify({
            "success": False,
            "message": "Invalid phone number format. Use E.164 e.g. +911234567890"
        }), 400

    # ── Verify BaaS JWT ───────────────────────────────────────────────────────
    try:
        decoded     = jwt.decode(
            baas_token,
            jwt_secret,
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        token_phone = normalize_phone(decoded.get('sub', ''))

        if not token_phone:
            return jsonify({"success": False, "message": "Token missing phone claim"}), 401

        if token_phone != phone_number:
            logger.warning(f"Phone mismatch — token: {token_phone}, request: {phone_number}")
            return jsonify({"success": False, "message": "Phone number does not match token"}), 401

    except jwt.ExpiredSignatureError:
        return jsonify({"success": False, "message": "OTP session expired. Please resend OTP."}), 401
    except jwt.InvalidSignatureError:
        return jsonify({"success": False, "message": "Token signature invalid"}), 401
    except jwt.DecodeError:
        return jsonify({"success": False, "message": "Malformed token"}), 401
    except jwt.InvalidTokenError as e:
        logger.error(f"JWT error: {e}")
        return jsonify({"success": False, "message": "Invalid token"}), 401
    except Exception as e:
        logger.error(f"Unexpected token error: {e}")
        return jsonify({"success": False, "message": "Token verification failed"}), 500

    # ── Database logic ────────────────────────────────────────────────────────
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.phone == phone_number).first()

        if user:
            # ── Case 1: Phone user exists — just login ────────────────────────
            logger.info(f"Phone login success: {phone_number}")

        else:
            # ── Case 2: Check if email user already saved this phone ──────────
            # (Google/email user who added phone in profile)
            user_by_phone_in_profile = db.query(User).filter(
                User.phone == phone_number
            ).first()

            if user_by_phone_in_profile:
                # Phone already linked to an email account — just log them in
                user = user_by_phone_in_profile
                user.is_phone_verified = True
                db.commit()
                logger.info(f"Existing email user logged in via phone: {phone_number}")

            else:
                # ── Case 3: Brand new user via phone ─────────────────────────
                user = User(
                    phone=phone_number,
                    full_name="User",
                    email=None,           # no email yet — requires nullable email column
                    tier="Silver",
                    loyalty_points=0,
                    preferences={"mood": "Default"},
                    auth_provider="phone",
                    is_phone_verified=True,
                )
                db.add(user)
                try:
                    db.commit()
                    db.refresh(user)
                    logger.info(f"New phone user created: {phone_number}")
                except IntegrityError:
                    db.rollback()
                    # Race condition — another request created same phone user
                    user = db.query(User).filter(User.phone == phone_number).first()
                    if not user:
                        return jsonify({"success": False, "message": "Account creation failed"}), 500

        token = create_user_token(user)
        return jsonify({
            "success": True,
            "token":   token,
            "user":    build_user_response(user),
        }), 200

    except IntegrityError:
        db.rollback()
        logger.warning(f"Duplicate phone registration attempt: {phone_number}")
        return jsonify({
            "success": False,
            "message": "An account with this phone number already exists. Please log in."
        }), 409
    except Exception as e:
        db.rollback()
        logger.error(f"Phone auth DB error: {e}")
        return jsonify({"success": False, "message": "Database error during authentication"}), 500
    finally:
        db.close()