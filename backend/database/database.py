# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from database.models.base import Base
# #sfrom models import Base

# # 1. DATABASE URL CONFIGURATION
# # We use an environment variable for Production (Neon) 
# # and a local file for Development (SQLite).
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_PATH = os.path.join(BASE_DIR, "indoria_concierge.db")
# DATABASE_URL = 'postgresql://neondb_owner:npg_JTd3pnikMmG5@ep-royal-sound-a1rst6ld-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

# # 2. CREATE THE ENGINE
# # 'check_same_thread' is only required for SQLite.
# if DATABASE_URL.startswith("sqlite"):
#     engine = create_engine(
#         DATABASE_URL, connect_args={"check_same_thread": False}
#     )
# else:
#     # Production settings for Neon/PostgreSQL
#     engine = create_engine(
#         DATABASE_URL, 
#         pool_size=10, 
#         max_overflow=20
#     )

# # 3. SESSION FACTORY
# # Each request to your API will get its own temporary database session.
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # 4. DATABASE INITIALIZATION
# def init_db():
#     """
#     Creates all tables in the database based on our modular models.
#     Run this once at startup or via a setup script.
#     """
#     print(f"Connecting to: {DATABASE_URL}")
#     try:
#         # This command scans models/__init__.py and creates everything
#         Base.metadata.create_all(bind=engine)
#         print("Success: All luxury vault tables initialized.")
#     except Exception as e:
#         print(f"Error initializing database: {e}")

# # 5. DEPENDENCY (For FastAPI/Flask)
# def get_db():
#     """
#     Helper function to provide a database session to API routes.
#     Ensures the connection is closed after the request is finished.
#     """
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()











import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models.base import Base
#from models import Base
from dotenv import load_dotenv  # 1. Add this import



# 1. FETCH NEON URL
# This must match the name of the Secret in Cloud Run (usually DATABASE_URL)
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. CONFIGURE ENGINE FOR NEON
# Neon is serverless and requires SSL + connection health checks
if DATABASE_URL:
    if "sslmode" not in DATABASE_URL:
        DATABASE_URL += "?sslmode=require"

    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,  # Crucial: Wakes up Neon if it's sleeping
        pool_recycle=300,     # Refreshes connections every 5 minutes
        pool_size=10,
        max_overflow=20
    )
else:
    raise RuntimeError("DATABASE_URL not found! Set it in Cloud Run Secrets.")

# 3. SESSION FACTORY
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. INITIALIZE TABLES ON NEON
def init_db():
    """Creates tables on Neon if they don't exist."""
    try:
        Base.metadata.create_all(bind=engine)
        print("Neon Database connected and tables initialized.")
    except Exception as e:
        print(f"Neon Connection Error: {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()