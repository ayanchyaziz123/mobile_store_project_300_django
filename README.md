# 📱 Mobile Store Project (Django)

A Django-based web application for managing a mobile store. This project includes product listing, cart functionality, user authentication, and basic admin management.

## 🚀 Features

- User registration & login
- Product catalog with images and details
- Add to cart and order placement
- Admin dashboard for product and order management
- Mobile-friendly responsive design

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default Django database)
- **Frontend**: HTML, CSS, Bootstrap
- **Authentication**: Django's built-in auth system

## 📂 Project Structure


## ⚙️ Getting Started

### Prerequisites

- Python 3.x
- pip
- virtualenv (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/ayanchyaziz123/mobile_store_project_300_django.git

cd mobile_store_project_300_django

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt  # If requirements.txt not available, install Django manually
pip install django

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
