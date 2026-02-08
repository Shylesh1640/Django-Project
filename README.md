# Django Blog Project

A Django-based blog application with features for creating, managing, and displaying blog posts.

## Demo Video

[![Watch Demo](https://img.shields.io/badge/▶_Watch_Demo-Click_Here-red?style=for-the-badge&logo=youtube)](Django%20rec.mp4)

> 💡 **To display the video directly on GitHub:**
> 1. Upload your video to YouTube or convert to GIF
> 2. For GIF: `ffmpeg -i "Django rec.mp4" -vf "fps=10,scale=800:-1" demo.gif`
> 3. Then replace this section with: `![Demo](demo.gif)`

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
