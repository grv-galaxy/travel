import uuid
from flask import Blueprint, request, jsonify
from database.database import SessionLocal
from database.models import Document
from services.cloudinary_service import CloudinaryService 
from datetime import datetime

udocument_bp = Blueprint('udocument_bp', __name__)

# --- 1. FETCH DOCUMENTS ---
@udocument_bp.route('/documents', methods=['GET'])
def get_user_documents():
    db = SessionLocal()
    # Pull the ID from the custom header we send from Vue
    user_id = request.headers.get('X-User-Id')
    
    if not user_id:
        return jsonify({"success": False, "message": "User ID missing from headers"}), 400

    try:
        # Fetching documents linked to this specific UUID
        docs = db.query(Document).filter(Document.user_id == user_id).order_by(Document.uploaded_at.desc()).all()
        return jsonify([doc.to_dict() for doc in docs]), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Database Error: {str(e)}"}), 500
    finally:
        db.close()

# --- 2. UPLOAD DOCUMENT ---
@udocument_bp.route('/documents/upload', methods=['POST'])
def upload_credential():
    db = SessionLocal()
    user_id = request.headers.get('X-User-Id')
    
    if not user_id:
        return jsonify({"success": False, "message": "User context missing"}), 400

    try:
        if 'file' not in request.files:
            return jsonify({"success": False, "message": "No document file provided."}), 400
            
        file = request.files['file']
        doc_type = request.form.get('doc_type', 'Passport')
        doc_name = request.form.get('doc_name', file.filename)
        expiry_date_str = request.form.get('expiry_date')

        # 1. Upload to Cloudinary using ID for the folder path
        upload_result = CloudinaryService.upload_document(file, folder=f"user_vault/{user_id}")

        if not upload_result:
            return jsonify({"success": False, "message": "Cloudinary synchronization failed."}), 500

        # 2. Parse Date
        expiry_date = None
        if expiry_date_str:
            try:
                expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
            except ValueError:
                pass

        # 3. Create Record using the user_id from the header
        new_doc = Document(
            user_id=user_id,
            doc_name=doc_name,
            doc_type=doc_type,
            file_url=upload_result['secure_url'],
            public_id=upload_result['public_id'],
            expiry_date=expiry_date,
            status='Verified'
        )

        db.add(new_doc)
        db.commit()
        db.refresh(new_doc)
        
        return jsonify({
            "success": True, 
            "message": "Credential secured in vault.",
            "document": new_doc.to_dict()
        }), 201

    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": f"System Error: {str(e)}"}), 500
    finally:
        db.close()

# --- 3. DELETE DOCUMENT ---
@udocument_bp.route('/documents/<string:id>', methods=['DELETE'])
def delete_credential(id):
    db = SessionLocal()
    # We check user_id on delete too for basic security
    user_id = request.headers.get('X-User-Id')
    
    try:
        target = db.query(Document).filter(Document.id == id, Document.user_id == user_id).first()
        
        if not target:
            return jsonify({"success": False, "message": "Document not found."}), 404

        CloudinaryService.delete_resource(target.public_id)
        db.delete(target)
        db.commit()
        
        return jsonify({"success": True, "message": "Credential purged."}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()