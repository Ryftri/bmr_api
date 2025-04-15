# app/__init__.py

from flask import Flask, request
from app.routes.bmr_routes import bmr_bp  # Pastikan mengimpor Blueprint yang sudah dibuat

def create_app():
    app = Flask(__name__)

    @app.before_request
    def log_ip():
        user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        print(f"Request received from IP: {user_ip}")

    app.register_blueprint(bmr_bp)
    
    return app
