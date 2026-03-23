from sqlalchemy import Column, String, Numeric, Enum, Text, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base, generate_uuid

# --- THE LEDGER (Data for Upayment.vue) ---
class Payment(Base):
    __tablename__ = 'payments'

    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    
    # Financial Details
    transaction_ref = Column(String(100), unique=True, nullable=False) # e.g., IND-9921-X
    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String(3), default='INR')
    status = Column(Enum('Pending', 'Completed', 'Failed', name='payment_status'), default='Pending')
    description = Column(String(255)) # e.g., 'Premium Plus Portfolio'
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    invoice_url = Column(Text) # Link to the generated PDF receipt

    user = relationship("User", back_populates="payments")

# --- THE VAULT (Data for Udocuments.vue) ---
class Document(Base):
    __tablename__ = 'documents'

    # Identity
    id = Column(String(36), primary_key=True, default=generate_uuid)
    user_id = Column(String(36), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # Document Metadata
    doc_name = Column(String(255), nullable=False) # e.g., 'Passport - Main Page'
    doc_type = Column(Enum('Passport', 'Visa', 'Insurance', 'Health', name='doc_types'), nullable=False)
    
    # Storage Links
    file_url = Column(Text, nullable=False) # The secure path to view the file
    public_id = Column(Text, nullable=True) # ✅ CRITICAL: Required to delete the file from Cloudinary
    
    # Status & Expiry Logic
    status = Column(Enum('Verified', 'Pending', 'Expired', name='doc_status'), default='Pending')
    expiry_date = Column(Date, index=True) # Added index for faster queries on expiring docs
    verification_date = Column(DateTime(timezone=True))
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="documents")

    def to_dict(self):
        """Helper to convert SQL object to JSON for Vue frontend"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "doc_name": self.doc_name,
            "doc_type": str(self.doc_type.value) if hasattr(self.doc_type, 'value') else str(self.doc_type),
            "file_url": self.file_url,
            "public_id": self.public_id, # Added this
            "status": str(self.status.value) if hasattr(self.status, 'value') else str(self.status),
            "expiry_date": self.expiry_date.isoformat() if self.expiry_date else None,
            "uploaded_at": self.uploaded_at.isoformat() if self.uploaded_at else None
        }