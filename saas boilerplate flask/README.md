# Project Name

This project consists of a Python Flask backend server and a React frontend client.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Building and Running without Docker](#building-and-running-without-docker)
   - [Setting up the Server](#setting-up-the-server)
   - [Setting up the Client](#setting-up-the-client)
3. [Building and Running with Docker](#building-and-running-with-docker)
4. [Accessing the Application](#accessing-the-application)
5. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following installed:

- For non-Docker setup:
  - Python 3.9 or higher
  - Node.js 14 or higher
  - npm (usually comes with Node.js)
- For Docker setup:
  - Docker
  - Docker Compose

## Building and Running without Docker

### Setting up the Server

1. Open a terminal and navigate to the server directory:
   ```
   cd server
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the server:
   ```
   python src/main.py
   ```

The server should now be running on `http://localhost:5000`.

### Setting up the Client

1. Open a new terminal window and navigate to the client directory:
   ```
   cd client
   ```

2. Install the required dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

The client should now be running on `http://localhost:3000`.

## Building and Running with Docker

1. Ensure Docker and Docker Compose are installed on your system.

2. Open a terminal and navigate to the project root directory (where the `docker-compose.yml` file is located).

3. Build and start the containers:
   ```
   docker-compose up --build
   ```

   This command will build the Docker images for both the server and client, and then start the containers.

4. To stop the containers, use:
   ```
   docker-compose down
   ```

## Accessing the Application

- If running without Docker:
  - The server API will be accessible at `http://localhost:5000`
  - The client application will be accessible at `http://localhost:3000`

- If running with Docker:
  - The server API will be accessible at `http://localhost:5000`
  - The client application will be accessible at `http://localhost:80` or simply `http://localhost`

## Admin Dashboard

This project includes an admin dashboard that provides an overview of all users and billing information. To access the admin dashboard:

1. Log in with an admin account
2. Navigate to `/admin` in your browser

The admin dashboard displays:
- A list of all users and their roles
- Billing information for all users

Only users with the 'admin' role can access this dashboard.

## Troubleshooting

1. **Port conflicts**: If you encounter port conflicts, ensure no other applications are using ports 5000 (for the server) or 80 (for the client when using Docker). You can modify the port mappings in the `docker-compose.yml` file if needed.

2. **Environment variables**: If the client can't connect to the server, check that the `REACT_APP_API_BASE_URL` environment variable is set correctly. In the Docker setup, this is done in the client's Dockerfile.

3. **CORS issues**: If you encounter CORS (Cross-Origin Resource Sharing) issues, ensure that your server is configured to allow requests from the client's origin.

4. **Docker network issues**: If the client container can't reach the server container, ensure that both containers are on the same Docker network (which should be the case if you're using the provided `docker-compose.yml`).

5. **Build errors**: If you encounter build errors, make sure all required dependencies are installed and that you're using compatible versions of Python and Node.js.

If you continue to experience issues, please check the console output for error messages and refer to the project's issue tracker or support channels for further assistance.