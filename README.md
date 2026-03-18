# AI Content Extractor API

A **production-style Python backend** built with FastAPI, Celery, Redis, and PostgreSQL. Users can submit URLs or text and get extracted content asynchronously.

## Features

- JWT Authentication (Signup/Login)
- Async content extraction using Celery
- Redis caching
- PostgreSQL database integration
- Dockerized setup
- API documentation via FastAPI Swagger
- Background job status tracking

## Tech Stack

- Python 3.11
- FastAPI
- Celery + Redis
- PostgreSQL
- Docker & Docker Compose
- SQLAlchemy ORM
- Pytest (for testing)

## Run Locally

1. Clone repo:
```bash
git clone <repo_url>
cd ai-content-extractor