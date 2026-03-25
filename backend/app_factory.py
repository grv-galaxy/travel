# from flask import Flask
# from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from flask_bcrypt import Bcrypt
# from routes.auth_routes import auth_bp
# from routes.uprofile import uprofile_bp
# from services.cloudinary_service import CloudinaryService

# bcrypt = Bcrypt()
# jwt = JWTManager()

# def create_app():
#     app = Flask(__name__)

#     # Configuration
#     app.config['JWT_SECRET_KEY'] = 'INDORIA_VIP_KEY_2025' # Secret for signing tokens
#     app.config['CLOUDINARY'] = CloudinaryService
    
#     # Initialize Plugins
#     CORS(app, resources={r"/api/*":{"origin":"https://travel-xxnc.onrender.com/"}})  # Allows Vue to talk to Flask
#     bcrypt.init_app(app)
#     jwt.init_app(app)

#     # Register Blueprints (The "When": Link routes to the app)
#     app.register_blueprint(auth_bp, url_prefix='/api/auth')
#     app.register_blueprint(uprofile_bp, url_prefix='/api/uprofile')

#     return app











# import os
# from flask import Flask
# from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from flask_bcrypt import Bcrypt
# from dotenv import load_dotenv
# from routes.auth_routes import auth_bp
# from routes.uprofile import uprofile_bp
# from services.cloudinary_service import CloudinaryService
# from routes import register_routes

# # Load variables from .env if it exists (useful for local dev)
# load_dotenv()

# bcrypt = Bcrypt()
# jwt = JWTManager()

# def create_app():
#     app = Flask(__name__)

#     # --- Configuration ---
#     # Fetch from Environment Variables for Security. 
#     # Always provide a long, random fallback for safety.
#     app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-fallback-key-replace-this')
#     app.config['CLOUDINARY'] = CloudinaryService

#     # --- Initialize Plugins ---
    
#     # PRODUCTION CORS: 
#     # We allow your custom domain and localhost for testing.
#     # Using a list is cleaner and more professional.
#     allowed_origins = [
#         "https://indoria-gcodes.co.in",
#         "https://www.indoria-gcodes.co.in",
#         "http://localhost:5173",
#         "https://indoriatravelfrontend-fb6b2.web.app"
#     ]
    
#     CORS(app, resources={r"/api/*": {"origins": allowed_origins}})
    
#     bcrypt.init_app(app)
#     jwt.init_app(app)

#     # # --- Register Blueprints ---
#     register_routes(app)

#     return app














# import os
# from flask import Flask
# from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from flask_bcrypt import Bcrypt
# from dotenv import load_dotenv
# from services.cloudinary_service import CloudinaryService
# from routes import register_routes

# # Load variables from .env if it exists (useful for local dev)
# load_dotenv()

# bcrypt = Bcrypt()
# jwt = JWTManager()

# def create_app():
#     app = Flask(__name__)

#     # --- Configuration ---
#     app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-fallback-key-replace-this')
#     app.config['CLOUDINARY'] = CloudinaryService

#     # --- Initialize Plugins ---
#     allowed_origins = [
#         "https://indoria-gcodes.co.in",
#         "https://www.indoria-gcodes.co.in",
#         "http://localhost:5173",
#         "https://indoriatravelfrontend-fb6b2.web.app"
#     ]
    
#     CORS(app, 
#          resources={r"/api/*": {"origins": allowed_origins}},
#          allow_headers=['Content-Type', 'Authorization'],
#          methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
#          supports_credentials=True)
    
#     bcrypt.init_app(app)
#     jwt.init_app(app)

#     # --- Register Blueprints ---
#     register_routes(app)

#     return app
















import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from services.cloudinary_service import CloudinaryService
from routes import register_routes
# import firebase_admin
# from firebase_admin import credentials, auth as firebase_auth

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate('./serviceAccountKey.json')
# firebase_admin.initialize_app(cred)

load_dotenv()

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-fallback-key-replace-this')
    app.config['CLOUDINARY'] = CloudinaryService

    allowed_origins = [
        "https://indoria.gcodes.co.in",
        "https://www.indoria.gcodes.co.in",
        "https://travel-8f96a.web.app",
        "https://travel-8f96a.firebaseapp.com",

    ]
    
    # ✅ FIXED CORS - explicitly allow content-type
    CORS(app, 
         resources={r"/api/*": {"origins": allowed_origins}},
         allow_headers=['Content-Type', 'Authorization'],
         methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
        #  expose_headers=['Content-Type', 'Authorization'],
         supports_credentials=True)
    
    

    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = jsonify({'status': 'ok'})
            response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin', '')
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            return response, 200

    bcrypt.init_app(app)
    jwt.init_app(app)
    
    register_routes(app)

    return app