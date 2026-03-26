# Task Manager API

A production-ready task management backend inspired by tools like Jira and Todoist, built with FastAPI.

## Features

- User registration
- JWT-based login authentication
- Protected routes
- User-isolated task access
- Create, read, update, delete tasks
- Mark tasks complete
- Task priority support
- Due dates
- Filtering by completion status
- Filtering by priority
- Search by title
- Pagination with skip and limit

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Uvicorn

## Project Structure

```bash
task-manager-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       ├── users.py
│       └── tasks.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── test.db