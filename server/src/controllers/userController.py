from flask import jsonify, request
from src.utils.supabase_client import supabase

def get_user_profile(user_id):
    """
    Fetch user profile data from Supabase.
    
    Args:
        user_id (str): The ID of the user.
    
    Returns:
        dict: A dictionary containing the user's profile data.
    """
    try:
        response = supabase.table('profiles').select('*').eq('user_id', user_id).execute()
        if response.data:
            return jsonify(response.data[0]), 200
        else:
            return jsonify({"error": "User profile not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_user_profile():
    """
    Update user profile data in Supabase.
    
    Returns:
        dict: A dictionary containing the updated user profile data.
    """
    try:
        user_id = request.json.get('user_id')
        update_data = request.json.get('profile_data')
        
        response = supabase.table('profiles').update(update_data).eq('user_id', user_id).execute()
        
        if response.data:
            return jsonify(response.data[0]), 200
        else:
            return jsonify({"error": "Failed to update profile"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_user_account(user_id):
    """
    Delete a user account from Supabase.
    
    Args:
        user_id (str): The ID of the user to be deleted.
    
    Returns:
        dict: A dictionary containing the deletion status.
    """
    try:
        # Delete user profile
        supabase.table('profiles').delete().eq('user_id', user_id).execute()
        
        # Delete user authentication data (this might require admin rights)
        supabase.auth.admin.delete_user(user_id)
        
        return jsonify({"status": "success", "message": "User account deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

async def get_all_users():
    users = await User.all()
    return [user.to_dict() for user in users]