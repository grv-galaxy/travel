import uuid
import json
from flask import Blueprint, request, jsonify
from database.database import SessionLocal
from database.models import Destination, DestinationItinerary
from services.cloudinary_service import CloudinaryService
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

destinations_bp = Blueprint('destinations_bp', __name__)

# --- Helper for safe numeric conversion ---
def safe_int(val, default):
    try:
        return int(val) if val and str(val).strip() else default
    except (ValueError, TypeError):
        return default

# --- Helper for Itinerary Synchronization ---
def handle_itinerary_sync(db, destination_id, itinerary_json):
    """Parses itinerary JSON and syncs it to the database."""
    if not itinerary_json:
        return
    
    try:
        # 1. Parse the JSON string sent from the frontend
        steps = json.loads(itinerary_json)
        
        # 2. Clear existing steps for this destination (prevents duplicates on update)
        db.query(DestinationItinerary).filter(DestinationItinerary.destination_id == destination_id).delete()
        
        # 3. Insert new steps from the builder
        for step in steps:
            # We map 'day_number' from frontend and provide a fallback for 'icon'
            new_step = DestinationItinerary(
                destination_id=destination_id,
                day_number=step.get('day_number'),
                title=step.get('title'),
                activity=step.get('activity'),
                icon=step.get('icon', 'fa-map-marker-alt')
            )
            db.add(new_step)
    except Exception as e:
        print(f"Intelligence Sync Error (Itinerary): {str(e)}")
        # We don't raise the error here to allow the main destination to save 
        # but you could raise it if itinerary is mandatory.

@destinations_bp.route('/destinations', methods=['GET'])
def get_destinations():
    db = SessionLocal()
    try:
        all_destinations = db.query(Destination).order_by(Destination.created_at.desc()).all()
        return jsonify({
            "success": True,
            "count": len(all_destinations),
            "data": [d.to_dict() for d in all_destinations]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Database Error: {str(e)}"}), 500
    finally:
        db.close()

@destinations_bp.route('/destinations/add', methods=['POST'])
def add_destination():
    db = SessionLocal()
    try:
        # 1. Extract Mandatory Fields
        name = request.form.get('name')
        region = request.form.get('region')
        
        if not name or not region:
            return jsonify({"success": False, "message": "Location Name and Region are mandatory."}), 400

        # 2. Extract All Fields
        category = request.form.get('category', 'Beach')
        price = safe_int(request.form.get('price'), 0)
        excerpt = request.form.get('excerpt', '')
        description = request.form.get('description', '')
        status = request.form.get('status', 'Optimal')
        temp = safe_int(request.form.get('temp'), 25)
        weather = request.form.get('weather', 'Clear')
        capacity = safe_int(request.form.get('capacity'), 0)
        active_vips = safe_int(request.form.get('activeVips'), 0)

        # 3. Image Upload logic
        if 'image' not in request.files:
            return jsonify({"success": False, "message": "Strategic visual asset is required."}), 400
        
        image_file = request.files['image']
        image_url = CloudinaryService.upload_image(image_file, folder="indoria_hotspots")
        
        if not image_url:
            return jsonify({"success": False, "message": "Cloudinary synchronization failed."}), 500

        # 4. Create Record
        new_hotspot = Destination(
            name=name,
            region=region,
            category=category,
            price=price,
            excerpt=excerpt,
            description=description,
            status=status,
            temp=temp,
            weather=weather,
            capacity=capacity,
            active_vips=active_vips,
            image=image_url,
            is_featured=True 
        )

        db.add(new_hotspot)
        
        # 5. Flush to generate the UUID for the itinerary relationship
        db.flush() 

        # 6. Handle Itinerary Sync
        itinerary_data = request.form.get('itinerary')
        handle_itinerary_sync(db, new_hotspot.id, itinerary_data)

        db.commit()
        db.refresh(new_hotspot) 

        return jsonify({
            "success": True, 
            "message": "Deployed successfully.", 
            "destination": new_hotspot.to_dict()
        }), 201

    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": f"System Error: {str(e)}"}), 500
    finally:
        db.close()

@destinations_bp.route('/destinations/<string:id>', methods=['PUT'])
def update_destination(id):
    db = SessionLocal()
    try:
        target = db.query(Destination).filter(Destination.id == id).first()
        if not target:
            return jsonify({"success": False, "message": "Hotspot not found."}), 404

        # Update Text Fields
        target.name = request.form.get('name', target.name)
        target.region = request.form.get('region', target.region)
        target.category = request.form.get('category', target.category)
        target.excerpt = request.form.get('excerpt', target.excerpt)
        target.description = request.form.get('description', target.description)
        target.status = request.form.get('status', target.status)
        target.weather = request.form.get('weather', target.weather)

        # Update Numeric Fields
        target.price = safe_int(request.form.get('price'), target.price)
        target.temp = safe_int(request.form.get('temp'), target.temp)
        target.capacity = safe_int(request.form.get('capacity'), target.capacity)
        target.active_vips = safe_int(request.form.get('activeVips'), target.active_vips)

        # Update Image only if a new file is provided
        if 'image' in request.files:
            new_image_url = CloudinaryService.upload_image(request.files['image'], folder="indoria_hotspots")
            if new_image_url:
                target.image = new_image_url

        # Handle Itinerary Update
        itinerary_data = request.form.get('itinerary')
        handle_itinerary_sync(db, id, itinerary_data)

        db.commit()
        return jsonify({"success": True, "message": "Records updated.", "data": target.to_dict()}), 200

    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()

@destinations_bp.route('/destinations/<string:id>', methods=['DELETE'])
def decommission_destination(id):
    db = SessionLocal()
    try:
        target = db.query(Destination).filter(Destination.id == id).first()
        if not target:
            return jsonify({"success": False, "message": "Target hotspot not found."}), 404
        
        # Note: If you have Cascade Delete set in models, it will remove itinerary too
        db.delete(target)
        db.commit()
        return jsonify({"success": True, "message": "Hotspot decommissioned."}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()

@destinations_bp.route('/destinations/<id>/details', methods=['GET'])
def get_destination_details(id):
    db = SessionLocal()
    try:
        dest = db.query(Destination).filter(Destination.id == id).first()
        if not dest:
            return jsonify({"success": False, "message": "Not found"}), 404
        
        # Fetch the itinerary days for this destination
        itinerary = db.query(DestinationItinerary).filter(
            DestinationItinerary.destination_id == id
        ).order_by(DestinationItinerary.day_number).all()
        
        data = dest.to_dict()
        # Convert list of SQLAlchemy objects to list of dictionaries
        data['itinerary'] = [item.to_dict() for item in itinerary]
        
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        db.close()