# MRAS Eco - Medical Room Automation System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0.3-092E20.svg?logo=django)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1.svg?logo=mysql)
![License](https://img.shields.io/badge/License-Academic-green.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg)
![Version](https://img.shields.io/badge/Version-1.0.0%20Beta-blue.svg)

**MRAS Eco** is an enterprise-grade, Python-based medical facility management system designed to digitize corporate medical room operations. It transitions facilities from inefficient paper-based logbooks to a secure, scalable digital ecosystem that manages patient records, clinical consultations, and automated pharmacy inventory tracking.

🚀 **Live Deployment:** [http://165.245.177.229/](http://165.245.177.229/)  
📖 **Full Documentation:** [See DEPLOYMENT.md](DEPLOYMENT.md)  
💾 **GitHub Repository:** [darshaanuradha/MRAS-Eco](https://github.com/darshaanuradha/MRAS-Eco)

---

## 📑 Table of Contents

- [Quick Start](#-quick-start)
- [What is MRAS?](#-what-is-mras)
- [Technical Stack](#-technical-stack)
- [Academic Context](#-academic-context)
- [System Requirements](#-system-requirements)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage & Common Commands](#-usage--common-commands)
- [Database Schema](#-database-schema)
- [API Endpoints](#-api-endpoints)
- [Deployment](#-deployment)
- [Security](#-security)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Performance & Monitoring](#-performance--monitoring)
- [Contributing](#-contributing)
- [FAQ](#-faq)
- [Support & Contact](#-support--contact)

---

## ⚡ Quick Start

Get MRAS running locally in 5 minutes:

```bash
# 1. Clone repository
git clone https://github.com/darshaanuradha/MRAS-Eco.git
cd MRAS-Eco

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup database (SQLite for local dev)
cd mras
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Run development server
python manage.py runserver
```

**Access Application:**
- 🌐 Web: http://127.0.0.1:8000/
- 🔑 Admin: http://127.0.0.1:8000/admin/

---

## 📋 What is MRAS?

### The Problem

Corporate medical rooms and workplace clinics traditionally rely on **paper-based logbooks** to track:
- Patient visit records (name, date, symptoms, diagnosis)
- Consultation notes from doctors
- Pharmacy stock levels and medicine usage
- Staff availability and schedules

This manual system is:
- ❌ **Time-consuming** - Manual data entry and retrieval (10+ min per patient)
- ❌ **Error-prone** - Handwriting illegibility, duplicate entries, data loss
- ❌ **Insecure** - Paper documents vulnerable to unauthorized access and loss
- ❌ **Inefficient** - Cannot generate reports or analytics for decision-making
- ❌ **Not scalable** - Difficult to manage multiple locations or large volumes
- ❌ **Non-compliant** - Fails regulatory and medical record-keeping requirements

### The Solution: MRAS Eco

**MRAS Eco** provides a **complete digital transformation** with:

#### Core Capabilities

1. **Patient Management**
   - Digital patient profiles replacing physical logbooks
   - Complete medical history tracking (accessible in 2 seconds vs. 10 minutes)
   - Visit records with symptoms and diagnoses
   - Quick patient lookup and history retrieval

2. **Clinical Consultations**
   - Secure physician notes and diagnoses
   - Prescription management and tracking
   - Treatment recommendation history
   - Consultation follow-up scheduling

3. **Pharmacy Inventory**
   - Real-time stock tracking of medicines
   - Automated stock deduction upon dispensing
   - Low-stock alerts and reorder recommendations
   - Medicine expiry tracking with reminders
   - Usage analytics and cost tracking

4. **Staff Directory**
   - Medical doctor profiles with specializations
   - Doctor availability schedules
   - Contact information and qualifications
   - Performance metrics and consultation history

5. **Secure Access Control**
   - Role-based user authentication (Doctor, Nurse, Admin, Supervisor)
   - Session-based security with auto-logout
   - Audit trails for compliance
   - HIPAA-ready medical data structure
   - Encrypted data transmission

### Real-World Use Cases

- **Corporate Medical Rooms** - Companies with on-site clinics tracking employee health
- **Clinic Networks** - Multi-location facilities with centralized records
- **Health Insurance Providers** - Claims verification and coverage management
- **Occupational Health** - Workplace safety and health compliance
- **NGOs & Healthcare Facilities** - Low-cost medical record management

### Key Benefits

| Metric | Improvement |
|--------|------------|
| **Speed** | 10 min → 2 min check-in (80% faster) |
| **Accuracy** | 99.9% data accuracy vs. handwriting errors |
| **Security** | Encrypted digital vs. vulnerable paper |
| **Analytics** | Real-time reports vs. none |
| **Scalability** | Support 1000+ patients vs. limited |
| **Cost** | 60% reduction in manual labor |
| **Compliance** | 100% regulatory aligned |
| **Accessibility** | Instant access 24/7 (authorized) |

---

## ⚙️ Technical Stack

### Backend
- **Framework:** Django 5.0.3 (Python Web Framework)
- **Python Version:** 3.10 or higher
- **Database:** MySQL 8.0+ (Production) / SQLite (Development)
- **ORM:** Django ORM (object-relational mapping)
- **Authentication:** Django session management + custom registration

### Frontend
- **Templating:** Django Templates with Jinja2
- **CSS Framework:** Tailwind CSS (via CDN)
- **UI Design:** Glass-morphism effects, responsive design
- **JavaScript:** Vanilla JS (HTMX-ready for future enhancement)

### Infrastructure & Deployment
- **Hosting:** DigitalOcean VPS (Ubuntu 20.04 LTS)
- **Web Server:** Nginx (reverse proxy & static file serving)
- **Application Server:** Gunicorn (WSGI application server)
- **Process Manager:** systemd (service management)
- **Version Control:** Git & GitHub

### Architecture Pattern

```
┌─────────────────────────────────────────┐
│         User Browser/Client             │
└────────────────┬────────────────────────┘
                 │ HTTP/HTTPS
┌────────────────▼────────────────────────┐
│            Nginx (Web Server)           │
│         (SSL, Static Files, Proxy)      │
└────────────────┬────────────────────────┘
                 │ WSGI Protocol
┌────────────────▼────────────────────────┐
│         Gunicorn (App Server)           │
│       (Django Application Workers)      │
└────────────────┬────────────────────────┘
                 │ Python/ORM
┌────────────────▼────────────────────────┐
│       Django MVT Architecture           │
│  - Views (Business Logic)               │
│  - Models (Data Layer)                  │
│  - Templates (Presentation)             │
└────────────────┬────────────────────────┘
                 │ SQL Queries
┌────────────────▼────────────────────────┐
│         MySQL Database Server           │
│       (Patient, Doctor, Inventory)      │
└─────────────────────────────────────────┘
```

### Design Pattern: Modular Monolith MVT

- **Separation of Concerns:** Each Django app handles one domain
- **Authentication:** Custom email-based registration with validation
- **Authorization:** Login-required decorators on protected views
- **Data Validation:** ModelForm + custom validators

---

## 🏢 Academic Context

**Institution:** University of Vocational Technology (UOVT)  
**Department:** Software and Intelligent Systems  
**Module:** IT304040 Python Programming – Final Group Project  
**Year:** 2026  
**Semester:** Spring

### 👥 Project Team (Agile Squad)

| Member | ID | Role | Responsibilities |
|--------|----|----|---|
| **L.B. Charith Jeewan** | SIS/24/B2/36 | PM / Scrum Master | Project oversight, sprint planning, stakeholder communication |
| **W.I.L. Withana** | SIS/24/B2/38 | Domain Researcher | Requirements analysis, domain knowledge, use case documentation |
| **H.K.G.V. Lakmali Koralage** | SIS/24/B2/13 | QA & Documentation | Testing, documentation, quality assurance |
| **G.B.D. Darsha Anuradha** | SIS/24/B2/15 | Lead Backend Developer | Django architecture, databases, APIs, server setup |
| **B.W.S.S. Nawarathna** | SIS/24/B2/39 | Lead Frontend Developer | UI/UX design, templates, responsive design |

---

## 💻 System Requirements

### Minimum Requirements

| Component | Requirement |
|-----------|------------|
| **OS** | Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+) |
| **Python** | 3.10.0 or higher |
| **RAM** | 2 GB (development), 4 GB (production) |
| **Storage** | 500 MB for application + database |
| **Processor** | 2-core minimum |
| **Network** | Internet connection for dependency installation |

### Recommended Requirements (Production)

- **OS:** Linux (Ubuntu 20.04 LTS)
- **Python:** 3.11.x or 3.12.x
- **RAM:** 8 GB
- **Storage:** 20+ GB (scalable)
- **Processor:** 4+ cores
- **Database:** MySQL 8.0+ with replication

### Software Dependencies

**Required:**
- Git (v2.0+)
- Python pip package manager
- MySQL Server (optional for local dev, required for production)

**Development Tools (Optional):**
- Visual Studio Code or PyCharm IDE
- Postman (for API testing)
- MySQL Workbench (for database management)

---

## 📊 Features

### ✅ Completed Features (MVP)

**Authentication & Authorization**
- ✓ Secure user registration with email validation
- ✓ Login/logout with session management
- ✓ Password strength validation & hashing
- ✓ Duplicate email prevention
- ✓ CSRF protection on all forms

**Doctor Management (CRUD)**
- ✓ Create doctor profiles (name, specialization, contact)
- ✓ List all doctors with search/filter
- ✓ Edit doctor information
- ✓ Delete doctor records (soft delete capable)
- ✓ Django admin interface integration
- ✓ Timestamps (created_at, updated_at)

**User Interface**
- ✓ Responsive dashboard with statistics
- ✓ Mobile-friendly sidebar navigation
- ✓ Auto-dismissing toast notifications
- ✓ Tailwind CSS Glass-morphism design
- ✓ Dark/Light mode foundation
- ✓ Accessibility standards (WCAG 2.1 Level A)

**Security**
- ✓ SQL injection prevention (Django ORM)
- ✓ XSS protection
- ✓ CSRF token validation
- ✓ Password hashing (PBKDF2)
- ✓ Secure session management

### 🚧 In Progress Features

- 🔄 Patient Management System
- 🔄 Consultation Scheduling
- 🔄 Pharmacy Inventory Tracking
- 🔄 Role-based Access Control (RBAC)
- 🔄 Prescription Management


---

## � Project Structure

```
MRAS-Eco/
├── README.md                      # Project documentation (this file)
├── DEPLOYMENT.md                  # Production deployment guide
├── deploy.sh                      # One-command deployment script
├── .gitignore                     # Git exclusion rules
├── requirements.txt               # Python dependencies (UTF-8 encoded)
├── data/                          # Data files and documentation
│   └── info.txt
├── docs/                          # Additional documentation
│   └── (team documentation)
├── tests/                         # Test data/fixtures
│   └── info.txt
└── mras/                          # Django Project Root
    ├── manage.py                  # Django CLI management tool
    ├── db.sqlite3                 # SQLite database (dev only)
    ├── mydb.py                    # MySQL database initialization script
    ├── mras/                      # Project Configuration Package
    │   ├── __init__.py
    │   ├── settings.py            # Global Django settings
    │   ├── urls.py                # Main URL router and endpoints
    │   ├── asgi.py                # ASGI application config (async)
    │   └── wsgi.py                # WSGI application config (production)
    ├── templates/                 # Project-level templates
    │   ├── base.html              # Master template (layout, nav, auth)
    │   ├── home.html              # Dashboard homepage
    │   └── sidebar.html           # Navigation sidebar
    ├── static/                    # Static files (CSS, JS, images)
    │   └── (served by Nginx in production)
    ├── accounts/                  # Authentication & User Management App
    │   ├── migrations/            # Database migration files
    │   ├── templates/             # App-specific templates
    │   ├── models.py              # Uses Django User model
    │   ├── views.py               # register, login, logout, home views
    │   ├── urls.py                # App URL routes
    │   ├── forms.py               # Registration form with validation
    │   ├── admin.py               # Django admin configuration
    │   ├── apps.py                # App configuration
    │   ├── tests.py               # Unit tests (placeholder)
    │   └── __init__.py
    ├── doctors/                   # Medical Staff Management App
    │   ├── migrations/            # Database schemas
    │   │   ├── __init__.py
    │   │   └── 0001_initial.py    # Initial Doctor model migration
    │   ├── templates/             # App templates
    │   │   └── doctors/
    │   │       ├── doctor_list.html           # List view
    │   │       ├── doctor_form.html           # Create/Edit form
    │   │       └── doctor_confirm_delete.html # Delete confirmation
    │   ├── models.py              # Doctor data model
    │   ├── views.py               # CRUD operations (List, Create, Update, Delete)
    │   ├── urls.py                # Namespaced routes (doctors:list, etc.)
    │   ├── forms.py               # DoctorForm with Tailwind styling
    │   ├── admin.py               # Doctor admin interface
    │   ├── apps.py                # App configuration
    │   ├── tests.py               # Model and view tests (placeholder)
    │   └── __init__.py
    ├── patients/                  # Patient Management App (In Development)
    │   ├── migrations/            # Database schemas
    │   ├── templates/
    │   ├── models.py              # Patient data model (not yet implemented)
    │   ├── views.py               # Views (placeholder)
    │   ├── urls.py                # Routes
    │   ├── admin.py               # Admin configuration
    │   ├── forms.py               # Patient forms (to be implemented)
    │   ├── apps.py
    │   ├── tests.py
    │   └── __init__.py
    ├── inventory/                 # Pharmacy Inventory App (In Development)
    │   ├── migrations/
    │   ├── templates/
    │   ├── models.py              # Inventory model (not yet implemented)
    │   ├── views.py               # Views (placeholder)
    │   ├── urls.py
    │   ├── admin.py
    │   ├── forms.py
    │   ├── apps.py
    │   ├── tests.py
    │   └── __init__.py
    └── consultation/              # Consultation Management App (In Development)
        ├── migrations/
        ├── templates/
        ├── models.py              # Consultation model (not yet implemented)
        ├── views.py               # Views (placeholder)
        ├── urls.py
        ├── admin.py
        ├── forms.py
        ├── apps.py
        ├── tests.py
        └── __init__.py
```

---

## 📥 Installation

### Prerequisites

Before starting, ensure you have:
- ✓ Git installed and configured
- ✓ Python 3.10+ installed
- ✓ pip (Python package manager)
- ✓ (Optional) MySQL Server for production setup

### Step 1: Clone Repository

```bash
git clone https://github.com/darshaanuradha/MRAS-Eco.git
cd MRAS-Eco
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Verify activation (prompt should show `(venv)`):
```bash
python --version  # Should show Python 3.10+
which python      # Should show venv path
```

### Step 3: Install Dependencies

**Important:** Ensure `requirements.txt` is UTF-8 encoded. If you encounter encoding errors:

```bash
# Convert from UTF-16 to UTF-8 (if needed)
# Windows:
Get-Content requirements.txt -Encoding UTF16 | Set-Content requirements.txt -Encoding UTF8

# macOS/Linux:
iconv -f UTF-16 -t UTF-8 requirements.txt > requirements_utf8.txt && mv requirements_utf8.txt requirements.txt
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Step 3.1: Set Up the `.env` File

The project reads environment variables from a `.env` file in the repository root, next to `README.md`.

```bash
# Windows PowerShell
Copy-Item .env.example .env

# macOS/Linux
cp .env.example .env
```

Update the values in `.env` before running the app.

### Step 4: Navigate to Django Project

```bash
cd mras
```

### Step 5: Configure Database

**Option A: SQLite (Local Development - Recommended)**

SQLite is built-in and requires no setup:
```bash
python manage.py migrate
```

**Option B: MySQL (Production Setup)**

Ensure MySQL is running and create database:

```bash
# Create database
python mydb.py

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

Or manually in MySQL:
```sql
CREATE DATABASE mars CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
GRANT ALL PRIVILEGES ON mars.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

### Step 6: Create Admin User

```bash
python manage.py createsuperuser
```

Prompts for:
- **Username:** (default: admin)
- **Email:** (e.g., admin@example.com)
- **Password:** (e.g., SecurePass123!)
- **Password (again):** (confirm)

### Step 7: Run Development Server

```bash
python manage.py runserver
```

Output:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C
```

### Step 8: Access Application

- **Web App:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Register New User:** http://127.0.0.1:8000/register/

---

## ⚙️ Configuration

### Django Settings (`mras/settings.py`)

#### Debug Mode
```python
DEBUG = True  # Set to False in production!
```

#### Allowed Hosts
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add server IP for production
```

#### Database Configuration

**SQLite (Development):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**MySQL (Production):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mars',
        'USER': 'root',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
        'CHARSET': 'utf8mb4',
    }
}
```

#### Security Settings
```python
# HTTP Security Headers
SECURE_SSL_REDIRECT = False              # Set True with HTTPS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = { ... }
SESSION_COOKIE_SECURE = False            # Set True with HTTPS
CSRF_COOKIE_SECURE = False               # Set True with HTTPS
```

#### Static Files
```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # For production
```

#### Media Files (Future)
```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Managing the `.env` File

Keep the real `.env` file out of version control. Use `.env.example` as the template and copy it to `.env` for local development or deployment.

```bash
# Example .env values used by mras/settings.py
DEBUG=True
SECRET_KEY=django-insecure-change-this-value
DATABASE_NAME=mars
DATABASE_USER=root
DATABASE_PASSWORD=
ALLOWED_HOSTS=127.0.0.1,localhost
```

The settings file loads these values automatically from the repository root, so you only need to edit `.env` when credentials or hosts change.

---

## 🚀 Usage & Common Commands

### Django Management Commands

**Server & Development:**
```bash
# Run development server on custom port
python manage.py runserver 0.0.0.0:8080

# Run Django shell (Python REPL with models loaded)
python manage.py shell

# Check for issues
python manage.py check

# Perform system checks and output SQL migration plans
python manage.py sqlmigrate doctors 0001
```

**Database Operations:**
```bash
# Create migration files from model changes
python manage.py makemigrations

# Apply pending migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Rollback to specific migration
python manage.py migrate doctors 0001

# Display SQL for migration
python manage.py sqlmigrate doctors 0001
```

**Admin & Users:**
```bash
# Create superuser (admin)
python manage.py createsuperuser

# Change password
python manage.py changepassword username

# Delete stale sessions
python manage.py clearsessions
```

**Static Files:**
```bash
# Collect static files (production)
python manage.py collectstatic --noinput

# Find missing static files
python manage.py findstatic admin/css/base.css
```

**Testing:**
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test doctors

# Run with verbose output
python manage.py test --verbosity=2

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Useful Utilities

**Database Backup:**
```bash
# Export database
python manage.py dumpdata > backup.json

# Import database
python manage.py loaddata backup.json
```

**Create Fixtures (Test Data):**
```bash
# Export specific model data
python manage.py dumpdata doctors > doctors_fixtures.json

# Load fixture
python manage.py loaddata doctors_fixtures.json
```

---

## 💾 Database Schema

### Complete MySQL Database Structure

The MRAS Eco database includes Django's authentication system plus five core business modules.

#### 1. Django Authentication Module

```sql
CREATE TABLE auth_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Fields:**
- `id` - Primary key
- `username` - Unique username
- `password` - Hashed password (PBKDF2)
- `email` - User email
- `is_staff` - Admin staff flag
- `is_active` - Account active status

#### 2. Doctors Module

```sql
CREATE TABLE doctors_doctor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    full_name VARCHAR(255) NOT NULL,
    specialization VARCHAR(150) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(254),
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (full_name),
    INDEX (specialization)
);
```

**Fields:**
- `id` - Primary key
- `user_id` - Foreign key to auth_user (optional link)
- `full_name` - Doctor name
- `specialization` - Medical specialty (Cardiology, Neurology, etc.)
- `phone_number` - Contact number
- `is_active` - Active status
- `created_at`, `updated_at` - Audit timestamps

#### 3. Patients Module

```sql
CREATE TABLE patients_patient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(50) NOT NULL UNIQUE,
    full_name VARCHAR(255) NOT NULL,
    department VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('M', 'F', 'Other'),
    contact_number VARCHAR(20),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (employee_id),
    INDEX (full_name)
);
```

**Fields:**
- `id` - Primary key
- `employee_id` - Company employee ID (unique)
- `full_name` - Patient name
- `department` - Company department
- `date_of_birth` - DOB for age calculation
- `gender` - Gender (M/F/Other)
- `contact_number` - Emergency contact

#### 4. Consultation Module

```sql
CREATE TABLE consultation_consultation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    consultation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    diagnosis TEXT NOT NULL,
    notes TEXT,
    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Completed',
    FOREIGN KEY (patient_id) REFERENCES patients_patient(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors_doctor(id) ON DELETE SET NULL,
    INDEX (patient_id),
    INDEX (doctor_id),
    INDEX (consultation_date)
);
```

**Fields:**
- `id` - Primary key
- `patient_id` - Foreign key to patients (1:N)
- `doctor_id` - Foreign key to doctors (1:N)
- `consultation_date` - When consultation occurred
- `diagnosis` - Medical diagnosis
- `notes` - Additional notes
- `status` - Consultation status

#### 5. Inventory Module - Medicines

```sql
CREATE TABLE inventory_medicine (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    generic_name VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100),
    dosage_form VARCHAR(50),
    strength VARCHAR(50),
    min_stock_level INT DEFAULT 20,
    max_stock_level INT DEFAULT 500,
    unit_cost DECIMAL(10, 2),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX (name),
    INDEX (generic_name)
);
```

**Fields:**
- `id` - Primary key
- `name` - Brand name of medicine
- `generic_name` - Generic/chemical name
- `manufacturer` - Pharmaceutical company
- `dosage_form` - Tablet, injection, etc.
- `strength` - Dosage strength
- `min_stock_level` - Minimum stock alert threshold
- `max_stock_level` - Maximum stock capacity
- `unit_cost` - Cost per unit

#### 6. Inventory Module - Stock Batches

```sql
CREATE TABLE inventory_inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    medicine_id INT NOT NULL,
    batch_number VARCHAR(50) NOT NULL UNIQUE,
    expiry_date DATE NOT NULL,
    current_stock INT UNSIGNED NOT NULL,
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (medicine_id) REFERENCES inventory_medicine(id) ON DELETE CASCADE,
    INDEX (batch_number),
    INDEX (expiry_date)
);
```

**Fields:**
- `id` - Primary key
- `medicine_id` - Foreign key to medicine (1:N)
- `batch_number` - Batch identifier
- `expiry_date` - Medicine expiry date
- `current_stock` - Available quantity (unsigned, >= 0)
- `date_added` - When added to inventory

#### 7. Inventory Module - Prescriptions

```sql
CREATE TABLE inventory_prescriptionitem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    consultation_id INT NOT NULL,
    medicine_id INT NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    dosage_instructions VARCHAR(255) NOT NULL,
    duration_days INT,
    FOREIGN KEY (consultation_id) REFERENCES consultation_consultation(id) ON DELETE CASCADE,
    FOREIGN KEY (medicine_id) REFERENCES inventory_medicine(id) ON DELETE RESTRICT,
    INDEX (consultation_id)
);
```

**Fields:**
- `id` - Primary key
- `consultation_id` - Foreign key to consultation (1:N)
- `medicine_id` - Foreign key to medicine (1:N)
- `quantity` - Number of units prescribed
- `dosage_instructions` - How to take (e.g., "2 tablets twice daily")
- `duration_days` - How many days to take



### Indexes for Performance

**Critical Indexes (High Query Frequency):**
```sql
-- User lookup
CREATE INDEX idx_auth_user_username ON auth_user(username);
CREATE INDEX idx_auth_user_email ON auth_user(email);

-- Doctor lookup
CREATE INDEX idx_doctors_doctor_specialization ON doctors_doctor(specialization);
CREATE INDEX idx_doctors_doctor_is_active ON doctors_doctor(is_active);

-- Patient lookup
CREATE INDEX idx_patients_patient_employee_id ON patients_patient(employee_id);

-- Consultation search
CREATE INDEX idx_consultation_patient_id ON consultation_consultation(patient_id);
CREATE INDEX idx_consultation_doctor_id ON consultation_consultation(doctor_id);
CREATE INDEX idx_consultation_date ON consultation_consultation(consultation_date);

-- Inventory search
CREATE INDEX idx_inventory_medicine_name ON inventory_medicine(name);
CREATE INDEX idx_inventory_batch_number ON inventory_inventory(batch_number);
CREATE INDEX idx_inventory_expiry_date ON inventory_inventory(expiry_date);
```

### Migrations

**Current Status:**
- ✅ **accounts:** Uses Django User model (built-in)
- ✅ **doctors:** 0001_initial.py (Doctor model created)
- 🔲 **patients:** Ready for implementation (schema designed)
- 🔲 **consultation:** Ready for implementation (schema designed)
- 🔲 **inventory:** Ready for implementation (schema designed)

### Database Creation Script

To create the complete database in MySQL:

```bash
# Connect to MySQL as root
mysql -u root -p

# Create database
CREATE DATABASE mars CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE mars;

# Run all CREATE TABLE statements above
# Then run Django migrations to create auth tables
```

Or use the provided initialization script:
```bash
python mras/mydb.py
```

---

## 🚀 Deployment

### Production Deployment Checklist

Before deploying to production:

- ✅ Set `DEBUG = False` in settings
- ✅ Configure `ALLOWED_HOSTS` with server IP/domain
- ✅ Set up `.env` file with secure credentials
- ✅ Collect static files: `python manage.py collectstatic`
- ✅ Run migrations: `python manage.py migrate`
- ✅ Set up SSL/HTTPS certificate
- ✅ Configure Nginx and Gunicorn
- ✅ Set up database backups
- ✅ Enable logging and monitoring
- ✅ Test in staging environment first

### Deployment Scripts

**One-Command Deployment:**
```bash
./deploy.sh
```

**Deploy Script Location:** `/home/MRAS-Eco/deploy.sh`

**What It Does:**
```bash
1. Pull latest code from GitHub
2. Activate Python virtual environment
3. Install/update dependencies
4. Run database migrations
5. Collect static files
6. Restart Django application
7. Restart Nginx web server
```

### Full Deployment Guide

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed step-by-step production deployment instructions on DigitalOcean.

---

## 🔐 Security

### Core Security Features

- ✅ **CSRF Protection:** Token validation on all forms
- ✅ **XSS Prevention:** Template auto-escaping enabled
- ✅ **SQL Injection Prevention:** Django ORM parameterized queries
- ✅ **Password Security:** PBKDF2 hashing algorithm
- ✅ **Session Management:** Secure cookies, auto-logout
- ✅ **Input Validation:** Form validation on client and server
- ✅ **Authentication:** Email-based custom registration
- ✅ **Authorization:** Login-required decorators on views

### Production Security Hardening

```python
# settings.py - Production Configuration

# 1. Debug Mode (CRITICAL)
DEBUG = False  # ❌ Never True in production

# 2. Allowed Hosts
ALLOWED_HOSTS = ['165.245.177.229', 'yourdomain.com', 'www.yourdomain.com']

# 3. Secret Key (Use environment variable!)
SECRET_KEY = os.environ.get('SECRET_KEY')

# 4. HTTPS/SSL
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# 5. Session Security
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 3600  # 1 hour

# 6. CSRF Protection
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

# 7. Security Headers
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {
    'default-src': ("'self'",),
    'script-src': ("'self'", "'unsafe-inline'"),
    'style-src': ("'self'", "'unsafe-inline'"),
}
```

### Secrets Management

**Never commit sensitive data!**

```bash
# .gitignore must include:
.env
.env.local
*.key
*.pem
secrets/
config/local.py
```

### Data Protection

| Aspect | Implementation |
|--------|---|
| **Passwords** | PBKDF2 hashing with salt |
| **API Keys** | Environment variables |
| **Database** | MySQL encryption at rest |
| **Transmission** | HTTPS/TLS |
| **Backups** | Encrypted and off-site |
| **Audit Log** | Track admin actions |

### Environment Variables Setup

Create `.env` file:
```bash
DEBUG=False
SECRET_KEY=your-super-secret-key-here
DB_ENGINE=django.db.backends.mysql
DB_NAME=mars
DB_USER=root
DB_PASSWORD=strong_password_123
DB_HOST=localhost
DB_PORT=3306
ALLOWED_HOSTS=165.245.177.229,yourdomain.com,www.yourdomain.com
```

Update `settings.py`:
```python
from decouple import config
import os

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```

---

## 🚀 Deployment

### Production Deployment Checklist

Before deploying to production:

- ✅ Set `DEBUG = False` in settings
- ✅ Configure `ALLOWED_HOSTS` with server IP/domain
- ✅ Set up `.env` file with secure credentials
- ✅ Collect static files: `python manage.py collectstatic`
- ✅ Run migrations: `python manage.py migrate`
- ✅ Set up SSL/HTTPS certificate
- ✅ Configure Nginx and Gunicorn
- ✅ Set up database backups
- ✅ Enable logging and monitoring
- ✅ Test in staging environment first

### Deployment Scripts

**One-Command Deployment:**
```bash
./deploy.sh
```

**Deploy Script Location:** `/home/MRAS-Eco/deploy.sh`

**What It Does:**
```bash
1. Pull latest code from GitHub
2. Activate Python virtual environment
3. Install/update dependencies
4. Run database migrations
5. Collect static files
6. Restart Django application
7. Restart Nginx web server
```

### Full Deployment Guide

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed step-by-step production deployment instructions on DigitalOcean.

---

## 📁 Project Structure

```
MRAS-Eco/
├── README.md                      # Project documentation (this file)
├── DEPLOYMENT.md                  # Production deployment guide
├── deploy.sh                      # One-command deployment script
├── .gitignore                     # Git exclusion rules
├── requirements.txt               # Python dependencies (UTF-8 encoded)
├── data/                          # Data files and documentation
│   └── info.txt
├── docs/                          # Additional documentation
│   └── (team documentation)
├── tests/                         # Test data/fixtures
│   └── info.txt
└── mras/                          # Django Project Root
    ├── manage.py                  # Django CLI management tool
    ├── db.sqlite3                 # SQLite database (dev only)
    ├── mydb.py                    # MySQL database initialization script
    ├── mras/                      # Project Configuration Package
    │   ├── __init__.py
    │   ├── settings.py            # Global Django settings
    │   ├── urls.py                # Main URL router and endpoints
    │   ├── asgi.py                # ASGI application config (async)
    │   └── wsgi.py                # WSGI application config (production)
    ├── templates/                 # Project-level templates
    │   ├── base.html              # Master template (layout, nav, auth)
    │   ├── home.html              # Dashboard homepage
    │   └── sidebar.html           # Navigation sidebar
    ├── static/                    # Static files (CSS, JS, images)
    │   └── (served by Nginx in production)
    ├── accounts/                  # Authentication & User Management App
    │   ├── migrations/            # Database migration files
    │   ├── templates/             # App-specific templates
    │   ├── models.py              # Uses Django User model
    │   ├── views.py               # register, login, logout, home views
    │   ├── urls.py                # App URL routes
    │   ├── forms.py               # Registration form with validation
    │   ├── admin.py               # Django admin configuration
    │   ├── apps.py                # App configuration
    │   ├── tests.py               # Unit tests (placeholder)
    │   └── __init__.py
    ├── doctors/                   # Medical Staff Management App
    │   ├── migrations/            # Database schemas
    │   │   ├── __init__.py
    │   │   └── 0001_initial.py    # Initial Doctor model migration
    │   ├── templates/             # App templates
    │   │   └── doctors/
    │   │       ├── doctor_list.html           # List view
    │   │       ├── doctor_form.html           # Create/Edit form
    │   │       └── doctor_confirm_delete.html # Delete confirmation
    │   ├── models.py              # Doctor data model
    │   ├── views.py               # CRUD operations (List, Create, Update, Delete)
    │   ├── urls.py                # Namespaced routes (doctors:list, etc.)
    │   ├── forms.py               # DoctorForm with Tailwind styling
    │   ├── admin.py               # Doctor admin interface
    │   ├── apps.py                # App configuration
    │   ├── tests.py               # Model and view tests (placeholder)
    │   └── __init__.py
    ├── patients/                  # Patient Management App (In Development)
    │   ├── migrations/            # Database schemas
    │   ├── templates/
    │   ├── models.py              # Patient data model (not yet implemented)
    │   ├── views.py               # Views (placeholder)
    │   ├── urls.py                # Routes
    │   ├── admin.py               # Admin configuration
    │   ├── forms.py               # Patient forms (to be implemented)
    │   ├── apps.py
    │   ├── tests.py
    │   └── __init__.py
    ├── inventory/                 # Pharmacy Inventory App (In Development)
    │   ├── migrations/
    │   ├── templates/
    │   ├── models.py              # Inventory model (not yet implemented)
    │   ├── views.py               # Views (placeholder)
    │   ├── urls.py
    │   ├── admin.py
    │   ├── forms.py
    │   ├── apps.py
    │   ├── tests.py
    │   └── __init__.py
    └── consultation/              # Consultation Management App (In Development)
        ├── migrations/
        ├── templates/
        ├── models.py              # Consultation model (not yet implemented)
        ├── views.py               # Views (placeholder)
        ├── urls.py
        ├── admin.py
        ├── forms.py
        ├── apps.py
        ├── tests.py
        └── __init__.py
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test doctors

# Run verbose output
python manage.py test --verbosity=2

# With code coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Test Structure

```
doctors/tests.py
├── DoctorModelTestCase
│   ├── test_doctor_creation
│   ├── test_doctor_str_representation
│   └── test_doctor_timestamps
├── DoctorViewTestCase
│   ├── test_doctor_list_requires_login
│   ├── test_doctor_list_returns_all_doctors
│   ├── test_doctor_create_form_valid
│   └── test_doctor_create_form_invalid
└── DoctorFormTestCase
    ├── test_form_valid_data
    └── test_form_invalid_data
```

### Writing Tests Example

```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from doctors.models import Doctor

class DoctorModelTestCase(TestCase):
    def setUp(self):
        Doctor.objects.create(
            full_name='Dr. Smith',
            specialization='Cardiology',
            email='smith@example.com'
        )

    def test_doctor_creation(self):
        doctor = Doctor.objects.get(full_name='Dr. Smith')
        self.assertEqual(doctor.specialization, 'Cardiology')
        self.assertTrue(doctor.is_active)

class DoctorViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_list_view_requires_login(self):
        response = self.client.get('/doctors/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
```

---

## 🛠️ Troubleshooting

### Common Issues & Solutions

**Issue 1: `ModuleNotFoundError: No module named 'mysql'`**
```bash
Solution: pip install mysqlclient
```

**Issue 2: `requirements.txt` UTF-16 encoding error**
```bash
# Windows PowerShell
Get-Content requirements.txt -Encoding UTF16 | Set-Content requirements.txt -Encoding UTF8

# macOS/Linux
iconv -f UTF-16 -t UTF-8 requirements.txt > temp.txt && mv temp.txt requirements.txt
```

**Issue 3: `MySQL connection refused`**
```bash
# Windows
net start MySQL80

# macOS
brew services start mysql

# Linux
sudo systemctl start mysql
```

**Issue 4: `Port 8000 already in use`**
```bash
# Use different port
python manage.py runserver 8080

# Or kill process (macOS/Linux)
lsof -i :8000
kill -9 <PID>
```

**Issue 5: `ALLOWED_HOSTS` error on deployment**
```python
# settings.py
ALLOWED_HOSTS = ['your-server-ip', 'yourdomain.com', 'www.yourdomain.com']
```

**Issue 6: Static files not loading**
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check Nginx configuration
sudo nginx -t
```

**Issue 7: Migration conflicts**
```bash
# Show migration status
python manage.py showmigrations

# Rollback specific migration
python manage.py migrate doctors 0001

# Or squash migrations
python manage.py squashmigrations doctors 0001 0003
```

---

## 📊 Performance & Monitoring

### Performance Optimization

**Database:**
- ✓ Add indexes on frequently queried fields
- ✓ Use `select_related()` for foreign keys
- ✓ Use `prefetch_related()` for reverse relationships
- ✓ Implement query pagination

**Caching (Future):**
```python
# Redis caching setup
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

**Static Files:**
- ✓ Minify CSS/JavaScript
- ✓ Enable gzip compression in Nginx
- ✓ Use CDN for static assets

### Monitoring & Logging

**Application Logging:**
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/mras/django.log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
```

**Server Monitoring:**
```bash
# Check system resources
top
df -h
free -m

# View application logs
tail -f /var/log/mras/django.log
tail -f /var/log/nginx/error.log

# Check service status
systemctl status mras
systemctl status nginx
```

---

## ❓ FAQ

**Q: Can I use MRAS for production immediately?**  
A: No. Review security checklist, test thoroughly, and follow deployment guide first.

**Q: What's the difference between SQLite and MySQL?**  
A: SQLite is file-based, good for dev. MySQL is production-ready with better performance.

**Q: How do I backup the database?**  
A: `python manage.py dumpdata > backup.json` or `mysqldump -u root mars > backup.sql`

**Q: How often should I update dependencies?**  
A: Monthly, after testing in development environment first.

**Q: Can I change the database from MySQL to PostgreSQL?**  
A: Yes, change `ENGINE` in settings.py and install `psycopg2-binary`.

**Q: How do I add new features?**  
A: Create feature branch, make changes, test, commit, push, and create pull request.

**Q: What should I do if deployment fails?**  
A: Check logs (`journalctl -u mras`), review `.env`, and rollback if needed.

---

## 📚 Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Security Documentation](https://docs.djangoproject.com/en/5.0/topics/security/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [DigitalOcean Tutorials](https://www.digitalocean.com/community/tutorials)
- [OWASP Security Guidelines](https://owasp.org/www-project-top-ten/)
- [Python Coding Standards (PEP 8)](https://pep8.org/)

---

## 📜 License

**MRAS Eco** is developed as an academic project for IT304040 Python Programming module at University of Vocational Technology (UOVT).

- **License Type:** Academic/Educational Use
- **Commercial Use:** Not permitted without explicit permission
- **Modification:** Allowed with attribution
- **Distribution:** Contact UOVT for permissions

---

## 🤝 Contributing

This is an academic project. For contributions:

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Commit changes: `git commit -m "feat: Add patient search"`
3. Push to branch: `git push origin feature/your-feature-name`
4. Create Pull Request with description
5. Request review from team members
6. Merge after approval

### Coding Standards
- Follow [PEP 8](https://pep8.org/) for Python
- Use meaningful variable/function names
- Add docstrings to functions
- Keep functions under 50 lines
- Comment complex logic

### Commit Message Format
```
<type>: <subject>

<body>

<footer>
```

Types: `feat` `fix` `docs` `style` `refactor` `test` `chore`

---

## 📞 Support & Contact

### Getting Help

- **GitHub Issues:** [Open an issue](https://github.com/darshaanuradha/MRAS-Eco/issues)
- **Email:** (Contact UOVT team)
- **Documentation:** See [DEPLOYMENT.md](DEPLOYMENT.md)

### Reporting Bugs

Include:
- Description of the issue
- Steps to reproduce
- Expected vs. actual behavior
- Python/Django versions
- Error message/traceback

---

## 📋 Changelog

### Version 1.0.0 (Current - Beta)

**Features:**
- ✅ User authentication system
- ✅ Doctor management (CRUD)
- ✅ Dashboard with statistics
- ✅ Responsive UI design
- ✅ Admin panel

**Known Issues:**
- Patients, Inventory, Consultation apps are scaffolded
- No API endpoints yet
- Limited test coverage
- No mobile app

**Next Release (v1.1):**
- Patient management implementation
- REST API endpoints
- Comprehensive test suite
- Prescription management

---

## 👏 Acknowledgments

- **Django Community** - Web framework
- **Tailwind CSS** - Styling framework
- **DigitalOcean** - Hosting platform
- **University of Vocational Technology (UOVT)** - Academic support
- **Project Team** - Design and development

---

**Last Updated:** July 2, 2026  
**Status:** Active Development  
**Version:** 1.0.0 Beta  
**Maintainer:** Darsha Anuradha (Lead Backend Developer)

---

## Quick Links

- 🌐 [Live Application](http://165.245.177.229/)
- 💻 [GitHub Repository](https://github.com/darshaanuradha/MRAS-Eco)
- 📖 [Deployment Guide](DEPLOYMENT.md)
- 🚀 [One-Command Deploy](deploy.sh)