# 🔨 Django Auction Platform

This project is a web-based **online auction system** built with Django. It allows users to register, log in, create listings, categorize them, place bids, and leave comments on auction items.

---

## 🌟 Features

- 🔐 **User Authentication** (register, login, logout)
- 🧾 **Listing System**: Users can create and manage auction listings.
- 📂 **Category System**: Listings can be assigned to multiple categories.
- 💰 **Bidding System**: Users can place bids on active listings.
- 💬 **Commenting System**: Users can comment on listings.
- 📸 **Image Support**: Listings can include image URLs.
- 🕒 **Created timestamp**: Listings have a creation date.
- ✅ **Active Status**: Listings can be marked as active or inactive.

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/metaamiri/django-ecommerce.git
cd django-ecommerce/commerce
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a Superuser
```bash
python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 to use the app.

## 🧑 Admin Panel
Access the admin panel at:
http://127.0.0.1:8000/admin

- Use your superuser credentials to:
- Manage users
- Add/edit listings
- View comments, bids, and categories

## 🙏 Acknowledgements
Inspired by CS50 Web Programming with Python and Django project ideas.
