from flask import Blueprint, request, jsonify
import uuid
from sqlalchemy.exc import SQLAlchemyError
from flask_bcrypt import Bcrypt  # Switched to Bcrypt to match auth_bp

# MATCHING YOUR SESSION PATTERN
from database.database import SessionLocal
from database.models import Admin

security_bp = Blueprint('security', __name__)
bcrypt = Bcrypt() # Initialize Bcrypt

# 1. GET ALL ADMINS
@security_bp.route('/admins', methods=['GET'])
def get_all_admins():
    """Fetch the list of all administrative personnel."""
    db = SessionLocal()
    try:
        admins = db.query(Admin).order_by(Admin.created_at.desc()).all()
        admin_list = []
        for a in admins:
            admin_list.append({
                "id": a.id,
                "full_name": a.full_name,
                "email": a.email,
                "role": a.role,
                "last_login": a.last_login.strftime('%Y-%m-%d %H:%M') if a.last_login else 'Never'
            })
        return jsonify(admin_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

# 2. PROVISION NEW ADMIN
@security_bp.route('/admins/provision', methods=['POST'])
def provision_admin():
    """Create a new admin account with specific role-based access."""
    db = SessionLocal()
    try:
        data = request.get_json()
        
        # Validation
        required = ['full_name', 'email', 'password', 'role']
        if not all(k in data for k in required):
            return jsonify({"message": "Missing critical fields"}), 400

        # Check if email exists
        if db.query(Admin).filter(Admin.email == data['email']).first():
            return jsonify({"message": "Administrator already exists"}), 409

        # Create New Admin Instance
        new_admin = Admin(
            id=str(uuid.uuid4()),
            full_name=data['full_name'],
            email=data['email'].strip().lower(),
            # ✅ MATCHING AUTH_BP: Use bcrypt to generate the hash
            password_hash=bcrypt.generate_password_hash(data['password']).decode('utf-8'),
            role=data['role'],
            added_by_id=None, 
            is_active=True
        )
        
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)

        return jsonify({
            "id": new_admin.id,
            "full_name": new_admin.full_name,
            "role": new_admin.role,
            "message": "Access successfully provisioned"
        }), 201

    except Exception as e:
        db.rollback()
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
    finally:
        db.close()

# 3. REVOKE ACCESS (DELETE)
@security_bp.route('/admins/<string:admin_id>', methods=['DELETE'])
def revoke_admin(admin_id):
    """Permanently revoke administrative access."""
    db = SessionLocal()
    try:
        target_admin = db.query(Admin).filter(Admin.id == admin_id).first()

        if not target_admin:
            return jsonify({"message": "Administrator not found"}), 404

        db.delete(target_admin)
        db.commit()
        return jsonify({"message": "Access revoked successfully"}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()