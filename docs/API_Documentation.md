# API Documentation

## Project
COMP3011 Productivity API

## API Root Prefix
`http://127.0.0.1:8000/api/`

All endpoints in this project begin with this prefix.

## Overview
This API was built using Django and SQLite. It supports CRUD operations for habits, completion logging, and simple productivity analytics.

---

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

---

## 1. Get All Habits

**Method:** `GET`  
**Endpoint:** `/habits/`

### Description
Returns all habits stored in the database.

### Success Response
**200 OK**

### Example Response
```json
[
  {
    "id": 1,
    "name": "Drink More Water",
    "description": "Drink 3 litres daily",
    "frequency": "Daily",
    "created_at": "2026-03-08T14:15:31.965Z"
  }
]
```

---

## 2. Get One Habit

**Method:** `GET`  
**Endpoint:** `/habits/<id>/`

### Description
Returns a single habit by ID.

### Success Response
**200 OK**

### Error Response
**404 Not Found**
```json
{
  "error": "Habit not found"
}
```

---

## 3. Create Habit

**Method:** `POST`  
**Endpoint:** `/habits/create/`

### Description
Creates a new habit in the database.

### Required Fields
- `name`
- `frequency`

### Optional Fields
- `description`

### Allowed Frequency Values
- `Daily`
- `Weekly`

### Example Request Body
```json
{
  "name": "Walk Daily",
  "description": "Walk for 20 minutes",
  "frequency": "Daily"
}
```

### Success Response
**201 Created**

### Error Responses
**400 Bad Request**
```json
{
  "error": "Name and frequency are required"
}
```

```json
{
  "error": "Frequency must be either 'Daily' or 'Weekly'"
}
```

**405 Method Not Allowed**
```json
{
  "error": "Only POST method is allowed"
}
```

---

## 4. Update Habit

**Method:** `PUT`  
**Endpoint:** `/habits/<id>/update/`

### Description
Updates an existing habit by ID.

### Required Fields
- `name`
- `frequency`

### Optional Fields
- `description`

### Allowed Frequency Values
- `Daily`
- `Weekly`

### Example Request Body
```json
{
  "name": "Drink More Water",
  "description": "Drink 3 litres daily",
  "frequency": "Daily"
}
```

### Success Response
**200 OK**

### Error Responses
**400 Bad Request**
```json
{
  "error": "Name and frequency are required"
}
```

```json
{
  "error": "Frequency must be either 'Daily' or 'Weekly'"
}
```

**404 Not Found**
```json
{
  "error": "Habit not found"
}
```

**405 Method Not Allowed**
```json
{
  "error": "Only PUT method is allowed"
}
```

---

## 5. Delete Habit

**Method:** `DELETE`  
**Endpoint:** `/habits/<id>/delete/`

### Description
Deletes a habit by ID.

### Success Response
**200 OK**
```json
{
  "message": "Habit deleted successfully"
}
```

### Error Responses
**404 Not Found**
```json
{
  "error": "Habit not found"
}
```

**405 Method Not Allowed**
```json
{
  "error": "Only DELETE method is allowed"
}
```

---

## 6. Habit Summary

**Method:** `GET`  
**Endpoint:** `/habits/summary/`

### Description
Returns a simple summary of habit data.

### Success Response
**200 OK**

### Example Response
```json
{
  "total_habits": 1,
  "daily_habits": 1,
  "weekly_habits": 0
}
```

---

## 7. Create Habit Log

**Method:** `POST`  
**Endpoint:** `/habits/<id>/logs/create/`

### Description
Creates a completion log for a specific habit.

### Required Fields
- `completed_on`

### Optional Fields
- `notes`

### Date Format
- `YYYY-MM-DD`

### Example Request Body
```json
{
  "completed_on": "2026-03-08",
  "notes": "Completed after Fajr"
}
```

### Success Response
**201 Created**

### Error Responses
**400 Bad Request**
```json
{
  "error": "Invalid JSON body"
}
```

```json
{
  "error": "completed_on must be a valid date in YYYY-MM-DD format"
}
```

**404 Not Found**
```json
{
  "error": "Habit not found"
}
```

**405 Method Not Allowed**
```json
{
  "error": "Only POST method is allowed"
}
```

---

## 8. Get Habit Logs

**Method:** `GET`  
**Endpoint:** `/habits/<id>/logs/`

### Description
Returns all completion logs for a specific habit.

### Success Response
**200 OK**

### Example Response
```json
[
  {
    "id": 1,
    "habit_id": 1,
    "habit_name": "Drink More Water",
    "completed_on": "2026-03-08",
    "notes": "Completed after Fajr",
    "created_at": "2026-03-08T16:39:34.817Z"
  }
]
```

### Error Response
**404 Not Found**
```json
{
  "error": "Habit not found"
}
```

---

## 9. Get Habit Streak

**Method:** `GET`  
**Endpoint:** `/habits/<id>/streak/`

### Description
Returns the current streak and total logs for a specific habit.

### Success Response
**200 OK**

### Example Response
```json
{
  "habit_id": 1,
  "habit_name": "Drink More Water",
  "current_streak": 1,
  "total_logs": 1
}
```

### Error Response
**404 Not Found**
```json
{
  "error": "Habit not found"
}
```

---

## Status Codes Used
- `200 OK`
- `201 Created`
- `400 Bad Request`
- `404 Not Found`
- `405 Method Not Allowed`

## Tools Used
- Python
- Django
- SQLite
- Git
- GitHub
- Postman
- Django Test Framework