# MRAS Eco — Medical Room Automation System

![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.x-092E20.svg?logo=django)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1.svg?logo=mysql&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-CDN-06B6D4.svg?logo=tailwindcss&logoColor=white)
![License](https://img.shields.io/badge/License-Academic-green.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

**MRAS Eco** is a full-stack web application for managing medical room operations — patient records, doctor directories, clinical consultations with prescriptions, and pharmaceutical inventory with automated FEFO (First-Expired, First-Out) stock management.

Built with **Python/Django** and **MySQL**, featuring a modern responsive UI with dark/light theme support.

🌐 **Live Demo:** [http://165.245.177.229/](http://165.245.177.229/)  
💾 **GitHub:** [darshaanuradha/MRAS-Eco](https://github.com/darshaanuradha/MRAS-Eco)

---

## ✨ Key Features

| Module | Capabilities |
|--------|-------------|
| 🔐 **Authentication** | Register, Login, Logout with email-based auth, session management, CSRF protection |
| 📊 **Dashboard** | Real-time KPI cards (patients, consultations, doctors, stock), pending consultations table, low-stock alerts |
| 👥 **Patients** | Full CRUD + search by name, detailed patient profiles with medical history |
| 👨‍⚕️ **Doctors** | Directory with active/inactive status badges, specialization tracking |
| 📋 **Consultations** | Create consultations with inline prescription formsets, status workflow (Pending → Completed → Cancelled) |
| 💊 **FEFO Dispensing** | Automatic batch-level stock deduction using First-Expired, First-Out algorithm with full traceability |
| 📦 **Inventory** | Medicine catalog + batch tracking with expiry dates, search, color-coded stock levels |
| 🔔 **Notifications** | Real-time alerts for expired batches, expiring-soon (30 days), and low-stock medicines |
| 🖨️ **Print** | Printable consultation/prescription slips |
| 🌗 **Theme** | Light/Dark mode toggle with localStorage persistence |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│        Browser (Client)             │
│   HTML + Tailwind CSS + Vanilla JS  │
└────────────────┬────────────────────┘
                 │ HTTP
┌────────────────▼────────────────────┐
│        Django 5.x (MVT)            │
│  Views → Forms → Templates         │
│  Models → Django ORM                │
└────────────────┬────────────────────┘
                 │ SQL
┌────────────────▼────────────────────┐
│          MySQL Database             │
│  7 tables, 5 Django apps            │
└─────────────────────────────────────┘
```

### Application Modules

```
MRAS Eco
├── accounts       → Authentication (Login, Register, Logout, Dashboard)
├── patients       → Patient Records (CRUD + Search)
├── doctors        → Doctor Directory (CRUD + Active/Inactive Status)
├── consultation   → Consultations + Inline Prescriptions + FEFO Dispensing
└── inventory      → Medicine Catalog + Batch Stock + Expiry Tracking + Alerts
```

---

## 🎓 Academic Context

**Institution:** University of Vocational Technology (UOVT)  
**Department:** Software and Intelligent Systems  
**Module:** IT304040 Python Programming — Final Group Project  
**Year:** 2026

### Team Members

| Member | ID | Role |
|--------|----|------|
| **L.B. Charith Jeewan** | SIS/24/B2/36 | PM / Scrum Master |
| **W.I.L. Withana** | SIS/24/B2/38 | Domain Researcher |
| **H.K.G.V. Lakmali Koralage** | SIS/24/B2/13 | QA & Documentation |
| **G.B.D. Darsha Anuradha** | SIS/24/B2/15 | Lead Backend Developer |
| **B.W.S.S. Nawarathna** | SIS/24/B2/39 | Lead Frontend Developer |

---

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- MySQL 8.0+
- Git

### Installation

```bash
# 1. Clone repository
git clone https://github.com/darshaanuradha/MRAS-Eco.git
cd MRAS-Eco

# 2. Create & activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
cd mras
pip install -r requirements.txt

# 4. Configure environment
cd ..
copy .env.example .env         # Windows
# cp .env.example .env         # macOS/Linux
# Edit .env with your database credentials

# 5. Setup database
cd mras
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Run server
python manage.py runserver
```

### Access

| URL | Page |
|-----|------|
| http://127.0.0.1:8000/ | Dashboard |
| http://127.0.0.1:8000/login/ | Login |
| http://127.0.0.1:8000/register/ | Register |
| http://127.0.0.1:8000/admin/ | Django Admin |

---

## 💾 Database Schema

### Entity Relationship Diagram

```
Patient (1) ──── (M) Consultation (M) ──── (1) Doctor
                          │
                          │ 1:M
                          ▼
                   PrescriptionItem
                     │          │
                M:1  │          │ 1:M
                     ▼          ▼
                 Medicine    PrescriptionAllocation
                     │                │
                1:M  │           M:1  │
                     ▼                ▼
                 Inventory ◄──────────┘
                  (Batch)
```

### Models Summary

| Model | Key Fields | Purpose |
|-------|-----------|---------|
| **Patient** | name, age, gender, contact, address, medical_history | Patient records |
| **Doctor** | full_name, specialization, phone, email, is_active | Doctor directory |
| **Consultation** | patient (FK), doctor (FK), diagnosis, notes, status | Clinical records |
| **Medicine** | name (unique), generic_name, strength, min/max_stock_level, unit_cost | Medicine catalog |
| **Inventory** | medicine (FK), batch_number (unique), expiry_date, current_stock | Batch-level stock |
| **PrescriptionItem** | consultation (FK), medicine (FK), quantity, dosage_instructions, duration_days | Prescribed medicines |
| **PrescriptionAllocation** | prescription_item (FK), inventory_batch (FK), quantity | Batch traceability |

---

## 💊 FEFO Algorithm — Key Feature

When a consultation is marked as **"Completed"**, the system automatically dispenses medicine using **First-Expired, First-Out**:

1. Queries all inventory batches for the prescribed medicine (sorted by `expiry_date ASC`)
2. Deducts from the **earliest-expiring batch first**
3. If one batch is insufficient, continues to the next batch
4. Creates `PrescriptionAllocation` records for full traceability
5. Entire operation wrapped in `transaction.atomic()` — rolls back on any failure

```python
# Simplified logic (see consultation/views.py for full implementation)
available_batches = Inventory.objects.filter(
    medicine=item.medicine, current_stock__gt=0
).order_by('expiry_date')  # ← FEFO: earliest expiry first

for batch in available_batches:
    take_qty = min(remaining_qty, batch.current_stock)
    batch.current_stock -= take_qty
    batch.save()
    PrescriptionAllocation.objects.create(...)
```

---

## 📁 Project Structure

```
MRAS-Eco/
├── .env.example                    # Environment template
├── .gitignore
├── README.md                       # This file
├── docs/                           # Documentation
│   ├── project_proposal.md         # Academic project proposal
│   ├── srs_document.md             # Software Requirements Specification
│   └── presentation.md             # Presentation slides & speaker notes
├── data/
├── tests/
└── mras/                           # Django Project Root
    ├── manage.py
    ├── requirements.txt
    ├── mras/                       # Project Configuration
    │   ├── settings.py             # Django settings (env-based config)
    │   ├── urls.py                 # Root URL router
    │   └── wsgi.py / asgi.py
    ├── accounts/                   # Auth module
    │   ├── views.py                # register, login, logout, home (dashboard)
    │   └── templates/              # login.html, register.html
    ├── patients/                   # Patient module
    │   ├── models.py               # Patient model
    │   ├── views.py                # CRUD + search views
    │   ├── forms.py                # PatientForm
    │   └── templates/patients/     # list, form, detail, confirm_delete
    ├── doctors/                    # Doctor module
    │   ├── models.py               # Doctor model
    │   ├── views.py                # CRUD views
    │   ├── forms.py                # DoctorForm
    │   └── templates/doctors/      # list, form, confirm_delete
    ├── consultation/               # Consultation module
    │   ├── models.py               # Consultation model
    │   ├── views.py                # CBVs + FEFO dispense_stock()
    │   ├── forms.py                # ConsultationForm + PrescriptionFormSet
    │   └── templates/              # list, form, print
    ├── inventory/                  # Inventory module
    │   ├── models.py               # Medicine, Inventory, PrescriptionItem, PrescriptionAllocation
    │   ├── views.py                # CRUD + stock views
    │   ├── forms.py                # MedicineForm, InventoryForm
    │   ├── context_processors.py   # Global notification alerts
    │   └── templates/              # inventory, stock_view, add/edit forms
    ├── static/
    │   ├── css/                    # Design system (6 CSS files)
    │   │   ├── variables.css       # Design tokens + dark mode
    │   │   ├── base.css            # Global styles
    │   │   ├── components.css      # Buttons, cards, tables, badges, etc.
    │   │   ├── layout.css          # Sidebar, topbar, auth layouts
    │   │   ├── animations.css      # Keyframes, transitions
    │   │   └── responsive.css      # 6 breakpoints (320px–1440px)
    │   └── js/
    │       └── main.js             # Sidebar, notifications, theme toggle
    └── templates/                  # Global templates
        ├── base.html               # Master layout
        ├── home.html               # Dashboard
        ├── sidebar.html            # Navigation
        └── components/
            └── footer.html
```

---

## 🔔 Notification System

A Django **context processor** runs on every authenticated request, injecting alert data globally:

| Alert Type | Trigger | Badge Color |
|-----------|---------|-------------|
| 🔴 **Expired** | `expiry_date < today` AND `current_stock > 0` | Red |
| 🔵 **Expiring Soon** | Expires within 30 days | Blue |
| 🟡 **Low Stock** | `total_stock ≤ min_stock_level` | Amber |

Notifications appear in a dropdown from the bell icon in the topbar, with clickable links to the relevant medicine's stock page.

---

## 🎨 Design System

The UI uses a custom CSS architecture with **100+ design tokens**:

- **Color Palette:** Cyan primary (#06B6D4), slate neutrals, semantic colors
- **Typography:** Inter font (Google Fonts), 5 weight levels
- **Components:** 6 button variants, cards, data tables, badges, stat cards, toasts, avatars, confirm dialogs
- **Animations:** Fade-in-up, hover-lift, staggered children, toast slides
- **Responsive:** 6 breakpoints from 320px to 1440px
- **Dark Mode:** Full theme toggle via CSS custom property scoping on `.dark` class

---

## 🔒 Security

| Feature | Implementation |
|---------|---------------|
| CSRF Protection | `{% csrf_token %}` on all forms |
| Password Hashing | Django PBKDF2 algorithm |
| Auth Guards | `@login_required` on all views |
| SQL Injection | Django ORM parameterized queries |
| XSS Protection | Django template auto-escaping |
| Secret Management | `python-dotenv` — credentials in `.env`, not source code |
| Data Integrity | `transaction.atomic()` for stock operations |
| Cascade Rules | CASCADE (patients), SET_NULL (doctors), RESTRICT (medicines) |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.10+ |
| **Framework** | Django 5.x |
| **Database** | MySQL 8.x |
| **ORM** | Django ORM |
| **Frontend** | HTML5, CSS3, Tailwind CSS (CDN) |
| **JavaScript** | Vanilla ES6+ |
| **Typography** | Google Fonts (Inter) |
| **Config** | python-dotenv |
| **VCS** | Git + GitHub |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Project Proposal](docs/project_proposal.md) | Problem statement, objectives, scope, architecture, timeline |
| [SRS Document](docs/srs_document.md) | 50+ functional requirements, data models, use cases (IEEE 830) |
| [Presentation](docs/presentation.md) | 20 slides with speaker notes + Q&A preparation |

---

## 🚀 Future Enhancements

- 📅 Appointment scheduling with calendar integration
- 📱 REST API via Django REST Framework for mobile app
- 📧 Email/SMS notifications for critical alerts
- 📊 Analytics dashboard with consumption trends
- 🏥 Multi-facility support
- 💳 Billing and invoice generation
- 🔑 Role-based access control (Doctor, Nurse, Pharmacist)

---

## 📄 License

This project was developed as an academic group project for the University of Vocational Technology (UOVT). All rights reserved by the project team.

---

<p align="center">
  Built with ❤️ using Python & Django
</p>