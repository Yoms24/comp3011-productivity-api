# API Documentation

## Project
COMP3011 Productivity API

## Base URL
`http://127.0.0.1:8000/api/`

## Overview
This API was built using Django and SQLite. It supports CRUD operations for habits and includes a simple analytics summary endpoint.

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