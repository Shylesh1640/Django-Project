# Django Blog Project

A Django-based blog application with features for creating, managing, and displaying blog posts.

## Demo Video

<video controls width="800">
  <source src="django rec.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Project Structure

- **myapp/** - Main Django project directory
  - **blog/** - Blog application with models, views, and templates
  - **templates/** - Global templates including 404 page

## Features

- Blog post creation and management
- Category support
- About Us page
- Custom slug URLs for posts

## Setup

1. Activate the virtual environment:
   ```bash
   # Windows
   env\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install django mysqlclient faker
   ```

3. Run migrations:
   ```bash
   cd myapp
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Requirements

- Python 3.x
- Django 6.0.1
- MySQL (mysqlclient)
