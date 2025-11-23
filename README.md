🔑 Storefront Backend API | Token-Based Authentication

Hello! 👋 I'm [Your Name Here].

Welcome to my portfolio showcase of a modern, API-driven backend application. This project demonstrates competency across the full backend development lifecycle, focusing on containerization, security, and stateless API design.

The entire project is ready to run locally via Docker Compose, requiring only a single command after cloning.

🛠️ Core Competencies & Technologies

This project utilizes industry-standard tools and patterns for building production-grade web services.

Area

Technologies & Skills

Competence Demonstrated

Backend Framework

Django 5.2 (Python), Django REST Framework

Clean code structure, ORM usage, and handling complex request/response cycles.

Authentication

JWT (SimpleJWT)

Implementing stateless, scalable security essential for modern mobile/JS frontends.

Database

PostgreSQL, Django ORM

Connecting to and managing a robust, external database.

Deployment

Docker, Docker Compose

Containerizing the application and database for portable development and deployment.

Configuration

Pipenv, python-dotenv

Managing dependencies and securing sensitive data (passwords, secrets) using environment variables.

🚀 Featured End-to-End Project

Storefront Product Catalog API

This project delivers a secure, read-only API endpoint for accessing product information.

Challenge: Create a scalable product listing service where data integrity is maintained in PostgreSQL, but access is restricted to authenticated clients (mobile app, single-page application).

Technical Highlight: The application successfully separates the data model (PostgreSQL) from the access layer (DRF API), enforcing security with a JWT requirement. This demonstrates the ability to build a secure, decoupled service that is ready for a separate frontend team.

Core Endpoints:

Login (Token Exchange): /api/token/

Protected Data: /playground/api/products/ (Returns JSON only upon valid JWT token validation)

Data Management: /admin/ (Secure internal interface)

⚙️ Setup and Installation Guide (1-Minute Docker Setup)

1. Prerequisites

Git

Docker Desktop (must be running)

2. Clone and Configure

# Clone the repository
git clone [https://github.com/Spp77/django-storefront.git](https://github.com/Spp77/django-storefront.git)
cd django-storefront

# Create the .env file with secrets (Required by Docker Compose)
# NOTE: Use 'postgres' for USER/PASSWORD/DB to match Docker defaults
# POSTGRES_DB=postgres
# POSTGRES_USER=postgres
# POSTGRES_PASSWORD=postgres


3. Build, Migrate, and Run

This single sequence of commands builds the containers, creates the database schema, and starts the API.

# 1. Build containers (Installs all Python dependencies via Dockerfile)
docker-compose up --build -d

# 2. Create database tables inside the Docker Postgres container
docker-compose run app python manage.py migrate

# 3. Create a Superuser (Admin) account for testing the API login
docker-compose run app python manage.py createsuperuser


Your API is now running and accessible at http://localhost:8000.

🔑 Testing the Token Authentication

To verify your security, you need an Access Token.

A. Get Token (API Login)

Send a POST request to the endpoint below with your superuser credentials (username/password).

Endpoint: http://localhost:8000/api/token/

B. Access Protected Data

Use the access token received in Step A to make a GET request to the protected endpoint.

Endpoint: http://localhost:8000/playground/api/products/

Header Required: Authorization: Bearer [YOUR_ACCESS_TOKEN_HERE]

Test Case

Expected Result

Status Code

Test 1: No Token Header

Rejected Access

401 Unauthorized

Test 2: Valid Access Token

Product List (JSON Data)

200 OK

License

This project is open-source.
