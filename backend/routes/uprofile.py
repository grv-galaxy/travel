from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.database import SessionLocal
from database.models.user import User
from sqlalchemy.exc import SQLAlchemyError

uprofile_bp = Blueprint('uprofile', __name__)

@uprofile_bp.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        return jsonify({"success": True}), 200

# 1. READ: Get Profile Information
@uprofile_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    current_user_email = get_jwt_identity()
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == current_user_email).first()
        if not user:
            return jsonify({"success": False, "message": "User not found"}), 404

        return jsonify({
            "success": True,
            "data": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "phone": user.phone,
                "tier": user.tier,
                "loyalty_points": user.loyalty_points,
                "profile_image": user.profile_image,
                "preferences": user.preferences,
                "created_at": user.created_at
            }
        }), 200
    finally:
        db.close()

# 2. UPDATE: Edit Profile Information
@uprofile_bp.route('/profile/update', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user_email = get_jwt_identity()
    data = request.get_json()
    db = SessionLocal()
    
    try:
        user = db.query(User).filter(User.email == current_user_email).first()
        if not user:
            return jsonify({"success": False, "message": "User not found"}), 404

        # Update basic fields if provided in request
        user.full_name = data.get('full_name', user.full_name)
        user.phone = data.get('phone', user.phone)
        user.profile_image = data.get('profile_image', user.profile_image)
        
        # Update preferences (merging JSON data)
        if 'preferences' in data:
            user.preferences = data['preferences']

        db.commit()
        return jsonify({"success": True, "message": "Luxury profile updated successfully"}), 200
    
    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()

# 3. DELETE: Remove User Account
# @uprofile_bp.route('/profile/delete', methods=['DELETE'])
# @jwt_required()
# def delete_profile():
#     current_user_email = get_jwt_identity()
#     db = SessionLocal()
    
#     try:
#         user = db.query(User).filter(User.email == current_user_email).first()
#         if not user:
#             return jsonify({"success": False, "message": "User not found"}), 404

#         db.delete(user)
#         db.commit()
#         return jsonify({"success": True, "message": "Account deactivated and removed"}), 200
    
#     except SQLAlchemyError as e:
#         db.rollback()
#         return jsonify({"success": False, "message": str(e)}), 500
#     finally:
#         db.close()