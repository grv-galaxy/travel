# from sqlalchemy import Column, String, Integer, Enum, Text, JSON, DateTime, ForeignKey, Boolean
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
# from .base import Base, generate_uuid

# # --- THE DESTINATION (Updated for Global Hotspots Dashboard) ---
# class Destination(Base):
#     __tablename__ = 'destinations'

#     id = Column(String(36), primary_key=True, default=generate_uuid)
#     name = Column(String(255), nullable=False, unique=True) 
#     region = Column(String(255)) # This acts as the "location" in your UI (e.g., Greece)
    
#     # --- NEW FIELDS FOR "EXPLORE THE WORLD" SECTION ---
#     category = Column(String(50), default='Beach') # Beach, Mountain, City, Cultural
#     price = Column(Integer, default=0)             # e.g., 1200
#     excerpt = Column(Text)                         # Short card description
#     # --------------------------------------------------

#     # Live Intelligence Fields
#     status = Column(String(50), default='Optimal') 
#     active_vips = Column(Integer, default=0)       
#     capacity = Column(Integer, default=0)          
#     temp = Column(Integer, default=25)             
#     weather = Column(String(100), default='Clear') 
    
#     # Visuals & Content
#     description = Column(Text)                     # Full heritage story
#     image = Column(Text)                           # Main card image
#     gallery = Column(JSON, default=[])             
#     is_featured = Column(Boolean, default=False) 
    
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "location": self.region,        # Mapped to 'location' for your UI
#             "category": self.category,      # Added for filtering
#             "price": self.price,            # Added for pricing
#             "excerpt": self.excerpt,        # Added for short description
#             "status": self.status,
#             "activeVips": self.active_vips,
#             "capacity": self.capacity,
#             "temp": self.temp,
#             "weather": self.weather,
#             "image": self.image,
#             "description": self.description
#         }


# class DestinationItinerary(Base):
#     __tablename__ = 'destination_itineraries'

#     id = Column(String(36), primary_key=True, default=generate_uuid)
#     destination_id = Column(String(36), ForeignKey('destinations.id'))
#     day_number = Column(Integer) # Day 1, Day 2, etc.
#     title = Column(String(255))
#     activity = Column(Text)
#     icon = Column(String(50), default='fa-map-marker-alt')

#     def to_dict(self):
#         return {
#             "day": self.day_number,
#             "title": self.title,
#             "activity": self.activity,
#             "icon": self.icon
#         }

        
# # --- THE BOOKING (Data for Uplans.vue) ---
# class TravelPackage(Base):
#     __tablename__ = 'travel_packages'

#     id = Column(String(36), primary_key=True, default=generate_uuid)
#     user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
#     package_name = Column(String(255), nullable=False) # e.g., 'Imperial Heritage'
#     destination_city = Column(String(255))
#     arrival_date = Column(DateTime(timezone=True))
#     duration_nights = Column(Integer)
#     hero_image_url = Column(Text)
#     inclusions = Column(JSON, default=[]) # List of perks: ["Butler", "Wifi", "Champagne"]
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     # Links back to User and down to Itinerary
#     user = relationship("User", back_populates="packages")
#     itinerary = relationship("ItineraryMoment", back_populates="package", cascade="all, delete-orphan")

# # --- THE TIMELINE (Data for Ujourney.vue) ---
# class ItineraryMoment(Base):
#     __tablename__ = 'itinerary_moments'

#     id = Column(String(36), primary_key=True, default=generate_uuid)
#     package_id = Column(String(36), ForeignKey('travel_packages.id'), nullable=False)
#     scheduled_time = Column(DateTime(timezone=True))
#     title = Column(String(255), nullable=False) # e.g., 'Fleet Connection'
#     description = Column(Text)
#     location = Column(String(255))
#     icon_class = Column(String(100)) # FontAwesome icon used in vertical timeline
#     status = Column(Enum('Completed', 'Active', 'Upcoming', name='moment_status'), default='Upcoming')

#     package = relationship("TravelPackage", back_populates="itinerary")


























from sqlalchemy import Column, String, Integer, Enum, Text, JSON, DateTime, ForeignKey, Boolean, Index
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from .base import Base, generate_uuid

# --- THE DESTINATION (The Master Hotspot) ---
class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(255), nullable=False, unique=True, index=True) 
    region = Column(String(255), index=True) 
    
    category = Column(Enum('Beach', 'Mountain', 'City', 'Cultural', name='dest_category'), default='Beach', index=True)
    price = Column(Integer, default=0) 
    excerpt = Column(Text) 

    # Live Intelligence Fields (Optimized for frequent updates)
    status = Column(Enum('Optimal', 'High Peak', 'Restricted', name='dest_status'), default='Optimal', index=True)
    active_vips = Column(Integer, default=0)        
    capacity = Column(Integer, default=0)           
    temp = Column(Integer, default=25)              
    weather = Column(String(100), default='Clear') 
    
    # Visuals & Content
    description = Column(Text) 
    image = Column(Text) # Cloudinary URL
    gallery = Column(JSON, default=[])              
    is_featured = Column(Boolean, default=False, index=True) 
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    # RELATIONSHIPS
    # If a Destination is deleted, its daily itineraries MUST be deleted (delete-orphan)
    itineraries = relationship(
        "DestinationItinerary", 
        back_populates="destination", 
        cascade="all, delete-orphan",
        passive_deletes=True,
        order_by="DestinationItinerary.day_number"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "region": self.region,
            "category": self.category,
            "price": self.price,
            "excerpt": self.excerpt,
            "status": self.status,
            "activeVips": self.active_vips,
            "capacity": self.capacity,
            "temp": self.temp,
            "weather": self.weather,
            "image": self.image,
            "description": self.description,
            "itinerary": [i.to_dict() for i in self.itineraries]
        }

# --- DESTINATION ITINERARY (Daily Templates) ---
class DestinationItinerary(Base):
    __tablename__ = 'destination_itineraries'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    # ondelete="CASCADE" at the FK level is critical for database-level cleanup
    destination_id = Column(String(36), ForeignKey('destinations.id', ondelete="CASCADE"), nullable=False)
    
    day_number = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
    activity = Column(Text)
    icon = Column(String(50), default='fa-map-marker-alt')

    destination = relationship("Destination", back_populates="itineraries")

    def to_dict(self):
        return {
            "day_number": self.day_number,
            "title": self.title,
            "activity": self.activity,
            "icon": self.icon
        }

# --- TRAVEL PACKAGE (User Bookings) ---
class TravelPackage(Base):
    __tablename__ = 'travel_packages'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey('users.id', ondelete="CASCADE"), nullable=False, index=True)
    
    package_name = Column(String(255), nullable=False)
    destination_city = Column(String(255), index=True)
    arrival_date = Column(DateTime(timezone=True))
    duration_nights = Column(Integer)
    hero_image_url = Column(Text)
    inclusions = Column(JSON, default=[]) 
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="packages")
    moments = relationship("ItineraryMoment", back_populates="package", cascade="all, delete-orphan", passive_deletes=True)

# --- ITINERARY MOMENT (Timeline Events) ---
class ItineraryMoment(Base):
    __tablename__ = 'itinerary_moments'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    package_id = Column(String(36), ForeignKey('travel_packages.id', ondelete="CASCADE"), nullable=False)
    
    scheduled_time = Column(DateTime(timezone=True), index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    location = Column(String(255))
    icon_class = Column(String(100))
    status = Column(Enum('Completed', 'Active', 'Upcoming', name='moment_status'), default='Upcoming', index=True)

    package = relationship("TravelPackage", back_populates="moments")