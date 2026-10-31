# 🌟 MyProject — Django Portfolio Website

A sleek, full-featured **personal portfolio web app** built with Django. Showcase your projects with a stunning dark glassmorphism UI. Includes user authentication and full CRUD functionality.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat-square&logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

---

## ✨ Features

- 🔐 **User Authentication** — Register, Login, Logout
- 📁 **Project Management** — Add, Edit, Delete your portfolio projects
- 🎨 **Dark Glassmorphism UI** — Modern, premium dark theme design
- 📱 **Responsive Design** — Works on all screen sizes
- 🔒 **Login Protected** — Only logged-in users can manage projects

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django 6.0 |
| Frontend | HTML5, CSS3 |
| Database | SQLite3 |
| Auth | Django built-in auth |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/kevinbakraniya2-ship-it/myproject.git
cd myproject
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Start the Server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**

---

## 📂 Project Structure

```
myproject/
├── home/                   # Main app
│   ├── templates/home/     # HTML templates
│   ├── static/home/        # CSS files
│   ├── models.py           # Database models
│   ├── views.py            # App logic
│   ├── forms.py            # Django forms
│   └── urls.py             # URL routing
├── myproject/              # Project config
│   └── settings.py
├── .env                    # Secret keys (not in git)
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## 👤 Author

**Kevin Bakraniya**
- GitHub: [@kevinbakraniya2-ship-it](https://github.com/kevinbakraniya2-ship-it)

---

## 📄 License

This project is licensed under the **MIT License**.
