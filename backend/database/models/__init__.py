# Import the Base and Utility
from .base import Base, generate_uuid

# Import Admin & Authentication
from .admin import Admin

# Import User Identity
from .user import User

# Import Travel & Itinerary
from .travel import Destination, TravelPackage, ItineraryMoment, DestinationItinerary

# Import Logistics & Messaging
from .logistics import FleetAssignment, Message, FleetAsset

# Import Finance & The Vault
from .finance import Payment, Document

# Import Inquiry
from .inquiry import Inquiry

# This list allows you to see exactly what models are exposed
__all__ = [
    "Base",
    "Admin",
    "User",
    "Destination",
    "DestinationItinerary",  # ADD THIS
    "TravelPackage",
    "ItineraryMoment",
    "FleetAsset",            # ADD THIS
    "FleetAssignment",
    "Message",
    "Payment",
    "Document",
    "Inquiry"
]