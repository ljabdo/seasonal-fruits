# Seasonal Fruits Web Application

## Project Goal

Build a full-stack web application that displays which fruits are currently in season.

The project is intended as a learning exercise covering:

- Frontend development
- Backend APIs
- Docker containers
- CI/CD pipelines
- Cloud deployment
- Infrastructure as Code

---

# Functional Requirements

## Homepage

The application homepage shall display:

- Current season
- List of fruits currently in season
- Simple responsive design
- Loading state
- Error state

Example:

Current Season: Summer

Fruits:
- Peach
- Watermelon
- Cherry

---

# Backend Requirements

## Technology

- Python 3.12
- FastAPI
- Uvicorn

## API Endpoint

GET /fruits

Response:

```json
{
  "season": "summer",
  "fruits": [
    "Peach",
    "Watermelon",
    "Cherry"
  ]
}
```

## Season Logic

Winter:
- December
- January
- February

Spring:
- March
- April
- May

Summer:
- June
- July
- August

Fall:
- September
- October
- November

## Backend Requirements

- CORS enabled
- JSON responses
- Containerized with Docker
- Environment variable support

---

# Frontend Requirements

## Technology

- Next.js
- React
- TypeScript

## Features

- Fetch data from backend API
- Display season
- Display fruit list
- Loading indicator
- Error handling
- Responsive layout

## Configuration

API URL shall be supplied using:

NEXT_PUBLIC_API_URL

---

# Docker Requirements

## Backend

- Python 3.12 image
- Expose port 8000

## Frontend

- Node image
- Expose port 3000

## Local Development

docker-compose shall start:

- frontend
- backend

---

# Deployment Requirements

## Frontend

Platform:
- Vercel

Requirements:
- Automatic deployment from GitHub
- HTTPS enabled

## Backend

Container deployment platform:
- Render
- Fly.io
- Railway

Requirements:
- Public API endpoint
- HTTPS enabled

---

# CI/CD Requirements

GitHub Actions shall:

- Run frontend build
- Run backend validation
- Build Docker images
- Execute on push to main

---

# Terraform Requirements

Terraform shall manage:

- Docker containers
- Environment variables
- Future cloud infrastructure

Directory:

terraform/

Commands:

terraform init
terraform plan
terraform apply

---

# Repository Structure

seasonal-fruits/

frontend/
backend/
terraform/
.github/
PROJECT_SPEC.md
README.md

---

# Future Enhancements

- Database integration
- User accounts
- Favorite fruits
- Seasonal notifications
- Admin panel
- Kubernetes deployment
- Monitoring and logging

---

# Definition of Done

- Frontend deployed publicly
- Backend deployed publicly
- Containers built successfully
- GitHub Actions passing
- Terraform configuration operational
- Application accessible via HTTPS
