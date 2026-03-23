# from database import engine, SessionLocal, init_db
# from models import Admin, User, Destination, TravelPackage, FleetAssignment
# from flask_bcrypt import Bcrypt
# from datetime import datetime, timedelta

# bcrypt = Bcrypt()

# def seed_data():
#     db = SessionLocal()
#     try:
#         # --- 1. Create the Root Admin ---
#         # This is the person who will manage the Indoria Concierge platform
#         if not db.query(Admin).filter_by(email="admin@indoria.com").first():
#             hashed_password = bcrypt.generate_password_hash("Indoria2025!").decode('utf-8')
#             root_admin = Admin(
#                 full_name="Indoria System Admin",
#                 email="admin@indoria.com",
#                 password_hash=hashed_password,
#                 role="SuperAdmin"
#             )
#             db.add(root_admin)
#             print("✓ Created SuperAdmin: admin@indoria.com")

#         # --- 2. Create a Featured Destination ---
#         # This will show up in your Destinations.vue
#         if not db.query(Destination).filter_by(city_name="Udaipur").first():
#             udaipur = Destination(
#                 city_name="Udaipur",
#                 region="Rajasthan",
#                 description="The City of Lakes and the historic capital of the kingdom of Mewar.",
#                 cover_image="https://images.unsplash.com/photo-1590050752117-23a9d7fc2173",
#                 gallery=["https://images.unsplash.com/photo-1615469038354-be1324b1d890"],
#                 is_featured=True
#             )
#             db.add(udaipur)
#             print("✓ Seeded Destination: Udaipur")

#         # --- 3. Create a VIP Traveler ---
#         # This traveler will see their data in the User Dashboard
#         if not db.query(User).filter_by(email="maharaja@elite.com").first():
#             vip_user = User(
#                 full_name="Maharaja Vikram Singh",
#                 email="maharaja@elite.com",
#                 phone="+91 99999 88888",
#                 tier="Platinum Imperial",
#                 loyalty_points=12500,
#                 preferences={"temp": 20, "mood": "Classical", "drink": "Darjeeling First Flush"}
#             )
#             db.add(vip_user)
#             db.flush() # Flush to get the ID for the next steps

#             # --- 4. Assign a Fleet (Car) to the Traveler ---
#             fleet = FleetAssignment(
#                 user_id=vip_user.id,
#                 chauffeur_name="Arjun",
#                 chauffeur_rating=4.98,
#                 vehicle_model="Rolls-Royce Ghost",
#                 license_plate="RJ 01 VIP 0001",
#                 wifi_password="indoria_private",
#                 eta_minutes=8
#             )
#             db.add(fleet)

#             # --- 5. Create an Active Travel Package ---
#             package = TravelPackage(
#                 user_id=vip_user.id,
#                 package_name="Royal Rajputana Tour",
#                 destination_city="Udaipur",
#                 arrival_date=datetime.now() + timedelta(days=2),
#                 duration_nights=5,
#                 hero_image_url="https://images.unsplash.com/photo-1590050752117-23a9d7fc2173",
#                 inclusions=["Private Jet Transfer", "24/7 Butler", "Palace Access"]
#             )
#             db.add(package)
            
#             print("✓ Created VIP User: Maharaja Vikram Singh")

#         db.commit()
#         print("\n[SUCCESS] Database is fully seeded and ready for the Vue frontend.")

#     except Exception as e:
#         print(f"Error during seeding: {e}")
#         db.rollback()
#     finally:
#         db.close()

# if __name__ == "__main__":
#     # First, create the tables
#     init_db()
#     # Second, add the dummy data
#     seed_data()



# from database import engine, SessionLocal, init_db
# from models import Admin, User, Destination, TravelPackage, FleetAssignment, DestinationItinerary
# from flask_bcrypt import Bcrypt
# from datetime import datetime, timedelta

# bcrypt = Bcrypt()

# def seed_data():
#     db = SessionLocal()
#     try:
#         # --- 1. Create the Root Admin ---
#         if not db.query(Admin).filter_by(email="admin@indoria.com").first():
#             hashed_password = bcrypt.generate_password_hash("Indoria2025!").decode('utf-8')
#             root_admin = Admin(
#                 full_name="Indoria System Admin",
#                 email="admin@indoria.com",
#                 password_hash=hashed_password,
#                 role="SuperAdmin"
#             )
#             db.add(root_admin)
#             print("✓ Created SuperAdmin: admin@indoria.com")

#         # --- 2. Create Featured Hotspots with Default Details ---
        
#         # --- UDAIPUR SEED ---
#         udaipur = db.query(Destination).filter_by(name="Udaipur").first()
#         if not udaipur:
#             udaipur = Destination(
#                 name="Udaipur",
#                 region="Rajasthan, India",
#                 category="Cultural",
#                 price=85000,
#                 excerpt="Experience the Venice of the East with royal palace stays and private lake cruises.",
#                 status="Optimal",
#                 active_vips=12,
#                 capacity=45,
#                 temp=28,
#                 weather="Clear Sky",
#                 description="Udaipur, formerly the capital of the Mewar Kingdom, is a city of ivory palaces and shimmering lakes. Our curated journey takes you beyond the tourist paths into the private corridors of the City Palace and hidden artisan workshops.",
#                 image="https://images.unsplash.com/photo-1590050752117-23a9d7fc2173",
#                 is_featured=True
#             )
#             db.add(udaipur)
#             db.flush() # Get ID for itinerary

#             # Day-by-Day for Udaipur
#             itinerary_udaipur = [
#                 DestinationItinerary(destination_id=udaipur.id, day_number=1, title="Palatial Arrival", activity="Luxury fleet pickup from Maharana Pratap Airport followed by a private sunset check-in at Lake Palace."),
#                 DestinationItinerary(destination_id=udaipur.id, day_number=2, title="The Royal Heritage", activity="Private guided tour of the City Palace Museum including access to the restricted Crystal Gallery."),
#                 DestinationItinerary(destination_id=udaipur.id, day_number=3, title="Lakeside Serenity", activity="Exclusive boat charter on Lake Pichola with high tea served on Jagmandir Island."),
#             ]
#             db.add_all(itinerary_udaipur)
#             print("✓ Seeded Udaipur with Itinerary")

#         # --- MALDIVES SEED ---
#         maldives = db.query(Destination).filter_by(name="Maldives Atoll").first()
#         if not maldives:
#             maldives = Destination(
#                 name="Maldives Atoll",
#                 region="Indian Ocean",
#                 category="Beach",
#                 price=145000,
#                 excerpt="Ultra-luxury overwater villas and underwater dining in the world's most pristine waters.",
#                 status="High Peak",
#                 active_vips=24,
#                 capacity=82,
#                 temp=30,
#                 weather="Tropical",
#                 description="The Maldives is the pinnacle of seclusion. Indoria Concierge provides access to private islands where the sand is white silk and the service is invisible yet omnipresent.",
#                 image="https://images.unsplash.com/photo-1514282401047-d79a71a590e8",
#                 is_featured=True
#             )
#             db.add(maldives)
#             db.flush()

#             # Day-by-Day for Maldives
#             itinerary_maldives = [
#                 DestinationItinerary(destination_id=maldives.id, day_number=1, title="Seaplane Transfer", activity="Private seaplane flight over the atolls directly to your villa deck."),
#                 DestinationItinerary(destination_id=maldives.id, day_number=2, title="Deep Blue Exploration", activity="Guided snorkeling with a marine biologist in a protected reef zone."),
#                 DestinationItinerary(destination_id=maldives.id, day_number=3, title="Castaway Dinner", activity="Gourmet 5-course meal prepared by a private chef on a deserted sandbank under the stars."),
#             ]
#             db.add_all(itinerary_maldives)
#             print("✓ Seeded Maldives with Itinerary")

#         # --- 3. Create a VIP Traveler ---
#         if not db.query(User).filter_by(email="maharaja@elite.com").first():
#             vip_user = User(
#                 full_name="Maharaja Vikram Singh",
#                 email="maharaja@elite.com",
#                 phone="+91 99999 88888",
#                 tier="Platinum Imperial",
#                 loyalty_points=12500,
#                 preferences={"temp": 20, "mood": "Classical", "drink": "Darjeeling First Flush"}
#             )
#             db.add(vip_user)
#             db.flush() 

#             # --- 4. Assign a Fleet ---
#             fleet = FleetAssignment(
#                 user_id=vip_user.id,
#                 chauffeur_name="Arjun",
#                 chauffeur_rating=4.98,
#                 vehicle_model="Rolls-Royce Ghost",
#                 license_plate="RJ 01 VIP 0001",
#                 wifi_password="indoria_private",
#                 eta_minutes=8
#             )
#             db.add(fleet)

#             print("✓ Created VIP User: Maharaja Vikram Singh")

#         db.commit()
#         print("\n[SUCCESS] Database is fully seeded with detailed itineraries.")

#     except Exception as e:
#         print(f"Error during seeding: {e}")
#         db.rollback()
#     finally:
#         db.close()

# if __name__ == "__main__":
#     init_db()
#     seed_data()




from database import engine, SessionLocal, init_db
from models import Admin, User, Destination, TravelPackage, FleetAssignment, DestinationItinerary
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def setup_database():
    """
    Initializes the database schema and creates the mandatory 
    System Administrator account.
    """
    # 1. Create all tables in the database (Neon/Postgres)
    print("Connecting to database and creating tables...")
    init_db()
    
    db = SessionLocal()
    try:
        # 2. Create the Root Admin
        # We keep this because without an admin, you cannot log in to add new data.
        admin_email = "admin@indoria.com"
        if not db.query(Admin).filter_by(email=admin_email).first():
            hashed_password = bcrypt.generate_password_hash("Indoria2025!").decode('utf-8')
            root_admin = Admin(
                full_name="Indoria System Admin",
                email=admin_email,
                password_hash=hashed_password,
                role="SuperAdmin"
            )
            db.add(root_admin)
            db.commit()
            print(f"✓ Table Schema Created.")
            print(f"✓ Root Admin Created: {admin_email}")
        else:
            print("✓ Database tables verified. Admin already exists.")

        print("\n[SUCCESS] Database is ready. No dummy hotspots or users were added.")

    except Exception as e:
        print(f"Critical Error during setup: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    setup_database()