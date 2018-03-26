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
| `/api/v1/users/` | `POST` | Create a new user  |
| `/api/v1/users/` | `GET` | Retrieve all users |
| `/api/v1/users/<user_id>` | `GET` |  Retrieve specific user by ID|
| `/api/v1/users/<user_id>` | `PATCH` | Update specific user info by ID |
| `/api/v1/social_networks/` | `POST` | Create a new social_network  |
| `/api/v1/social_networks/<social_networks_id>` | `GET` |  Retrieve specific social_network by ID|
| `/api/v1/social_networks/social_networks_id>` | `PATCH` | Update specific social_networks by ID |
| `/api/v1/hobbies/` | `POST` | Create a new hobby  |
| `/api/v1/hobbies/` | `GET` | Retrieve all hobbies |
| `/api/v1/hobbies/<hobby_id>` | `GET` |  Retrieve specific hobby by ID|
| `/api/v1/hobbies/<hobby_id>` | `PATCH` | Update specific hobby info by ID |

