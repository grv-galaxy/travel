# import os
# import sys
# from pathlib import Path
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv

# # Load .env from the backend root (one level above /database)
# load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# # Fix import path so 'models' package is found
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# from models import Base

# # 1. FETCH NEON URL
# DATABASE_URL = os.getenv("DATABASE_URL")

# # 2. CONFIGURE ENGINE FOR NEON
# if DATABASE_URL:
#     if "sslmode" not in DATABASE_URL:
#         DATABASE_URL += "?sslmode=require"

#     engine = create_engine(
#         DATABASE_URL,
#         pool_pre_ping=True,   # Wakes up Neon if it's sleeping
#         pool_recycle=300,     # Refreshes connections every 5 minutes
#         pool_size=10,
#         max_overflow=20
#     )
# else:
#     raise RuntimeError("DATABASE_URL not found! Add it to your .env file or Render environment variables.")

# # 3. SESSION FACTORY
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # 4. INITIALIZE TABLES ON NEON
# def init_db():
#     """Creates tables on Neon if they don't exist."""
#     try:
#         Base.metadata.create_all(bind=engine)
#         print("Neon Database connected and tables initialized.")
#     except Exception as e:
#         print(f"Neon Connection Error: {e}")

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# if __name__ == "__main__":
#     init_db()










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