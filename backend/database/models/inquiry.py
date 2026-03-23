from sqlalchemy import Column, String, Integer, Enum, Text, JSON, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base, generate_uuid

class Inquiry(Base):
    __tablename__ = 'inquiries'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(50))
    destination_type = Column(String(100)) # e.g. 'International'
    travelers = Column(Integer, default=1)
    message = Column(Text)
    status = Column(String(20), default='New') 
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "destination": self.destination_type,
            "travelers": self.travelers,
            "message": self.message,
            "status": self.status,
            "date": self.created_at.isoformat()
        }