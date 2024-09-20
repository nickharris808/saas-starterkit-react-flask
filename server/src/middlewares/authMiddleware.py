from functools import wraps
from flask import request, jsonify
from src.utils.supabase_client import supabase

def token_required(f):
    """
    Decorator to check if the request has a valid JWT token.
    
    Args:
        f (function): The function to be decorated.
    
    Returns:
        function: The decorated function.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # Check if the token is in the header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        
        try:
            # Verify the token using Supabase
            user = supabase.auth.get_user(token)
            
            # Add the user to the request context
            request.user = user
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401
        
        return f(*args, **kwargs)
    
    return decorated

def admin_required(f):
    """
    Decorator to check if the user has admin privileges.
    
    Args:
        f (function): The function to be decorated.
    
    Returns:
        function: The decorated function.
    """
    @wraps(f)
    @token_required
    def decorated(*args, **kwargs):
        # Check if the user has admin role
        if request.user.user_metadata.get('role') != 'admin':
            return jsonify({'message': 'Admin privilege required!'}), 403
        
        return f(*args, **kwargs)
    
    return decorated