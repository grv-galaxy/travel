from sqlalchemy import Column, String, Boolean, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base, generate_uuid

class Admin(Base):
    __tablename__ = 'admins'

    # Primary Key using secure UUID
    id = Column(String(36), primary_key=True, default=generate_uuid)
    
    # Credentials
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False) # Argon2/Bcrypt hash
    
    # Role-Based Access Control (RBAC)
    role = Column(Enum('SuperAdmin', 'Manager', 'Support', name='admin_roles'), default='Support')
    is_active = Column(Boolean, default=True)
    
    # Audit Trail: Tracks the 'Chain of Command'
    # Used to verify who authorized this specific admin account
    added_by_id = Column(String(36), ForeignKey('admins.id'), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_login = Column(DateTime(timezone=True))

    # Self-referential relationship: Allows an admin to have 'created_accounts'
    added_by_admin = relationship("Admin", remote_side=[id], backref="created_accounts")

    def __repr__(self):
        return f"<Admin(name={self.full_name}, role={self.role})>"