# Task Manager API

A production-ready task management backend built with FastAPI, SQLAlchemy, and JWT authentication.

## Features

- User registration and login
- JWT-based authentication
- Create, update, and delete tasks
- Task filtering (completed status and priority)
- Search functionality
- Pagination (skip, limit)
- Task ownership (user-specific data)
- Priority and due date support

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Uvicorn

## Project Structure

```text
task-manager-api/
│
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── users.py
│       └── tasks.py
│
├── requirements.txt
├── README.md
└── .gitignore

## How to Run
git clone https://github.com/ruchithajannu/Task-Manager-API.git
cd Task-Manager-API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

##API Docs

Visit:

http://127.0.0.1:8000/docs

Author

Ruchitha Jannu
