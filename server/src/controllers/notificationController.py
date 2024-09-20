from flask import jsonify, request
from src.utils.supabase_client import supabase

def get_notifications(user_id):
    """
    Fetch notifications for a user from Supabase.
    
    Args:
        user_id (str): The ID of the user.
    
    Returns:
        dict: A dictionary containing the user's notifications.
    """
    try:
        response = supabase.table('notifications').select('*').eq('user_id', user_id).order('created_at', desc=True).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def mark_notification_as_read():
    """
    Mark a notification as read in Supabase.
    
    Returns:
        dict: A dictionary containing the updated notification data.
    """
    try:
        notification_id = request.json.get('notification_id')
        
        response = supabase.table('notifications').update({'is_read': True}).eq('id', notification_id).execute()
        
        if response.data:
            return jsonify(response.data[0]), 200
        else:
            return jsonify({"error": "Failed to update notification"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_notification(user_id, message, notification_type):
    """
    Create a new notification for a user in Supabase.
    
    Args:
        user_id (str): The ID of the user.
        message (str): The notification message.
        notification_type (str): The type of notification.
    
    Returns:
        dict: A dictionary containing the created notification data.
    """
    try:
        notification_data = {
            'user_id': user_id,
            'message': message,
            'type': notification_type,
            'is_read': False
        }
        
        response = supabase.table('notifications').insert(notification_data).execute()
        
        if response.data:
            return jsonify(response.data[0]), 201
        else:
            return jsonify({"error": "Failed to create notification"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500