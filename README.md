# Saas Boilerplate

This project consists of a Python Flask backend server and a React frontend client, integrated with Supabase for authentication, PostgreSQL database management, and real-time functionality, with Stripe for subscription billing and SendGrid for email notifications.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Building and Running without Docker](#building-and-running-without-docker)
   - [Setting up the Server](#setting-up-the-server)
   - [Setting up the Client](#setting-up-the-client)
3. [Building and Running with Docker](#building-and-running-with-docker)
4. [Accessing the Application](#accessing-the-application)
5. [Codebase Overview](#codebase-overview)
   - [Client (React)](#client-react)
   - [Server (Flask)](#server-flask)
   - [Third-Party Integrations](#third-party-integrations)
   - [Database Schema](#database-schema)
6. [Admin Dashboard](#admin-dashboard)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following installed:

- **For non-Docker setup**:
  - Python 3.9 or higher
  - Node.js 14 or higher
  - npm (usually comes with Node.js)
- **For Docker setup**:
  - Docker
  - Docker Compose

---

## Building and Running without Docker

### Setting up the Server

1. Open a terminal and navigate to the server directory:
   ```bash
   cd server
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the server:
   ```bash
   python src/main.py
   ```

The server should now be running on `http://localhost:5000`.

### Setting up the Client

1. Open a new terminal window and navigate to the client directory:
   ```bash
   cd client
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The client should now be running on `http://localhost:3000`.

---

## Building and Running with Docker

1. Ensure Docker and Docker Compose are installed on your system.

2. Open a terminal and navigate to the project root directory (where the `docker-compose.yml` file is located).

3. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images for both the server and client, and then start the containers.

4. To stop the containers, use:
   ```bash
   docker-compose down
   ```

---

## Accessing the Application

- **Without Docker**:
  - The server API will be accessible at `http://localhost:5000`
  - The client application will be accessible at `http://localhost:3000`

- **With Docker**:
  - The server API will be accessible at `http://localhost:5000`
  - The client application will be accessible at `http://localhost:80` or simply `http://localhost`

---

## Codebase Overview

### Client (React)

The client-side of the application is built with React and styled using Tailwind CSS for a responsive design. Key features include user authentication, dashboards, file management, and notifications, all interacting with the Flask backend and Supabase API.

**Directory Structure**:
- **`/client/src`**: 
  - **`index.jsx`**: The entry point of the React app.
  - **`App.jsx`**: Sets up routing for different pages (e.g., login, signup, dashboard).
  - **`/pages`**: Contains the main page components (e.g., `LoginPage`, `SignUpPage`, `Dashboard`).
  - **`/components`**: Reusable UI components (e.g., buttons, forms, tables).
  - **`/utils`**: Utility functions, like API calls (e.g., Supabase client configuration) and helper methods.
  - **`/hooks`**: Custom React hooks, such as `useAuth` to manage authentication.
  - **`/styles`**: Tailwind CSS configurations and global styles.

**Key Features**:
- **Routing**: Managed by `react-router-dom` to handle navigation between pages.
- **State Management**: Optionally using `Context API` for global states like authentication.
- **API Integration**: Uses the Supabase client and Flask API to fetch and update data (e.g., user profile, subscriptions).
- **Responsive Design**: Tailwind CSS ensures the app is mobile-friendly.

---

### Server (Flask)

The backend is built with Flask, responsible for serving APIs, processing data, and handling third-party integrations (e.g., Supabase for authentication, Stripe for billing, SendGrid for emails).

**Directory Structure**:
- **`/server`**: 
  - **`app.py`**: The entry point of the Flask application. Initializes routes, middlewares, and services.
  - **`/src`**: Contains the core server logic.
    - **`/controllers`**: The core business logic for handling user requests (e.g., `userController.py`, `billingController.py`).
    - **`/routes`**: Defines the API routes for different features (e.g., `userRoutes.py`, `billingRoutes.py`).
    - **`/middlewares`**: Handles security, authentication, and rate limiting (`authMiddleware.py`, `rateLimiter.py`).
    - **`/services`**: Contains third-party integrations (e.g., `paymentService.py` for Stripe, `emailService.py` for SendGrid).
    - **`/utils`**: Utility files for configuration and logging (`config.py`, `logger.py`).

**Key Features**:
- **API Endpoints**: The Flask server exposes REST API endpoints for various functionalities:
  - **User Authentication**: Supabase-managed authentication (e.g., `/api/auth/signup`, `/api/auth/login`).
  - **Billing**: Manages Stripe payments and subscriptions (e.g., `/api/billing/create-subscription`).
  - **File Storage**: Interacts with Supabase's storage API for file uploads and management (e.g., `/api/files/upload`).
  - **Notifications**: Real-time notifications using Supabase (e.g., `/api/notifications`).
- **Middlewares**: Includes error handling, input validation, and security checks (e.g., `authMiddleware.py` for JWT validation).
- **Third-party Integrations**: Uses the Supabase API for authentication and database, Stripe for billing, and SendGrid for email notifications.

---

### Third-Party Integrations

1. **Supabase**: 
   - Handles user authentication, database management (PostgreSQL), real-time functionality, and file storage.
   - Replaces traditional Flask-JWT and SQLAlchemy setups, simplifying the backend.
   
2. **Stripe**: 
   - Manages subscription billing, including creating, updating, and canceling subscriptions.
   - Webhooks are implemented to listen for Stripe events such as payment success or failure.

3. **SendGrid**: 
   - Sends transactional emails such as account verification, password resets, and billing updates.

---

### Database Schema

Supabase manages the PostgreSQL database. The following tables are used:

- **`users`**: Manages user authentication data.
  - `id`, `email`, `password_hash`, `role`, `created_at`, `updated_at`.
  
- **`profiles`**: Stores additional user information.
  - `user_id`, `avatar_url`, `language`, `timezone`, `created_at`, `updated_at`.
  
- **`subscriptions`**: Tracks user subscription data (related to Stripe).
  - `id`, `user_id`, `stripe_customer_id`, `stripe_subscription_id`, `plan`, `status`.

- **`notifications`**: Stores in-app notifications.
  - `id`, `user_id`, `message`, `is_read`, `created_at`.

- **`files`**: Manages file uploads and metadata.
  - `id`, `user_id`, `file_name`, `file_url`, `created_at`.

---

## Admin Dashboard

This project includes an admin dashboard that provides an overview of all users and billing information. To access the admin dashboard:

1. Log in with an admin account.
2. Navigate to `/admin` in your browser.

**Admin Features**:
- A list of all users and their roles.
- Billing information for all users, fetched via Stripe.
- Only accessible to users with the 'admin' role, enforced by role-based access control via Supabase.

---

## Troubleshooting

1. **Port conflicts**: If you encounter port conflicts, ensure no other applications are using ports 5000 (server) or 80/3000 (client). You can modify the port mappings in `docker-compose.yml` if needed.
   
2. **Environment variables**: Ensure that environment variables (e.g., `SUPABASE_URL`, `STRIPE_API_KEY`) are correctly set in `.env` files

 for both the client and server.
   
3. **CORS issues**: If you encounter CORS issues, ensure your Flask server has the correct `CORS` configuration allowing requests from the frontend origin.
   
4. **Docker network issues**: Ensure that both the frontend and backend services are on the same Docker network by using `docker-compose.yml`.

5. **Build errors**: If you encounter build errors in Docker, check for missing dependencies or version mismatches in `requirements.txt` (Flask) or `package.json` (React).

For further assistance, consult the project’s issue tracker or community support.

--- 

This updated README offers not only a clear guide for building and running the project but also gives a comprehensive overview of the codebase, making it easier for developers to understand the project's structure and navigate the code efficiently.


