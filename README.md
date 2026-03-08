# COMP3011 Productivity API

A Django-based REST-style API for tracking habits, recording completion logs, and providing simple productivity analytics.

## Features
- Create a habit
- View all habits
- View one habit by ID
- Update a habit
- Delete a habit
- View a simple habit summary
- Create a completion log for a habit
- View all logs for a habit
- View a habit streak
- JSON responses
- Validation and error handling
- Automated Django tests

## Data Models

### Habit
- `id`
- `name`
- `description`
- `frequency`
- `created_at`

### HabitLog
- `id`
- `habit`
- `completed_on`
- `notes`
- `created_at`

## Endpoints

### Get all habits
`GET /api/habits/`

### Get one habit
`GET /api/habits/<id>/`

### Create a habit
`POST /api/habits/create/`

Example JSON body:

    {
      "name": "Walk Daily",
      "description": "Walk for 20 minutes",
      "frequency": "Daily"
    }

### Update a habit
`PUT /api/habits/<id>/update/`

Example JSON body:

    {
      "name": "Drink More Water",
      "description": "Drink 3 litres daily",
      "frequency": "Daily"
    }

### Delete a habit
`DELETE /api/habits/<id>/delete/`

### Habit summary
`GET /api/habits/summary/`

### Create a habit log
`POST /api/habits/<id>/logs/create/`

Example JSON body:

    {
      "completed_on": "2026-03-08",
      "notes": "Completed after Fajr"
    }

### Get habit logs
`GET /api/habits/<id>/logs/`

### Get habit streak
`GET /api/habits/<id>/streak/`

## Tech stack
- Python
- Django
- SQLite
- Git
- GitHub
- Postman

## Status codes used
- 200 OK
- 201 Created
- 400 Bad Request
- 404 Not Found
- 405 Method Not Allowed

## Testing
Automated tests were written using Django's testing framework to verify:
- habit CRUD functionality
- validation behaviour
- summary endpoint
- habit log creation
- habit log listing
- streak endpoint

## Running the project locally
1. Clone the repository
2. Install Django:
   `pip install django`
3. Run migrations:
   `python manage.py migrate`
4. Start the server:
   `python manage.py runserver`

## Notes
This project was developed incrementally with Git version control and tested using browser requests, Postman, and Django automated tests.