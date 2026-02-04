# Restaurant Kitchen Service

A Django web application for managing a restaurant kitchen.
The system allows cooks to manage dishes, dish types, and ingredients,
as well as assign responsible cooks to each dish.

---

## Features

- Custom user model (**Cook**) based on `AbstractUser`
- CRUD for:
  - Dish types
  - Dishes
  - Ingredients
  - Cooks
- Assign multiple cooks to dishes
- Assign ingredients to dishes (Many-to-Many)
- Search and filtering for dishes
- Pagination
- Authentication (login / logout)
- Admin panel
- Demo data via fixtures
- Unit tests

---

## Tech Stack

- Python 3
- Django
- SQLite
- Bootstrap 5
- django-crispy-forms

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd <project-folder>
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Load demo data
```bash
python manage.py loaddata kitchen_demo
```

### 7. Run development server
```bash
python manage.py runserver
```
Open in browser:
http://127.0.0.1:8000/

---

## Running Tests

To run all tests:
```bash
python manage.py test
```

To run only kitchen app tests:
```bash
python manage.py test kitchen
```

---

## Demo Data

The project includes demo fixtures with:
- Dish types (Soup, Main course, Salad, Dessert)
- Ingredients
- Dishes

Cooks can be created via:
- Admin panel (/admin/)
- Cooks section in the UI

---

## Admin Panel

Admin panel is available at:
```bash
/admin/
```

You can manage all models there:
- Cooks
- Dishes
- Dish types
- Ingredients

---

## Notes

- The project uses a custom user model (Cook)
- SQLite is used for simplicity
- UI is built with Bootstrap 5
- This project is intended for educational purposes

## Live Demo (Render)

The project is deployed on Render and available at:
```bash
https://service-for-the-restaurant-kitchen-94bf.onrender.com
```

## Authentication

Most pages require authentication.

You can:
- register a new cook via Sign up
- or log in via Login

login: admin

password: 123qwe456rty
