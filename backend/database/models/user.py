from sqlalchemy import Column, String, Integer, Enum, Text, JSON, DateTime, Numeric, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime 
from .base import Base, generate_uuid

class User(Base):
    __tablename__ = 'users'

    # Secure unique identifier for the traveler
    id = Column(String(36), primary_key=True, default=generate_uuid)
    
    # Basic Identity
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20), unique=True, nullable=True, index=True)

    #password = Column(String(255))
    is_email_verified = Column(Boolean, default=False) 
    is_phone_verified = Column(Boolean, default=False)
    auth_provider = Column(String(20), default='google')

    # Membership & Tier System (e.g., 'Gold Maharaja')
    tier = Column(Enum('Silver', 'Gold Maharaja', 'Platinum Imperial', name='user_tiers'), default='Gold Maharaja')
    loyalty_points = Column(Integer, default=0)
    profile_image = Column(Text) # URL to cloud-hosted avatar
    
    # Luxury Preferences: Highly important for personalization
    # Stores JSON like: {"temp": 21, "mood": "Jazz", "wine": "Krug 2008"}
    preferences = Column(JSON, default=lambda: {}) 
    passport_id = Column(String(50), unique=True)
    total_spend = Column(Numeric(12,2), default=0.00)
    last_seen = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default='Active')
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # --- Relationships ---
    # These allow us to fetch all data for a user in one go (e.g., user.packages)
    packages = relationship("TravelPackage", back_populates="user", cascade="all, delete-orphan")
    fleet = relationship("FleetAssignment", back_populates="user", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="user")
    documents = relationship("Document", back_populates="user")
    messages = relationship("Message", back_populates="user")

    def __repr__(self):
        return f"<User(name={self.full_name}, tier={self.tier})>"