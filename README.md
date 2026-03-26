# Task Manager API

A production-ready task management backend built with FastAPI, SQLAlchemy, and JWT authentication.

## Features

- User registration and login
- JWT-based authentication
- Create, update, and delete tasks
- Task filtering by completion status and priority
- Search functionality
- Pagination with skip and limit
- Task ownership with user-specific data
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

