from .auth_routes import auth_bp
from .Atravelers import travelers_bp
from .uprofile import uprofile_bp
from .Afleet import afleet_bp
from .Adestination import destinations_bp
from .Uinquiry import inquiries_bp
from .Udocument import udocument_bp
from .Asecurity import security_bp 

def register_routes(app):
    # Auth uses /api/auth
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    # User Profile uses /api/user
    app.register_blueprint(uprofile_bp, url_prefix='/api/user')
    
    # Inquiries uses /api
    app.register_blueprint(inquiries_bp, url_prefix='/api')

    # ADMIN SECTION
    # We combine these under /api/admin. 
    app.register_blueprint(travelers_bp, url_prefix='/api/admin')
    app.register_blueprint(afleet_bp, url_prefix='/api/admin')
    app.register_blueprint(destinations_bp, url_prefix='/api/admin')
    
    # 2. Register the Security/Admin Management blueprint
    # This makes your endpoint: /api/admin/api/admins (or similar depending on your @bp.route)
    app.register_blueprint(security_bp, url_prefix='/api/admin')

    app.register_blueprint(udocument_bp, url_prefix='/api/user')