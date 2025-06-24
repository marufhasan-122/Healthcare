# 🏥 Django Health Care App

A modern and responsive healthcare appointment system built with **Django** and **Tailwind CSS**. Users can view available doctors, make appointments, and contact the clinic directly from the website.

## 🔗 Live Project

This project is currently **not deployed**. To run it locally, follow the instructions below.

## 📌 Features

- 🏠 **Home Page** with banner, services, and contact form.
- 📋 **Appointment Form** to book appointments.
- 📞 **Contact Form** for sending messages.
- 👨‍⚕️ **Doctor List Page** to view available doctors.
- 📄 **About**, **Services**, and **Contact** pages.
- 🔒 CSRF protection and Django form validation.
- 🎨 Tailwind CSS for responsive and elegant UI.

## 🛠️ Tech Stack

- **Backend:** Django 5+
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite3 (default)
- **Python Version:** 3.10+

## 📁 Project Structure

```

Django-Health-Care-APP/
├── core/                   # Main Django app
│   ├── migrations/
│   ├── templates/core/     # All HTML templates
│   ├── static/             # Images, Icons, CSS
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── healthcare/             # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3              # Database
├── manage.py
└── README.md

````

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/najibulazam/Django-Health-Care-APP.git
cd Django-Health-Care-APP
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac/Git Bash
venv\Scripts\activate         # On Windows/Powershell
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not yet added, install manually:

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Now open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 🧪 Sample Data

You can populate the doctor list by adding dummy doctor data in the Django admin panel or through fixtures.

## 📬 Contact

Developed by [Md Najib Ul Azam Mahi](https://github.com/najibulazam)

If you like this project, don’t forget to ⭐ the repo!

---

### ✅ Next Steps:
- Place this in a file named `README.md` in the root of your project.
- You may also want to add a `requirements.txt` using:

```bash
pip freeze > requirements.txt
````

Let me know if you want me to add that or generate screenshots for the README.
