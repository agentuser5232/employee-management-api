# Employee Management API

## Overview

Employee Management API is a RESTful service built with FastAPI and SQLAlchemy. It demonstrates clean project organization, database connectivity, and basic CRUD operations for managing employee records.

## Features

* REST API built with FastAPI
* SQLAlchemy ORM integration
* SQLite database by default
* Environment-based configuration
* Create employee records
* Retrieve employee records
* Modular project structure

## Technology Stack

* Python 3.11+
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

## Installation

Clone the repository.

```bash
git clone https://github.com/agentuser5232/employee-management-api.git
cd employee-management-api
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux or macOS:

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server.

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Create Employee

```
POST /employees
```

Example request:

```json
{
  "name": "Alice Johnson",
  "department": "Engineering",
  "email": "alice@example.com"
}
```

### List Employees

```
GET /employees
```

## Future Enhancements

* Update and delete operations
* PostgreSQL support
* Authentication and authorization
* Logging
* Unit and integration tests
* Docker support
* CI/CD pipeline
