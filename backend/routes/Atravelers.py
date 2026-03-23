from flask import Blueprint, request, jsonify # Changed Flask to Blueprint
from flask_cors import CORS
from database.database import SessionLocal
from database.models.user import User
from sqlalchemy import or_, func

# 1. Define the Blueprint instead of 'app'
travelers_bp = Blueprint('travelers', __name__)

# Helper to format currency and dates for the frontend
def format_user(user):
    return {
        "id": user.id,
        "name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "passport": user.passport_id or "N/A",
        "tier": user.tier,
        "spend": f"{user.total_spend:,.2f}", 
        "lastSeen": user.last_seen.strftime("%b %d, %Y") if user.last_seen else "Never",
        "status": user.status,
        "avatar": user.profile_image or f"https://ui-avatars.com/api/?name={user.full_name}&background=f5e6c8&color=854f1d",
        "loyalty_points": user.loyalty_points
    }

# 2. Use @travelers_bp.route instead of @app.route
# Note: Since your url_prefix is '/api/admin', this route becomes '/api/admin/travelers'
@travelers_bp.route('/travelers', methods=['GET'])
def get_all_travelers():
    db = SessionLocal()
    try:
        search = request.args.get('search', '').strip()
        query = db.query(User)
        
        if search:
            query = query.filter(
                or_(
                    User.full_name.ilike(f'%{search}%'),
                    User.email.ilike(f'%{search}%'),
                    User.passport_id.ilike(f'%{search}%'),
                    User.tier.ilike(f'%{search}%')
                )
            )

        travelers = query.order_by(User.total_spend.desc()).all()

        total_vips = db.query(func.count(User.id)).scalar()
        in_transit = db.query(func.count(User.id)).filter(User.status == 'Transit').scalar()
        elite_tier = db.query(func.count(User.id)).filter(User.tier.in_(['Gold Maharaja', 'Platinum Imperial'])).scalar()

        return jsonify({
            "success": True,
            "data": [format_user(u) for u in travelers],
            "stats": {
                "total": total_vips,
                "inTransit": in_transit,
                "eliteCount": elite_tier
            }
        })
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()

@travelers_bp.route('/travelers/<uuid>', methods=['DELETE'])
def delete_traveler(uuid):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == uuid).first()
        if not user:
            return jsonify({"success": False, "message": "User not found"}), 404
        
        db.delete(user)
        db.commit()
        return jsonify({"success": True, "message": "Profile removed from concierge"})
    except Exception as e:
        db.rollback() # Fixed: use db.rollback() directly for SessionLocal
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()