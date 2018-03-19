# simple djangoproject
This is a simple django project with nested urls.

## Installation

Export database url in the environment. 
Example:
```
export DATABASE_URL="postgres://{user}@localhost:5432/{database_name}"
```

Make migrations and migrate by running the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

Run the server:
```
python manage.py runserver
```

## API Endpoints
| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `/api/authors/` | `POST` | Create a new  |
| `/api/authors/` | `GET` | Retrieve all authors |
| `api/authors/<id>/` | `GET` |  Retrieve an author by ID|
| `api/authors/<id>/` | `PUT` | Update an author |
| `api/authors/<id>/` | `DELETE` | Delete an author |
| `api/authors/<id>/books/` | `POST` |  Create books in a author |
| `api/authors/<id>/books/<book_id>/` | `DELETE`| Delete an item in a author|
| `api/authors/<id>/books/<book_id>/` | `PUT`| update a author item details|

