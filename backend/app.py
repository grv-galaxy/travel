# from app_factory import create_app
# from routes import register_routes

# app = create_app()
# register_routes(app)

# if __name__ == "__main__":
#     # Start on Port 5000
#     app.run(debug=True, port=5000)


import os
from app_factory import create_app


# Initialize the application using the factory pattern
app = create_app()

if __name__ == "__main__":
    # PRODUCTION SETTINGS:
    # 1. We remove debug=True because it is a security risk in production.
    # 2. We use the 'PORT' environment variable provided by Google Cloud Run.
    # 3. We bind to 0.0.0.0 so the container is accessible externally.
    
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)