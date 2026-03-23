from database.database import SessionLocal
from database.models.admin import Admin
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SessionLocal()

def create_initial_admin():
    # Hash the password first!
    hashed_pw = bcrypt.generate_password_hash('indoria123').decode('utf-8')
    
    new_admin = Admin(
        username="Superintendent",
        email="admin@indoria.com",
        password=hashed_pw,
        role="Super Admin"
    )
    
    db.add(new_admin)
    db.commit()
    print("Admin Created: admin@indoria.com / indoria123")

if __name__ == "__main__":
    create_initial_admin()