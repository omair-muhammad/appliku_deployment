# Triive-ai Django Project Setup Guide

## Prerequisites

Before you begin, ensure you have the following installed:
- Python (version 3.8 or higher)
- pip (Python package installer)

You can download Python from [python.org](https://www.python.org/downloads/).


## Step 1: Create a PostgreSQL Database and User

1. Open the PostgreSQL command line or a PostgreSQL GUI tool (like **pgAdmin**).
2. Run the following commands to create a database and a user with the necessary privileges:

   ```sql
   CREATE DATABASE triive_ai_db;
   CREATE USER triive_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE triive_ai_db TO triive_user;
 
## 2. Create and Activate a Virtual Environment
 
Creating a virtual environment (`venv`) is essential for managing project dependencies separately from the global Python environment.
 
### Step 1: Create the Virtual Environment
 
In your project directory, open a terminal and run:
 
```
python3 -m venv venv
```
 
This command creates a `venv` directory with the necessary environment files.
 
### Step 3: Activate the Virtual Environment
 
- **On macOS/Linux:**
 
  ```bash
  source venv/bin/activate
  ```
 
- **On Windows:**
 
  ```bash
  .\venv\Scripts\activate
  ```
 
After activation, you should see `(venv)` in your terminal prompt, indicating that the virtual environment is active.
 
## 4. Install Django and Project Dependencies
 
With the virtual environment activated, install Django and any other dependencies:
 
```
pip install django
```
 
To install other dependencies listed in a `requirements.txt` file (if present), run:
 
```
pip install -r requirements.txt
```
 
# Set Up Environment Variables for development 
Look for .env.example file in the project root with the following variables to configure Django and your database and other variables as specified.
```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=triive_ai_db
DB_USER=triive_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```


## 5. Run the Django Project
 
After installing Django and the necessary packages, you can run the Django development server.
 
### Step 1: Navigate to the Project Directory
 
Make sure you're in the directory containing `manage.py`:
 
```
cd path/to/your/project
```
 
### Step 2: Run the Development Server
 
Start the Django development server by running:
 
```bash
python manage.py runserver
```
 
You should see output similar to:
 
```plaintext
Starting development server at http://127.0.0.1:8000/
```
 
Open your browser and go to `http://127.0.0.1:8000/` to view the running project.
 
## 4. Deactivate the Virtual Environment
 
When you're done working, you can deactivate the virtual environment with:
 
```bash
deactivate
```
 
## Additional Notes
 
- **Requirements File**: To generate a `requirements.txt` file with the installed packages, run:
 
  ```
  pip freeze > requirements.txt
  ```
 
- **Migrations**: If this is the first time you're setting up the project, you may need to run migrations:
 
  ```bash
  python manage.py migrate
  ```
## 5. API Documentation with DRF Spectacular

  This project uses DRF Spectacular to generate and serve API documentation in both Swagger and ReDoc formats. You can access detailed information about each endpoint, including request and response formats, parameters, and authentication requirements

  Accessing the API Documentation
    
    ```
      python manage.py runserver
    ```

  Explore API Documentation:

  Swagger UI: Provides an interactive interface to test API endpoints directly in the browser.

    ```
      http://127.0.0.1:8000/api/docs/swagger/
    ```
  ReDoc: Offers a streamlined, document-like view of the API endpoints.
  ```
    http://127.0.0.1:8000/api/docs/redoc/
  ```

  View the OpenAPI Schema:

  The raw OpenAPI schema in JSON format is available at:

  ```
    http://127.0.0.1:8000/api/schema/
  ```