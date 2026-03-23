import uuid
from sqlalchemy.ext.declarative import declarative_base

# The source of truth for all your tables
Base = declarative_base()

def generate_uuid():
    """Generates a unique 36-character string for primary keys."""
    return str(uuid.uuid4())