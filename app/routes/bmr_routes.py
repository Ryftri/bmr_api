# app/routes/bmr_routes.py

import os
from flask import Blueprint, request, jsonify, abort
from app.services.bmr_service import (
    calculate_bmr_mifflin,
    calculate_bmr_harris_original,
    calculate_bmr_harris_revised
)

bmr_bp = Blueprint('bmr', __name__)

# Decorator untuk mencetak IP dan header X-RapidAPI-Host
def log_ip(func):
    def wrapper(*args, **kwargs):
        # Mendapatkan IP pengguna
        user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        # Mendapatkan header X-RapidAPI-Host
        rapidapi_host = request.headers.get('X-RapidAPI-Host', 'Not Available')
        print(f"Request received from IP: {user_ip}")
        print(f"X-RapidAPI-Host: {rapidapi_host}")
        secret = request.headers.get("X-RapidAPI-Proxy-Secret")
        print(f"X-RapidAPI-Proxy-Secret : {secret}")
        print(os.environ.get("RAPIDAPI_SECRET"))
        if secret != os.environ.get("RAPIDAPI_SECRET"):
            abort(403)
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@bmr_bp.route('/api/bmr/mifflin', methods=['POST'])
@log_ip
def mifflin_bmr():
    data = request.get_json()
    result = calculate_bmr_mifflin(data)
    return jsonify(result)

@bmr_bp.route('/api/bmr/harris-original', methods=['POST'])
@log_ip
def harris_original():
    data = request.get_json()
    result = calculate_bmr_harris_original(data)
    return jsonify(result)

@bmr_bp.route('/api/bmr/harris-revised', methods=['POST'])
@log_ip
def harris_revised():
    data = request.get_json()
    result = calculate_bmr_harris_revised(data)
    return jsonify(result)
