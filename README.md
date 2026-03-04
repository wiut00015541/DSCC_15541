# Project Description

A Django web application for task management was created for the DSCC module.
It allows users to create, update, delete and differenciate tasks using categories and tags.
The application is containerized using Docker and deployed on Google Cloud VPS with HTTPS enabled.

# URL:
https://dscc15541.duckdns.org

# Features
- User registration, login and logout
- Create, update and delete tasks
- Categories for tasks
- Tags system for the priority
- Personal tasks linked to user account
- Django admin panel
- PostgreSQL database
- HTTPS with SSL certificate
- CI/CD pipeline with GitHub Actions

# Database Structure

The application includes several models:
- User (one-to-many relationship with Task)
- Task (one-to-many relationship with Category\ one-to-many relationship with User)
- Category (one-to-many relationship with Task)
- Tag (many-to-many relationship with Task)

# Technologies Used

Backend:
- Python 3.11
- Django 5
- PostgreSQL

Deployment and Infrastructure:
- Docker
- Docker Compose
- Gunicorn
- Nginx
- Let's Encrypt
- DuckDNS
- Google Cloud VPS

CI/CD:
- GitHub Actions
- Docker Hub
- SSH deployment

Testing:
- pytest
- pytest-django
- flake8

# Local Setup Instructions

1. Clone the repository:

git clone https://github.com/wiut00015541/DSCC_15541.git
cd DSCC_15541

2. Create virtual environment:

python -m venv .venv

3. Activate it:

.venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Create .env file in project root:

POSTGRES_DB=mydb
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword

DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

<img width="1057" height="639" alt="image" src="https://github.com/user-attachments/assets/49cb90af-ffaf-4d27-9dfb-f84535837620" />


5. Run with Docker:

docker-compose up --build

The app will be available at:

http://localhost:8000

# Deployment Instructions

The application is deployed on a Google Cloud VM.

Deployment architecture includes:
- Docker containers
- Gunicorn as WSGI server
- Nginx as reverse proxy
- PostgreSQL as database
- SSL certificate from Let's Encrypt
- DuckDNS domain
- Firewall configuration

Deployment process:
1. Code is pushed to the main branch
2. GitHub Actions workflow runs automatically
3. flake8 checks code style
4. pytest runs automated tests
5. Docker image is built
6. Image is pushed to Docker Hub
7. Server pulls latest image via SSH
8. Containers are restarted
9. Migrations run automatically


# Environment Variables

The project uses environment variables for configuration:
1. SECRET_KEY – Django secret key
2. ALLOWED_HOSTS – allowed domains and IP addresses
3. DB_NAME – PostgreSQL database name
4. DB_USER – database user
5. DB_PASSWORD – database password
6. DB_HOST – database host
7. DB_PORT – database port
8. POSTGRES_DB – database name inside container
9. POSTGRES_USER – PostgreSQL container user
10. POSTGRES_PASSWORD – PostgreSQL container password


# CI/CD Pipeline

The CI/CD pipeline is implemented using GitHub Actions:
1. Code quality check with flake8
2. Automated testing with pytest
3. Docker image build
4. Docker image tagging (latest)
5. Push to Docker Hub
6. Automatic deployment to server via SSH
7. Database migrations during deployment


# Security Measures

- HTTPS enabled with valid SSL certificate
- DEBUG=False
- SECRET_KEY stored in environment variables
- Database credentials stored in environment variables
- Non-root user inside Docker container
- Firewall rules configured on VPS
- Reverse proxy configuration via Nginx

# Screenshots

Login Page
<img width="1920" height="1200" alt="Screenshot (238)" src="https://github.com/user-attachments/assets/1cabf6b6-d85e-4e4e-8db0-0f9d8c2afb1f" />

Task List Page
<img width="1920" height="1200" alt="Screenshot (237)" src="https://github.com/user-attachments/assets/9a6fc289-0623-482f-a017-c29a26212d5a" />


Admin Panel
<img width="1920" height="1200" alt="Screenshot (239)" src="https://github.com/user-attachments/assets/b55a11ea-9f22-4e76-a0fa-152a1d1bdf60" />


HTTPS Secure Connection
<img width="834" height="471" alt="image" src="https://github.com/user-attachments/assets/299643ea-17ec-4461-95a5-4639f0055a83" />

