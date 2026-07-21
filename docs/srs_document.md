# Software Requirements Specification (SRS)
## Medical Room Automation System (MRAS Eco)

**Version:** 1.0  
**Date:** July 2026  
**Document Standard:** Based on IEEE 830-1998

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Overall Description](#2-overall-description)
3. [Functional Requirements](#3-functional-requirements)
4. [Non-Functional Requirements](#4-non-functional-requirements)
5. [Data Model Specification](#5-data-model-specification)
6. [Interface Requirements](#6-interface-requirements)
7. [Use Case Descriptions](#7-use-case-descriptions)
8. [System Constraints](#8-system-constraints)
9. [Assumptions & Dependencies](#9-assumptions--dependencies)

---

## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) describes the functional and non-functional requirements for the **Medical Room Automation System (MRAS Eco)** — a web-based application for managing medical room operations including patient records, doctor directories, consultations with prescriptions, and pharmaceutical inventory tracking with automated stock management.

### 1.2 Scope

MRAS Eco is a Django-based web application that provides:

- Staff authentication (registration, login, logout)
- Patient records management (CRUD operations with search)
- Doctor directory management (CRUD with active/inactive status tracking)
- Consultation management with inline prescription creation
- Automated inventory deduction using FEFO (First-Expired, First-Out) algorithm
- Batch-level pharmaceutical stock tracking with expiry monitoring
- Real-time notification system for expired, expiring, and low-stock medicines
- Dashboard with key performance indicators (KPIs)
- Printable prescription/consultation reports
- Responsive design with light/dark theme toggle

### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|-----------|
| MRAS | Medical Room Automation System |
| CRUD | Create, Read, Update, Delete |
| FEFO | First-Expired, First-Out (inventory management strategy) |
| MVT | Model-View-Template (Django's architecture pattern) |
| ORM | Object-Relational Mapping |
| KPI | Key Performance Indicator |
| FK | Foreign Key |
| SRS | Software Requirements Specification |

### 1.4 References

- Django Documentation v5.x — https://docs.djangoproject.com/
- IEEE 830-1998 — Recommended Practice for SRS
- WHO Guidelines on Pharmaceutical Inventory Management

---

## 2. Overall Description

### 2.1 Product Perspective

MRAS Eco is a standalone web application designed for use within a single medical facility. It operates on a client-server architecture where:

- **Server:** Django application serving HTML pages, processing business logic, and interfacing with a MySQL database.
- **Client:** Any modern web browser (Chrome, Firefox, Edge, Safari) on desktop or mobile devices.

### 2.2 Product Functions (Summary)

| ID | Function | Description |
|----|----------|-------------|
| F1 | User Authentication | Register, login, logout with session management |
| F2 | Dashboard | Real-time KPI cards, pending consultations, low stock alerts |
| F3 | Patient Management | Full CRUD + search for patient records |
| F4 | Doctor Management | Full CRUD with active/inactive status tracking |
| F5 | Consultation Management | Create/edit consultations with inline prescription formsets |
| F6 | Prescription Dispensing | FEFO-based automatic batch stock deduction |
| F7 | Inventory Management | Medicine catalog + batch-level stock + expiry tracking |
| F8 | Notification System | Alerts for expired, expiring, and low-stock medicines |
| F9 | Print Support | Printable consultation/prescription slips |
| F10 | Theme Support | Light/dark mode toggle with persistence |

### 2.3 User Classes and Characteristics

| User Class | Description | Access Level |
|-----------|-------------|--------------|
| Staff Member | Medical room attendants, nurses, or administrative staff | Full system access after authentication |
| Administrator | System administrator with Django admin panel access | Full access + Django admin |

### 2.4 Operating Environment

- **Server OS:** Windows / Linux / macOS
- **Python:** 3.10+
- **Django:** 5.x
- **Database:** MySQL 8.x
- **Browser:** Chrome 90+, Firefox 88+, Edge 90+, Safari 14+

---

## 3. Functional Requirements

### 3.1 Module: Accounts (Authentication)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-AUTH-01 | The system shall allow new users to register with first name, last name, email, and password. | High |
| FR-AUTH-02 | The system shall validate that passwords match during registration. | High |
| FR-AUTH-03 | The system shall prevent duplicate email registrations. | High |
| FR-AUTH-04 | The system shall authenticate users using email and password. | High |
| FR-AUTH-05 | The system shall redirect authenticated users to the dashboard. | High |
| FR-AUTH-06 | The system shall allow users to log out, destroying their session. | High |
| FR-AUTH-07 | The system shall restrict access to all pages (except login/register) for unauthenticated users. | High |
| FR-AUTH-08 | The system shall display success/error messages using Django's messages framework. | Medium |

---

### 3.2 Module: Dashboard

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-DASH-01 | The dashboard shall display the total number of registered patients. | High |
| FR-DASH-02 | The dashboard shall display the count of pending consultations. | High |
| FR-DASH-03 | The dashboard shall display the count of active doctors. | High |
| FR-DASH-04 | The dashboard shall display the count of low-stock medicines. | High |
| FR-DASH-05 | The dashboard shall show the 5 most recent pending consultations in a table. | Medium |
| FR-DASH-06 | The dashboard shall show all low-stock medicines with their current vs. minimum stock levels. | Medium |
| FR-DASH-07 | The dashboard shall greet the user by first name. | Low |

---

### 3.3 Module: Patients

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-PAT-01 | The system shall display a list of all patients in a searchable table. | High |
| FR-PAT-02 | The system shall allow adding a new patient with: name, age, gender, contact, address, and optional medical history. | High |
| FR-PAT-03 | The system shall display a detailed view of a patient's record. | High |
| FR-PAT-04 | The system shall allow editing an existing patient's information. | High |
| FR-PAT-05 | The system shall allow deleting a patient with a confirmation dialog. | High |
| FR-PAT-06 | The system shall support searching patients by name (case-insensitive). | Medium |

---

### 3.4 Module: Doctors

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-DOC-01 | The system shall display a directory of all doctors. | High |
| FR-DOC-02 | The system shall allow adding a doctor with: full name, specialization, phone, email, and active status. | High |
| FR-DOC-03 | The system shall allow editing a doctor's information. | High |
| FR-DOC-04 | The system shall allow deleting a doctor with a confirmation dialog. | High |
| FR-DOC-05 | The system shall visually distinguish active and inactive doctors using status badges. | Medium |
| FR-DOC-06 | The system shall auto-record created and updated timestamps. | Low |

---

### 3.5 Module: Consultations & Prescriptions

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-CON-01 | The system shall display a list of all consultations with patient name, doctor name, date, and status. | High |
| FR-CON-02 | The system shall allow creating a new consultation with patient, doctor, status, diagnosis, and notes. | High |
| FR-CON-03 | The system shall allow adding multiple prescription items (medicines) as inline formsets within a consultation. | High |
| FR-CON-04 | Each prescription item shall specify: medicine, quantity, dosage instructions, and duration in days. | High |
| FR-CON-05 | The system shall validate that prescribed quantity does not exceed available inventory stock. | High |
| FR-CON-06 | When a consultation status is set to "Completed", the system shall automatically deduct stock from inventory using the FEFO algorithm. | **Critical** |
| FR-CON-07 | The FEFO algorithm shall select inventory batches in ascending order of expiry date, deducting from the earliest-expiring batch first. | **Critical** |
| FR-CON-08 | The system shall create `PrescriptionAllocation` records to track which batch supplied which prescription. | High |
| FR-CON-09 | The system shall prevent re-dispensing stock for already-dispensed prescriptions. | High |
| FR-CON-10 | The system shall allow editing existing consultations and their prescriptions. | High |
| FR-CON-11 | The system shall provide a printable prescription view. | Medium |
| FR-CON-12 | All consultation saves shall be wrapped in database transactions for data integrity. | High |

---

### 3.6 Module: Inventory

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-INV-01 | The system shall maintain a medicine catalog with: name, generic name, manufacturer, dosage form, strength, unit cost, and min/max stock levels. | High |
| FR-INV-02 | The system shall allow adding, editing, and deleting medicines from the catalog. | High |
| FR-INV-03 | The system shall track inventory at the batch level with: batch number, expiry date, and current stock. | High |
| FR-INV-04 | The system shall allow adding new stock batches to an existing medicine. | High |
| FR-INV-05 | The system shall display the total aggregated stock across all batches for each medicine. | High |
| FR-INV-06 | The system shall color-code stock levels (red for low stock, green for normal). | Medium |
| FR-INV-07 | The system shall allow searching medicines by name in the inventory view. | Medium |
| FR-INV-08 | Medicine names shall be unique in the catalog. | High |
| FR-INV-09 | Batch numbers shall be unique across all inventory records. | High |

---

### 3.7 Module: Notification System

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-NOT-01 | The system shall display a notification badge in the top navigation showing the total count of alerts. | High |
| FR-NOT-02 | The system shall alert for expired medicine batches (expiry date < today, stock > 0). | High |
| FR-NOT-03 | The system shall alert for batches expiring within the next 30 days. | High |
| FR-NOT-04 | The system shall alert for medicines where total stock ≤ minimum stock level. | High |
| FR-NOT-05 | The notification dropdown shall categorize alerts by type (expired, expiring, low stock) with distinct color coding. | Medium |
| FR-NOT-06 | Clicking a notification shall navigate to the relevant medicine's stock detail page. | Medium |
| FR-NOT-07 | The system shall allow marking all notifications as read (persisted in localStorage). | Low |

---

## 4. Non-Functional Requirements

| ID | Category | Requirement |
|----|----------|-------------|
| NFR-01 | **Performance** | Pages shall load within 3 seconds on a standard broadband connection. |
| NFR-02 | **Performance** | Database queries shall use indexing on frequently searched fields (medicine name, batch number, expiry date, patient name). |
| NFR-03 | **Security** | All forms shall include CSRF protection tokens. |
| NFR-04 | **Security** | Passwords shall be hashed using Django's default PBKDF2 algorithm. |
| NFR-05 | **Security** | Sensitive configuration (SECRET_KEY, database credentials) shall be stored in environment variables, not source code. |
| NFR-06 | **Usability** | The UI shall be responsive and usable on devices with screen widths from 320px to 1440px. |
| NFR-07 | **Usability** | The system shall support light and dark themes with user preference persistence. |
| NFR-08 | **Reliability** | Stock deduction operations shall use database transactions to prevent partial updates. |
| NFR-09 | **Maintainability** | The codebase shall follow Django's app-based modular architecture with separated concerns. |
| NFR-10 | **Compatibility** | The application shall work on Chrome 90+, Firefox 88+, Edge 90+, and Safari 14+. |
| NFR-11 | **Data Integrity** | Deleting a medicine that has been prescribed shall be restricted (on_delete=RESTRICT). |
| NFR-12 | **Data Integrity** | Deleting a patient shall cascade-delete their consultations. |
| NFR-13 | **Data Integrity** | Deleting a doctor shall set related consultations' doctor field to NULL (SET_NULL). |

---

## 5. Data Model Specification

### 5.1 Patient

| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key, Auto-increment |
| name | CharField(255) | Required, Indexed |
| age | IntegerField | Required |
| gender | CharField(10) | Required |
| contact | CharField(20) | Required |
| address | TextField | Required |
| medical_history | TextField | Optional (blank, null) |

### 5.2 Doctor

| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key, Auto-increment |
| full_name | CharField(150) | Required |
| specialization | CharField(100) | Required |
| phone_number | CharField(20) | Optional |
| email | EmailField | Optional |
| is_active | BooleanField | Default: True |
| created_at | DateTimeField | Auto (on create) |
| updated_at | DateTimeField | Auto (on update) |

### 5.3 Consultation

| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key, Auto-increment |
| patient | ForeignKey → Patient | CASCADE on delete |
| doctor | ForeignKey → Doctor | SET_NULL on delete, nullable |
| consultation_date | DateTimeField | Auto (on create) |
| diagnosis | TextField | Required |
| notes | TextField | Optional |
| status | CharField(15) | Choices: Pending/Completed/Cancelled, Default: Pending |

### 5.4 Medicine

| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key, Auto-increment |
| name | CharField(100) | Required, Unique, Indexed |
| generic_name | CharField(100) | Required, Indexed |
| manufacturer | CharField(100) | Optional |
| dosage_form | CharField(50) | Optional |
| strength | CharField(50) | Optional |
| min_stock_level | IntegerField | Default: 20 |
| max_stock_level | IntegerField | Default: 500 |
| unit_cost | DecimalField(10,2) | Optional |
| created_at | DateTimeField | Auto (on create) |

### 5.5 Inventory (Batch)

| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key, Auto-increment |
| medicine | ForeignKey → Medicine | CASCADE on delete |
| batch_number | CharField(50) | Unique, Indexed |
| expiry_date | DateField | Required, Indexed |
| current_stock | PositiveIntegerField | Required |
| date_added | DateTimeField | Auto (on create) |

### 5.6 PrescriptionItem

| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key, Auto-increment |
| consultation | ForeignKey → Consultation | CASCADE on delete |
| medicine | ForeignKey → Medicine | RESTRICT on delete |
| quantity | PositiveIntegerField | Required |
| dosage_instructions | CharField(255) | Required |
| duration_days | IntegerField | Optional |

### 5.7 PrescriptionAllocation

| Field | Type | Constraints |
|-------|------|-------------|
| id | BigAutoField | Primary Key, Auto-increment |
| prescription_item | ForeignKey → PrescriptionItem | CASCADE on delete |
| inventory_batch | ForeignKey → Inventory | RESTRICT on delete |
| quantity | PositiveIntegerField | Required |

---

## 6. Interface Requirements

### 6.1 User Interface

| Page | URL | Key Elements |
|------|-----|-------------|
| Login | `/login/` | Email + password fields, split-screen layout |
| Register | `/register/` | First/last name, email, password, confirm password |
| Dashboard | `/` | 4 KPI cards, consultation table, low stock table |
| Patient List | `/patients/` | Searchable data table, Add button |
| Patient Form | `/patients/add/`, `/patients/<id>/edit/` | Multi-field form in card layout |
| Patient Detail | `/patients/<id>/` | Read-only detail grid with avatar |
| Doctor List | `/doctors/` | Data table with status badges |
| Doctor Form | `/doctors/new/`, `/doctors/<id>/edit/` | Multi-field form |
| Consultation List | `/consultation/` | Data table with status badges |
| Consultation Form | `/consultation/new/`, `/consultation/<id>/edit/` | Two-card layout with inline formset |
| Consultation Print | `/consultation/<id>/print/` | Print-optimized view |
| Inventory | `/inventory/` | Searchable data table with stock color coding |
| Stock View | `/inventory/stock/view/<id>/` | Batch list with expiry badges |
| Medicine Form | `/inventory/medicine/add/`, `/inventory/medicine/edit/<id>/` | Form in card layout |
| Stock Form | `/inventory/stock/add/<id>/` | Batch entry form |

### 6.2 Hardware Interface
- No specialized hardware required. Standard computer with web browser and network connectivity.

### 6.3 Software Interface
- **Database:** MySQL 8.x via Django ORM
- **Authentication:** Django's built-in `auth` module

---

## 7. Use Case Descriptions

### UC-01: Register a New Staff Account

| Field | Description |
|-------|-------------|
| **Actor** | Unregistered User |
| **Precondition** | User is on the registration page |
| **Main Flow** | 1. User enters first name, last name, email, password, confirm password. 2. System validates input. 3. System creates a new User account. 4. System redirects to login page with success message. |
| **Alternate Flow** | 2a. Passwords don't match → Error message, stay on page. 2b. Email already exists → Error message, stay on page. |
| **Postcondition** | A new user account exists in the database. |

### UC-02: Create a Consultation with Prescriptions

| Field | Description |
|-------|-------------|
| **Actor** | Authenticated Staff Member |
| **Precondition** | At least one patient and one doctor exist in the system |
| **Main Flow** | 1. Staff selects patient, doctor, sets status, enters diagnosis. 2. Staff adds one or more prescription items (medicine, quantity, dosage, duration). 3. Staff submits the form. 4. System validates stock availability. 5. System saves consultation + prescriptions in a transaction. 6. If status = "Completed", system runs FEFO dispensing. |
| **Alternate Flow** | 4a. Prescribed quantity exceeds available stock → Error message, form re-displayed. 6a. Insufficient stock during FEFO → Transaction rolled back, error shown. |
| **Postcondition** | Consultation record exists. If completed, inventory is deducted and allocation records created. |

### UC-03: FEFO Stock Dispensing

| Field | Description |
|-------|-------------|
| **Actor** | System (triggered automatically) |
| **Precondition** | Consultation status set to "Completed" |
| **Main Flow** | 1. For each PrescriptionItem: 2. System queries inventory batches ordered by expiry_date ASC. 3. System deducts stock from earliest-expiring batch first. 4. If one batch is insufficient, continues to next batch. 5. Creates PrescriptionAllocation for each deduction. |
| **Alternate Flow** | 3a. Total available stock < prescribed qty → ValueError raised, transaction rolled back. |
| **Postcondition** | Inventory batch `current_stock` values reduced. PrescriptionAllocation records created. |

---

## 8. System Constraints

1. The system requires a MySQL database server running on port 3306.
2. The application uses Django's built-in `User` model for authentication (not a custom user model).
3. The email field is used as the username for authentication.
4. All datetime values are stored in UTC timezone.
5. The notification system runs synchronously via Django context processors on every authenticated request.

---

## 9. Assumptions & Dependencies

### Assumptions
1. Users have access to a modern web browser with JavaScript enabled.
2. Only authorized staff members will have access to the system.
3. One medical facility operates one instance of MRAS Eco.
4. Medicine names in the catalog are unique identifiers.

### Dependencies
1. Python 3.10+ runtime environment
2. MySQL 8.x database server
3. Django 5.x framework and its dependencies
4. `python-dotenv` for environment variable management
5. Network connectivity for Tailwind CSS CDN and Google Fonts
6. `mysqlclient` or `PyMySQL` database adapter
