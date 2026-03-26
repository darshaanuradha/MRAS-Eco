# 🏥 MRAS Eco: Climate-Integrated Medical Room Automation System

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=flat&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat&logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap)

**Institution:** University of Vocational Technology (UOVT)  
**Module:** IT304040 Python Programming – Final Group Project  
**Domain:** Healthcare & Bio-Medical Informatics (Digital Health & Decarbonization)

---

## 🌍 Live Deployment

**Access the live application here:** `[Insert your Render or Railway URL here]`

---

## 📖 Project Overview

The **Medical Room Automation System (MRAS Eco)** is a secure, Python-based web application engineered to digitize and optimize corporate medical workflows. It transitions facilities from inefficient paper logbooks to a modular digital ecosystem.

MRAS Eco manages patient histories, automates pharmacy inventory deductions, and crucially, integrates real-time environmental surveillance to correlate local air quality metrics with respiratory clinical data.

## 🔍 The Problem & Research Gap

**The Gap:** Current corporate medical facilities lack an integrated digital platform that fuses environmental risk factors with patient workflow.

**The Problem:** Legacy medical rooms rely on disparate manual processes. Clinical inventory and consultation workflows operate entirely in isolation from environmental risk factors. This results in an inability to anticipate respiratory medicine shortages (e.g., inhalers running out during a drop in Air Quality) or logically correlate clinical incidence data with local climate metrics.

## ✨ Key Features & Architecture

The system utilizes a **Modular Monolith** architecture, strictly separating concerns into four core Django apps:

1. **🔐 Security & Auth (`users`):** Role-Based Access Control (RBAC) for Admins, Doctors, and Pharmacists.
2. **🩺 Clinical Domain (`patients`):** Manages secure electronic health records (EHR) and digital consultation logging.
3. **💊 Pharmacy Domain (`inventory`):** Real-time inventory ledger that automatically deducts stock upon prescription issuance.
4. **🌤️ Environmental Surveillance (`climate`):** Integrates an external Weather API to fetch real-time Air Quality Index (AQI) data.
   - **Dynamic Threshold Logic:** The system uses a dynamic multiplier to adjust minimum stock alerts based on daily AQI. If air quality is poor, the safety threshold for respiratory meds automatically increases, triggering a predictive dashboard warning before a stock-out occurs.

---

## ⚙️ Installation & Setup Instructions

To run this project locally, follow these steps:

### 1. Prerequisites

Ensure you have **Python 3.10+** and **Git** installed on your machine.

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/mras-eco.git](https://github.com/your-username/mras-eco.git)
cd mras-eco

3. Create and Activate a Virtual EnvironmentWindows:Bashpython -m venv venv
venv\Scripts\activate
macOS/Linux:Bashpython3 -m venv venv
source venv/bin/activate
4. Install DependenciesBashpip install -r requirements.txt
5. Environment Variables (API Key)Create a .env file in the project root (mras_core/.env) and add your OpenWeatherMap API key for the climate module:Code snippetWEATHER_API_KEY=your_api_key_here
DJANGO_SECRET_KEY=your_django_secret
DEBUG=True
6. Run Database MigrationsBashpython manage.py makemigrations
python manage.py migrate
7. Create a Superuser (Admin Account)Bashpython manage.py createsuperuser
(Follow the prompts to set a username, email, and password).8. Run the Development ServerBashpython manage.py runserver
Navigate to http://127.0.0.1:8000 in your browser to view the application.🖥️ Usage GuideAdmin Setup: Log in via http://127.0.0.1:8000/admin using your superuser credentials to populate initial data (add Medicines, register Staff Users).Patient Registration: Navigate to the Patients dashboard to register a new corporate employee into the system.Clinical Consultation: A user with the "Doctor" role can initiate a consultation, log a diagnosis, and prescribe medication.Inventory Automation: Upon saving the consultation, the system will automatically deduct the prescribed amount from the Inventory batch and fetch the daily AQI to check for dynamic stock warnings on the main dashboard.👥 Project Team (Agile Squad)This project was developed collaboratively over a 4-week sprint using the Agile Scrum framework.NameStudent IDProject RoleL.B. Charith JeewanSIS/24/B2/36Project Manager / Scrum MasterW.I.L. WithanaSIS/24/B2/38Domain ResearcherG.B.D. Darsha AnuradhaSIS/24/B2/15Lead Developer (Backend)B.W.S.S. NawarathnaSIS/24/B2/39Lead Developer (Frontend)H.K.G.V. Lakmali KoralageSIS/24/B2/13QA & Documentation Specialist
```

Day 1 Initialization Commands
Once you have saved that file, open your terminal. Here are the exact commands to build your virtual environment, install these dependencies, and generate the core Django project structure.

1. Create and activate the virtual environment:

Bash
python -m venv venv

# On Windows:

venv\Scripts\activate

# On Mac/Linux:

source venv/bin/activate 2. Install the pinned dependencies:

Bash
pip install -r requirements.txt 3. Initialize the core Django project:
Note: The period . at the end of the second command is extremely important. It tells Django to build the project in your current folder rather than creating an extra nested folder.

Bash
django-admin startproject mras_core . 4. Create the four modular apps:

Bash
python manage.py startapp users
python manage.py startapp patients
python manage.py startapp inventory
python manage.py startapp climate
