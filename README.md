# Django Medical System API

This is a backend application built using Django and Django REST Framework (DRF) to manage patient and doctor data, with JWT-based authentication. It supports features like patient management, doctor management, and patient-doctor mapping.

## Features

- **Authentication APIs**: Register, Login, and JWT-based authentication.
- **Patient Management**: Add, retrieve, update, and delete patient records.
- **Doctor Management**: Add, retrieve, update, and delete doctor records.
- **Patient-Doctor Mapping**: Assign doctors to patients and manage their relationships.

## Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: JWT (using djangorestframework-simplejwt)

## API Endpoints

### Authentication APIs

- **POST** `/api/auth/register/`: Register a new user.
- **POST** `/api/auth/login/`: Login a user and get a JWT token.

### Patient Management APIs

- **POST** `/api/patients/`: Add a new patient (Authenticated users only).
- **GET** `/api/patients/`: Retrieve all patients created by the authenticated user.
- **GET** `/api/patients/<id>/`: Get details of a specific patient.
- **PUT** `/api/patients/<id>/`: Update patient details.
- **DELETE** `/api/patients/<id>/`: Delete a patient record.

### Doctor Management APIs

- **POST** `/api/doctors/`: Add a new doctor (Authenticated users only).
- **GET** `/api/doctors/`: Retrieve all doctors.
- **GET** `/api/doctors/<id>/`: Get details of a specific doctor.
- **PUT** `/api/doctors/<id>/`: Update doctor details.
- **DELETE** `/api/doctors/<id>/`: Delete a doctor record.

### Patient-Doctor Mapping APIs

- **POST** `/api/mappings/`: Assign a doctor to a patient.
- **GET** `/api/mappings/<patient_id>/`: Get all doctors assigned to a specific patient.
- **DELETE** `/api/mappings/delete/<id>/`: Remove a doctor from a patient.

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL
- `pip` (Python package manager)

### Steps to Run the Project Locally

1. **Clone the Repository**

git clone https://github.com/shibinshibii/health-care-backend.git

cd backend

2. **Create a Virtual Environment**


python -m venv venv

3.  **Activate the Virtual Environment**

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

4. **Install dependencies**
pip install -r requirements.txt

5. **Create a .env file in the root directory of the project**

Add the following database credentials to a .env file or use your own database:

DB_NAME=hcbackend 
DB_USER=hcuser        
DB_PASSWORD=123  
DB_HOST=localhost        
DB_PORT=5432 

6. **Run migrations to set up the database and then run the server**

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

7. **Test the API endpoints using Postman**

8. **For authentication, provide the JWT token as a Bearer token in the headers:**

json:-

{
    "Authorization": "Bearer <JWT_token>"
}