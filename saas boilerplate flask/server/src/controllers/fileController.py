from flask import jsonify, request
from src.utils.supabase_client import supabase
import uuid

def upload_file():
    """
    Upload a file to Supabase storage.
    
    Returns:
        dict: A dictionary containing the uploaded file details.
    """
    try:
        file = request.files['file']
        user_id = request.form.get('user_id')
        
        # Generate a unique filename
        filename = f"{uuid.uuid4()}_{file.filename}"
        
        # Upload file to Supabase storage
        response = supabase.storage.from_('user_files').upload(filename, file)
        
        if response.get('error'):
            return jsonify({"error": response['error']}), 400
        
        # Get public URL for the file
        file_url = supabase.storage.from_('user_files').get_public_url(filename)
        
        # Save file metadata to the database
        file_data = {
            'user_id': user_id,
            'file_name': filename,
            'file_url': file_url
        }
        db_response = supabase.table('files').insert(file_data).execute()
        
        return jsonify(db_response.data[0]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_user_files(user_id):
    """
    Fetch all files for a user from Supabase.
    
    Args:
        user_id (str): The ID of the user.
    
    Returns:
        dict: A dictionary containing the user's files.
    """
    try:
        response = supabase.table('files').select('*').eq('user_id', user_id).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_file():
    """
    Delete a file from Supabase storage and database.
    
    Returns:
        dict: A dictionary containing the deletion status.
    """
    try:
        file_id = request.json.get('file_id')
        
        # Get file details from the database
        file_response = supabase.table('files').select('*').eq('id', file_id).execute()
        
        if not file_response.data:
            return jsonify({"error": "File not found"}), 404
        
        file_name = file_response.data[0]['file_name']
        
        # Delete file from Supabase storage
        supabase.storage.from_('user_files').remove(file_name)
        
        # Delete file metadata from the database
        supabase.table('files').delete().eq('id', file_id).execute()
        
        return jsonify({"status": "success", "message": "File deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500