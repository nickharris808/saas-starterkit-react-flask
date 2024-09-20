from flask import jsonify

def register_error_handlers(app):
    """
    Register error handlers for the Flask app.
    
    Args:
        app (Flask): The Flask application instance.
    """
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "error": "Bad Request",
            "message": str(error)
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "error": "Unauthorized",
            "message": "Authentication is required to access this resource."
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "error": "Forbidden",
            "message": "You don't have the permission to access this resource."
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Not Found",
            "message": "The requested resource could not be found."
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "error": "Internal Server Error",
            "message": "An unexpected error occurred on the server."
        }), 500

    @app.errorhandler(Exception)
    def handle_exception(e):
        # Log the error here (you can use your logging setup)
        app.logger.error(f"Unhandled exception: {str(e)}")
        
        return jsonify({
            "error": "Internal Server Error",
            "message": "An unexpected error occurred on the server."
        }), 500