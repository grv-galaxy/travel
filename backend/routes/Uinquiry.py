from flask import Blueprint, request, jsonify
from database.database import SessionLocal
from database.models import Inquiry
from sqlalchemy.exc import SQLAlchemyError

inquiries_bp = Blueprint('inquiries_bp', __name__)

@inquiries_bp.route('/inquiries/submit', methods=['POST'])
def submit_inquiry():
    db = SessionLocal()
    try:
        # 1. Parse JSON data from Vue
        data = request.get_json()
        
        if not data:
            return jsonify({"success": False, "message": "No data provided"}), 400

        # 2. Create the record (Matching your Model exactly)
        new_inquiry = Inquiry(
            full_name=data.get('full_name'),
            email=data.get('email'),
            phone=data.get('phone'),
            destination_type=data.get('destination_type'),
            travelers=int(data.get('travelers') or 1),
            message=data.get('message'),
            status='New' # Initial status for the Admin Dashboard
        )

        # 3. Save to database
        db.add(new_inquiry)
        db.commit()
        db.refresh(new_inquiry)

        return jsonify({
            "success": True, 
            "message": "Strategic inquiry logged in secure ledger.",
            "inquiry_id": new_inquiry.id
        }), 201

    except SQLAlchemyError as e:
        db.rollback()
        return jsonify({"success": False, "message": f"Database Error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"success": False, "message": f"System Error: {str(e)}"}), 500
    finally:
        db.close()

# Route for Admin Dashboard to fetch the list
@inquiries_bp.route('/inquiries/list', methods=['GET'])
def get_all_inquiries():
    db = SessionLocal()
    try:
        # Fetching latest inquiries first
        inquiries = db.query(Inquiry).order_by(Inquiry.created_at.desc()).all()
        return jsonify({
            "success": True,
            "data": [i.to_dict() for i in inquiries]
        }), 200
    finally:
        db.close()

# Add this to your inquiries.py
@inquiries_bp.route('/inquiries/<string:inquiry_id>/status', methods=['PUT'])
def update_inquiry_status(inquiry_id):
    db = SessionLocal()
    try:
        # Use force=True to handle cases where Content-Type header might be missing
        data = request.get_json(force=True) 
        
        if not data or 'status' not in data:
            return jsonify({"success": False, "message": "Missing 'status' in request body"}), 400

        new_status = data.get('status')
        
        # Valid statuses based on your model/logic
        allowed = ['New', 'Contacted', 'Converted', 'Ignored', 'In-Progress']
        if new_status not in allowed:
            return jsonify({"success": False, "message": f"Invalid status: {new_status}"}), 400

        target = db.query(Inquiry).filter(Inquiry.id == inquiry_id).first()
        if not target:
            return jsonify({"success": False, "message": "Inquiry not found"}), 404

        target.status = new_status
        db.commit()
        
        return jsonify({"success": True, "message": "Status updated successfully"}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()