# from sqlalchemy import Column, String, Integer, Boolean, Numeric, ForeignKey, DateTime, Text, Enum
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
# from .base import Base, generate_uuid

# # --- THE MASTER INVENTORY (Master Table for Fleet Command) ---
# class FleetAsset(Base):
#     __tablename__ = 'fleet_assets'

#     id = Column(String(36), primary_key=True, default=generate_uuid)
#     name = Column(String(255), nullable=False) # e.g., 'Phantom Series II'
#     type = Column(String(50), nullable=False) # 'Luxury Sedan', 'Private Jet', etc.
#     license_plate = Column(String(50), unique=True, nullable=False)
#     image_url = Column(Text) # Cloudinary URL
#     status = Column(String(50), default='Available') # 'Available', 'In-Transit', 'Maintenance'
#     fuel_level = Column(Integer, default=100)
    
#     # specifications stored as JSON string for SQLite compatibility
#     specifications = Column(Text, default='{}') 
    
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     # Relationship to see history of assignments for this specific vehicle
#     assignments = relationship("FleetAssignment", back_populates="asset")


# # --- THE FLEET ASSIGNMENTS (Live Tracking & VIP Connection) ---
# class FleetAssignment(Base):
#     __tablename__ = 'fleet_assignments'

#     id = Column(String(36), primary_key=True, default=generate_uuid)
#     user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    
#     # Link to the Master Inventory Asset
#     asset_id = Column(String(36), ForeignKey('fleet_assets.id'), nullable=True)
    
#     # Chauffeur & Vehicle Snapshot Details
#     chauffeur_name = Column(String(255))
#     chauffeur_rating = Column(Numeric(3, 2)) # e.g., 4.95
#     vehicle_model = Column(String(255))      # e.g., 'Mercedes-Maybach S-Class'
#     license_plate = Column(String(50))
#     wifi_password = Column(String(100))
    
#     # Live Cabin Telematics (Updated by Vue sliders)
#     current_temp = Column(Integer, default=21)
#     current_mood = Column(String(100))       # e.g., 'Classic Jazz'
#     eta_minutes = Column(Integer)            # Live countdown to arrival
    
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())

#     # Relationships
#     user = relationship("User", back_populates="fleet")
#     asset = relationship("FleetAsset", back_populates="assignments")


# # --- CONCIERGE MESSAGING (Data for Uconcierge.vue) ---
# class Message(Base):
#     __tablename__ = 'messages'

#     id = Column(String(36), primary_key=True, default=generate_uuid)
#     user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    
#     # Distinguishes between traveler and the butler
#     sender_role = Column(Enum('user', 'concierge', name='roles'), nullable=False)
#     text = Column(Text, nullable=False)
#     is_read = Column(Boolean, default=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     user = relationship("User", back_populates="messages")






























from sqlalchemy import Column, String, Integer, Boolean, Numeric, ForeignKey, DateTime, Text, Enum, Index
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from .base import Base, generate_uuid

# --- THE MASTER INVENTORY ---
class FleetAsset(Base):
    __tablename__ = 'fleet_assets'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(255), nullable=False, index=True) 
    type = Column(String(50), nullable=False, index=True) 
    license_plate = Column(String(50), unique=True, nullable=False)
    image_url = Column(Text) 
    
    # Using Enum for status ensures data integrity at the DB level
    status = Column(Enum('Available', 'In-Transit', 'Maintenance', 'Decommissioned', name='asset_status'), default='Available')
    fuel_level = Column(Integer, default=100)
    specifications = Column(Text, default='{}') 
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    # --- RELATIONSHIP STRATEGY ---
    # cascade="all, delete-orphan" means if the asset is deleted, 
    # the assignments are also deleted. 
    # HOWEVER: For auditing, we usually use passive_deletes or set null.
    assignments = relationship(
        "FleetAssignment", 
        back_populates="asset",
        cascade="all, delete-orphan", # Remove assignments if asset is purged
        passive_deletes=True 
    )

# --- THE FLEET ASSIGNMENTS ---
class FleetAssignment(Base):
    __tablename__ = 'fleet_assignments'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    
    # ondelete="CASCADE" ensures that if the User is deleted, 
    # the assignment record is wiped from the DB automatically.
    user_id = Column(String(36), ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    asset_id = Column(String(36), ForeignKey('fleet_assets.id', ondelete="SET NULL"), nullable=True)
    
    chauffeur_name = Column(String(255))
    chauffeur_rating = Column(Numeric(3, 2))
    vehicle_model = Column(String(255)) 
    license_plate = Column(String(50))
    wifi_password = Column(String(100))
    
    current_temp = Column(Integer, default=21)
    current_mood = Column(String(100))
    eta_minutes = Column(Integer, index=True) # Index for sorting by arrival time
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="fleet")
    asset = relationship("FleetAsset", back_populates="assignments")

# --- CONCIERGE MESSAGING ---
class Message(Base):
    __tablename__ = 'messages'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey('users.id', ondelete="CASCADE"), nullable=False, index=True)
    
    sender_role = Column(Enum('user', 'concierge', name='sender_roles'), nullable=False)
    text = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    user = relationship("User", back_populates="messages")