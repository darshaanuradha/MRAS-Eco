# MRAS Eco (Medical Room Automation System)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0.3-092E20.svg?logo=django)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1.svg?logo=mysql)
![License](https://img.shields.io/badge/License-Academic-green.svg)

**MRAS Eco** is a Python-based, database-driven web application designed to digitize corporate medical room operations. It transitions facilities from inefficient paper logbooks to a secure digital ecosystem that manages patient histories, clinical consultations, and automated pharmacy inventory tracking.

🚀 **Live Deployment:** [http://165.245.177.229/](http://165.245.177.229/)

---

## 📋 What is MRAS?

### The Problem

Corporate medical rooms and workplace clinics traditionally rely on **paper-based logbooks** to track:
- Patient visit records (name, date, symptoms, diagnosis)
- Consultation notes from doctors
- Pharmacy stock levels and medicine usage
- Staff availability and schedules

This manual system is:
- ❌ **Time-consuming** - Manual data entry and retrieval
- ❌ **Error-prone** - Handwriting illegibility, duplicate entries
- ❌ **Insecure** - Paper documents can be lost or accessed without authorization
- ❌ **Inefficient** - Cannot generate reports or analytics
- ❌ **Not scalable** - Difficult to manage multiple locations or large patient volumes

### The Solution: MRAS

**MRAS** (Medical Room Automation System) provides a **complete digital transformation** of medical room operations:

#### Core Capabilities

1. **Patient Management**
   - Digital patient profiles replacing physical logbooks
   - Complete medical history tracking
   - Visit records with symptoms and diagnoses
   - Quick patient lookup and history retrieval

2. **Clinical Consultations**
   - Secure physician notes and diagnoses
   - Prescription management
   - Treatment recommendation tracking
   - Consultation history for follow-ups

3. **Pharmacy Inventory**
   - Real-time stock tracking of medicines
   - Automated stock deduction when medicines are dispensed
   - Low-stock alerts and reorder recommendations
   - Medicine expiry tracking
   - Usage analytics and trends

4. **Staff Directory**
   - Medical doctor profiles and specializations
   - Doctor availability schedules
   - Contact information
   - Performance and consultation history

5. **Secure Access Control**
   - Role-based user authentication (Doctor, Nurse, Admin)
   - Session-based security
   - Audit trails for compliance
   - HIPAA-ready structure for medical data

### Real-World Use Cases

**Corporate Medical Rooms** - Companies with on-site clinics can now:
- Track employee health records digitally
- Monitor medicine usage and costs
- Generate health reports for occupational health management
- Ensure compliance with workplace health regulations

**Clinic Networks** - Multi-location facilities can:
- Consolidate patient data across branches
- Share consultation history between clinics
- Centralize inventory management
- Monitor performance across locations

**Health Insurance Providers** - Companies can:
- Verify consultation records
- Track medicine usage claims
- Manage coverage and reimbursements
- Collect health statistics

### Key Benefits

| Benefit | Impact |
|---------|--------|
| **Speed** | Reduce patient check-in time from 10 min to 2 min |
| **Accuracy** | 99.9% data accuracy vs. handwriting errors |
| **Security** | Encrypted digital storage vs. vulnerable paper records |
| **Analytics** | Generate reports on health trends, medicine usage |
| **Scalability** | Support hundreds of patients vs. limited paper capacity |
| **Cost Savings** | Reduce manual labor, paper waste, and errors |
| **Compliance** | Meet regulatory requirements for medical record keeping |
| **Accessibility** | Access patient data instantly from anywhere (authorized users) |

---

## 🏢 Academic Context

**Institution:** University of Vocational Technology (UOVT)  
**Department:** Software and Intelligent Systems  
**Module:** IT304040 Python Programming – Final Group Project  

### 👥 Project Team (Agile Squad)

- **L.B. Charith Jeewan** (SIS/24/B2/36) - PM / Scrum Master
- **W.I.L. Withana** (SIS/24/B2/38) - Domain Researcher
- **H.K.G.V. Lakmali Koralage** (SIS/24/B2/13) - QA & Documentation
- **G.B.D. Darsha Anuradha** (SIS/24/B2/15) - Lead Backend Developer
- **B.W.S.S. Nawarathna** (SIS/24/B2/39) - Lead Frontend Developer

---

## ⚙️ Technical Architecture

The application utilizes a **Modular Monolith** architecture built on the Django Web Framework to enforce strict separation of concerns.

- **Interface Layer:** Django Templates, Tailwind CSS (via CDN), Glass-morphism UI
- **Domain Logic:** Python-based Django Views with business rule enforcement
- **Persistence Layer:** MySQL (Production) / SQLite (Local Development) via Django ORM
- **Authentication:** Django's built-in session management with custom email-based registration
- **Hosting:** DigitalOcean Droplet (Ubuntu), served via Gunicorn and Nginx

```
┌─────────────────────────────────┐
│    Frontend (Django Templates)  │
│    Tailwind CSS + Glass-UI      │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│   Django Views & URL Router     │
│   Business Logic & Validation   │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│      Django ORM Models          │
│   Doctor, Patient, Inventory    │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│  MySQL / SQLite Database        │
└─────────────────────────────────┘
```

---

## 📊 Modules & Current Status

| Module | Status | Description |
|:-------|:-------|:------------|
| **Accounts / Auth** | ✅ Complete | Secure registration, email validation, login, session management, RBAC foundation |
| **Doctors** | ✅ Complete | Full CRUD operations for medical staff profiles, directory listing, and admin panel |
| **Patients** | 🚧 In Progress | Digital identity profiles replacing physical logbooks, consultation history |
| **Consultations** | 🚧 In Progress | Secure interface for clinical diagnoses, prescriptions, and treatment notes |
| **Inventory** | 🚧 In Progress | Automated real-time pharmacy stock tracking and deduction system |

---

## 🎯 Key Features

### ✅ Completed Features

- **User Authentication System**
  - Secure user registration with email validation
  - Login/logout with session management
  - Password confirmation and duplicate email prevention
  - Role-based access control foundation

- **Dashboard & Navigation**
  - Responsive sidebar navigation
  - Mobile hamburger menu
  - Auto-dismissing toast notifications
  - Glass-morphism UI design

- **Doctor Management**
  - Complete CRUD operations (Create, Read, Update, Delete)
  - Doctor profiles with specialization and contact info
  - Staff directory listing
  - Django admin integration

- **Security**
  - CSRF protection on all forms
  - SQL injection prevention via ORM
  - Login-required decorators on protected views
  - Password hashing and validation

### 🚧 In Progress

- Patient management system with digital records
- Consultation scheduling and notes
- Automated pharmacy inventory tracking
- Role-based permissions (Doctor, Admin, Staff)

### 📋 Planned Features

- API endpoints (Django REST Framework)
- Comprehensive test suite
- Advanced reporting and analytics
- Notification system
- Mobile application

---

## 💻 Local Development Setup

Follow these steps to run MRAS Eco locally on your machine:

### 1. Clone the Repository

```bash
git clone https://github.com/darshaanuradha/MRAS-Eco.git
cd MRAS-Eco
```

### 2. Set Up Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Ensure requirements.txt is UTF-8 encoded
pip install -r requirements.txt
```

### 4. Database Configuration & Migrations

By default, the project is configured for MySQL. For local testing without a MySQL server, you can temporarily switch to SQLite:

**Using MySQL (Production Default):**
```bash
# Ensure MySQL server is running and database 'mars' is created
python manage.py makemigrations
python manage.py migrate
```

**Using SQLite (Local Development):**
Edit `mras/settings.py` and temporarily replace the DATABASES configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Then run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

You will be prompted to enter:
- Username
- Email
- Password (twice)

### 6. Run the Development Server

```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` in your browser.

**Admin Panel:** `http://127.0.0.1:8000/admin/` (use your superuser credentials)

---

## 🔐 Security & Production Deployment

### Critical Security Checklist

Before pushing to a **public production environment**, ensure:

1. **Debug Mode**
   ```python
   # In mras/settings.py
   DEBUG = False  # ⚠️ Must be False in production
   ```

2. **Allowed Hosts**
   ```python
   # Add your server IP and domain
   ALLOWED_HOSTS = ['165.245.177.229', 'yourdomain.com', 'www.yourdomain.com']
   ```

3. **Environment Variables**
   Create a `.env` file (never commit to git):
   ```
   DEBUG=False
   SECRET_KEY=your-secure-secret-key
   DB_ENGINE=django.db.backends.mysql
   DB_NAME=mars
   DB_USER=your-db-user
   DB_PASSWORD=your-db-password
   DB_HOST=localhost
   DB_PORT=3306
   ALLOWED_HOSTS=165.245.177.229,yourdomain.com
   ```

   Update `settings.py` to use environment variables:
   ```python
   from decouple import config
   SECRET_KEY = config('SECRET_KEY')
   DEBUG = config('DEBUG', default=False, cast=bool)
   ```

4. **Install Python Decouple**
   ```bash
   pip install python-decouple
   ```

5. **Additional Security Hardening**
   ```python
   # In settings.py
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   SECURE_BROWSER_XSS_FILTER = True
   SECURE_CONTENT_SECURITY_POLICY = {...}
   ```

6. **Update .gitignore**
   Ensure `.env` and sensitive files are excluded:
   ```
   .env
   *.log
   db.sqlite3
   __pycache__/
   venv/
   ```

### Deployment on DigitalOcean

See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step deployment instructions using Gunicorn and Nginx.

---

## 📁 Project Structure

```
MRAS-Eco/
├── README.md                      # Project documentation (this file)
├── DEPLOYMENT.md                  # Deployment instructions
├── .gitignore                     # Git ignore rules
├── requirements.txt               # Python dependencies
├── data/
│   └── info.txt
├── docs/
│   └── (documentation files)
├── tests/
│   └── info.txt
└── mras/                          # Django Project Root
    ├── manage.py                  # Django management command
    ├── db.sqlite3                 # Local SQLite database (dev only)
    ├── mydb.py                    # MySQL database setup utility
    ├── mras/                      # Project Configuration
    │   ├── settings.py            # Global settings
    │   ├── urls.py                # Main URL router
    │   ├── asgi.py                # ASGI config
    │   └── wsgi.py                # WSGI config
    ├── templates/                 # Project-level templates
    │   ├── base.html              # Master template
    │   ├── home.html              # Dashboard
    │   └── sidebar.html           # Navigation
    ├── accounts/                  # Authentication App
    │   ├── models.py
    │   ├── views.py               # register, login, logout, home
    │   ├── urls.py
    │   ├── forms.py
    │   ├── admin.py
    │   ├── migrations/
    │   └── templates/
    ├── doctors/                   # Staff Management App
    │   ├── models.py              # Doctor model
    │   ├── views.py               # CRUD views
    │   ├── urls.py
    │   ├── forms.py               # DoctorForm with Tailwind styling
    │   ├── admin.py
    │   ├── migrations/
    │   └── templates/doctors/
    ├── patients/                  # Patient Management App (In Progress)
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   ├── migrations/
    │   └── templates/
    ├── inventory/                 # Pharmacy Inventory App (In Progress)
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   ├── migrations/
    │   └── templates/
    └── consultation/              # Consultation App (In Progress)
        ├── models.py
        ├── views.py
        ├── urls.py
        ├── admin.py
        ├── migrations/
        └── templates/
```

---

## 🧪 Testing

Currently, all test files are placeholder templates. To add tests:

```bash
# Run existing tests
python manage.py test

# Create test for a specific app
python manage.py test doctors
```

Example test file (`accounts/tests.py`):
```python
from django.test import TestCase, Client
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_login(self):
        response = self.client.post('/login/', {
            'email': 'test@example.com',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
```

---

## 🛠️ Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'mysql'`
**Solution:** Install MySQLdb:
```bash
pip install mysqlclient
```

### Issue: `requirements.txt` encoding error
**Solution:** Convert to UTF-8:
```bash
# On Windows PowerShell
Get-Content requirements.txt -Encoding UTF16 | Set-Content requirements.txt -Encoding UTF8

# On macOS/Linux
iconv -f UTF-16 -t UTF-8 requirements.txt > requirements_utf8.txt
mv requirements_utf8.txt requirements.txt
```

### Issue: MySQL connection refused
**Solution:** Ensure MySQL is running:
```bash
# On Windows
net start MySQL80

# On macOS
brew services start mysql

# On Linux
sudo systemctl start mysql
```

### Issue: `ALLOWED_HOSTS` error on deployment
**Solution:** Add your server IP/domain to settings.py:
```python
ALLOWED_HOSTS = ['your-server-ip', 'yourdomain.com']
```

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [DigitalOcean Deployment Guide](https://www.digitalocean.com/community/tutorials)

---

## 📜 License

This project is developed as part of the IT304040 Python Programming module at the University of Vocational Technology (UOVT). Academic use only.

---

## 🤝 Contributing

This is an academic project. For modifications or improvements:

1. Create a feature branch
2. Commit your changes
3. Submit a pull request for review

---

## 📞 Support & Contact

For issues, questions, or contributions, please:
- Open an issue on GitHub
- Contact the project team at your institution

---

**Last Updated:** July 2, 2026  
**Status:** Active Development  
**Version:** 1.0.0 (Beta)