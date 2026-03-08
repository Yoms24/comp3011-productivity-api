# COMP3011 Productivity API

A Django-based REST-style API for tracking habits and simple productivity data.

## Features
- Create a habit
- View all habits
- View one habit by ID
- Update a habit
- Delete a habit
- View a simple habit summary
- JSON responses
- Basic validation and error handling

## Endpoints

### Get all habits
`GET /api/habits/`

### Get one habit
`GET /api/habits/<id>/`

### Create a habit
`POST /api/habits/create/`

Example JSON body:

    {
      "name": "Read Quran",
      "description": "Read 2 pages after Fajr",
      "frequency": "Daily"
    }

### Update a habit
`PUT /api/habits/<id>/update/`

Example JSON body:

    {
      "name": "Drink More Water",
      "description": "Drink 2.5 litres daily",
      "frequency": "Daily"
    }

### Delete a habit
`DELETE /api/habits/<id>/delete/`

### Habit summary
`GET /api/habits/summary/`

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

## Running the project locally
1. Clone the repository
2. Install Django:
   `pip install django`
3. Run migrations:
   `python manage.py migrate`
4. Start the server:
   `python manage.py runserver`

## Notes
This project was developed incrementally with Git version control and tested using browser requests and Postman.