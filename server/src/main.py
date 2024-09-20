from flask import Flask, jsonify
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.routes import auth, user, billing, admin
from src.middlewares.errorHandler import error_handler
from src.middlewares.authMiddleware import get_current_user

app = FastAPI()

@app.route('/api/data', methods=['GET'])
def get_data():
    # Simulate data retrieval from a database or API
    data = {'message': 'Hello, World!'}
    return jsonify(data)

# Add these new imports
from src.routes import admin

# Add the admin routes
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)