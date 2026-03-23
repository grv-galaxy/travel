from flask import Blueprint, request, jsonify
from database.database import SessionLocal 
from database.models.logistics import FleetAsset 
from services.cloudinary_service import CloudinaryService
import json

afleet_bp = Blueprint('afleet', __name__)

# --- 1. ADD ASSET ---
@afleet_bp.route('/fleet/add-asset', methods=['POST'])
def add_asset():
    db = SessionLocal()
    try:
        if 'image' not in request.files:
            return jsonify({"success": False, "message": "No asset visual provided"}), 400
        
        image_file = request.files['image']
        name = request.form.get('name')
        asset_type = request.form.get('type')
        license_plate = request.form.get('license')
        status = request.form.get('status', 'Available')

        fuel_raw = request.form.get('fuel')
        try:
            fuel_val = int(fuel_raw) if (fuel_raw and fuel_raw != 'undefined') else 100
        except (ValueError, TypeError):
            fuel_val = 100

        image_url = CloudinaryService.upload_image(image_file, folder="fleet")
        if not image_url:
            return jsonify({"success": False, "message": "Cloudinary upload failed"}), 500

        new_asset = FleetAsset(
            name=name,
            type=asset_type,
            license_plate=license_plate,
            image_url=image_url,
            status=status,
            fuel_level=fuel_val,
            specifications=json.dumps({"transmission": "Automatic", "luxury_class": "Tier-1"})
        )

        db.add(new_asset)
        db.commit()

        return jsonify({
            "success": True, 
            "message": "Asset deployed",
            "asset": {
                "id": new_asset.id,
                "name": new_asset.name,
                "image": new_asset.image_url,
                "license": new_asset.license_plate,
                "status": new_asset.status,
                "fuel": new_asset.fuel_level,
                "type": new_asset.type
            }
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()

# --- 2. GET ALL ASSETS ---
@afleet_bp.route('/fleet/assets', methods=['GET'])
def get_all_assets():
    db = SessionLocal()
    try:
        assets = db.query(FleetAsset).order_by(FleetAsset.created_at.desc()).all()
        fleet_list = [{
            "id": a.id, "name": a.name, "type": a.type,
            "license": a.license_plate, "image": a.image_url,
            "status": a.status, "fuel": a.fuel_level
        } for a in assets]
        return jsonify({"success": True, "data": fleet_list})
    finally:
        db.close()

# --- 3. DELETE ASSET ---
@afleet_bp.route('/fleet/assets/<asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    db = SessionLocal()
    try:
        asset = db.query(FleetAsset).get(asset_id)
        if not asset:
            return jsonify({"success": False, "message": "Asset not found"}), 404
        
        db.delete(asset)
        db.commit()
        return jsonify({"success": True, "message": "Asset decommissioned from fleet"})
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()

# --- 4. MODIFY (UPDATE) ASSET ---
@afleet_bp.route('/fleet/assets/<asset_id>', methods=['PATCH'])
def update_asset(asset_id):
    db = SessionLocal()
    try:
        asset = db.query(FleetAsset).get(asset_id)
        if not asset:
            return jsonify({"success": False, "message": "Asset not found"}), 404
        
        data = request.json # We expect JSON for updates
        
        # Update fields if they exist in request
        if 'status' in data: asset.status = data['status']
        if 'fuel' in data: asset.fuel_level = int(data['fuel'])
        if 'name' in data: asset.name = data['name']
        
        db.commit()
        return jsonify({"success": True, "message": "Asset intelligence updated"})
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()