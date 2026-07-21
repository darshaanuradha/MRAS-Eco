# Project Proposal
## Medical Room Automation System (MRAS Eco)

**Module:** Python Programming  
**Academic Year:** 2025/2026  
**Date:** July 2026

---

## 1. Introduction

The **Medical Room Automation System (MRAS Eco)** is a web-based healthcare management platform designed to digitize and streamline the day-to-day operations of a medical facility's front office. The system replaces traditional paper-based workflows for patient registration, doctor management, consultation recording, prescription handling, and pharmaceutical inventory tracking with a unified, modern web application.

MRAS Eco is built with the **Django** web framework (Python) and uses a **MySQL** relational database, following the Model-View-Template (MVT) architectural pattern. The application provides role-based access through Django's built-in authentication system, ensuring data security and user accountability.

---

## 2. Problem Statement

Small to medium-sized medical facilities (clinics, university medical rooms, dispensaries) often rely on:

- **Paper-based patient records** that are prone to loss, duplication, and difficulty in retrieval.
- **Manual inventory tracking** of medicines using logbooks, leading to expired medicines going unnoticed and stock-outs during critical times.
- **Handwritten prescriptions** that lack traceability to inventory, making it impossible to track which batch of medicine was dispensed to which patient.
- **No real-time alerts** for low stock levels or upcoming expiry dates, resulting in wastage and patient safety risks.

These inefficiencies lead to **delayed patient care**, **medicine wastage**, **regulatory non-compliance**, and **poor resource utilization**.

---

## 3. Objectives

### Primary Objectives
1. **Digitize Patient Management** — Provide a complete CRUD system for patient records with searchable directories.
2. **Automate Consultation Workflow** — Enable doctors to create consultations with inline prescriptions that are directly linked to inventory.
3. **Implement Smart Inventory Control** — Track medicines at the batch level with expiry dates, and automatically deduct stock using the FEFO (First-Expired, First-Out) algorithm when prescriptions are completed.
4. **Provide Real-Time Notifications** — Alert staff about expired medicines, soon-to-expire batches (within 30 days), and low-stock items via a persistent notification system.

### Secondary Objectives
5. Build a responsive, modern UI that works on desktop and mobile devices.
6. Implement user authentication with registration and login functionality.
7. Support dark mode and light mode for user accessibility preferences.
8. Generate printable prescription slips for patient records.

---

## 4. Scope

### In Scope
| Feature | Description |
|---------|-------------|
| User Authentication | Register, Login, Logout with session-based auth |
| Patient Management | Add, View, Edit, Delete, Search patient records |
| Doctor Management | Add, Edit, Delete doctors with active/inactive status |
| Consultation System | Create/Edit consultations with inline prescription formsets |
| Prescription Dispensing | FEFO-based automatic stock deduction on consultation completion |
| Inventory Management | Medicine catalog, batch-level stock tracking, expiry management |
| Search & Filtering | Patient search, Inventory search |
| Notification System | Real-time alerts for expired/expiring/low-stock medicines |
| Dashboard | KPI cards, pending consultations, low stock overview |
| Print Support | Printable prescription/consultation slips |
| Theme Support | Light mode and Dark mode toggle |

### Out of Scope (Future Enhancements)
- Appointment scheduling and calendar integration
- Electronic health records (EHR) compliance
- Multi-branch/multi-facility support
- SMS/Email notification delivery
- Billing and payment processing
- REST API for mobile app integration

---

## 5. Methodology

The project follows an **Agile-Iterative** development methodology:

1. **Requirements Gathering** — Identified key pain points in medical room operations through research and analysis.
2. **System Design** — Designed the ER diagram, defined models and relationships, planned URL routing and views.
3. **Iterative Development** — Built the system module-by-module:
   - Sprint 1: Project setup, Authentication, Patient module
   - Sprint 2: Doctor module, Consultation module with prescriptions
   - Sprint 3: Inventory module with batch tracking and FEFO logic
   - Sprint 4: Dashboard, Notifications, UI/UX redesign
4. **Testing & Refinement** — Tested each module for functional correctness, data integrity, and UI responsiveness.
5. **Deployment Preparation** — Configured environment variables, static file handling, and production settings.

---

## 6. System Architecture

### 6.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Client (Browser)                  │
│    HTML/CSS/JavaScript + Tailwind CSS Framework      │
└──────────────────────┬──────────────────────────────┘
                       │ HTTP Request/Response
┌──────────────────────▼──────────────────────────────┐
│              Django Web Framework (MVT)              │
│  ┌──────────┐  ┌──────────┐  ┌────────────────────┐ │
│  │  Views   │  │  Forms   │  │     Templates      │ │
│  │ (Logic)  │──│(Validate)│──│ (HTML Rendering)   │ │
│  └────┬─────┘  └──────────┘  └────────────────────┘ │
│       │                                              │
│  ┌────▼─────┐  ┌──────────────────────────────────┐ │
│  │  Models  │──│  Django ORM (Object Relational   │ │
│  │ (Schema) │  │  Mapping)                        │ │
│  └──────────┘  └──────────────┬───────────────────┘ │
└───────────────────────────────┼─────────────────────┘
                                │ SQL Queries
                       ┌────────▼────────┐
                       │  MySQL Database │
                       └─────────────────┘
```

### 6.2 Application Modules

```
MRAS Eco
├── accounts       → Authentication (Login, Register, Logout, Dashboard)
├── patients       → Patient Records (CRUD + Search)
├── doctors        → Doctor Directory (CRUD + Active/Inactive Status)
├── consultation   → Consultations + Inline Prescriptions + FEFO Dispensing
└── inventory      → Medicine Catalog + Batch Stock + Expiry Tracking + Alerts
```

### 6.3 Entity-Relationship Diagram

```
┌──────────┐     1:M      ┌───────────────┐     M:1      ┌──────────┐
│  Patient  │─────────────▶│ Consultation  │◀─────────────│  Doctor   │
└──────────┘               └───────┬───────┘               └──────────┘
                                   │ 1:M
                           ┌───────▼───────────┐
                           │ PrescriptionItem  │
                           └───────┬───────────┘
                          M:1     │      │ 1:M
                    ┌─────────────┘      └──────────────┐
            ┌───────▼──────┐              ┌─────────────▼──────────┐
            │   Medicine   │              │ PrescriptionAllocation │
            └───────┬──────┘              └─────────────┬──────────┘
                    │ 1:M                               │ M:1
            ┌───────▼──────┐                            │
            │  Inventory   │◀───────────────────────────┘
            │   (Batch)    │
            └──────────────┘
```

---

## 7. Technologies Used

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Backend** | Python | 3.x | Core programming language |
| **Framework** | Django | 5.x | Web framework (MVT pattern) |
| **Database** | MySQL | 8.x | Relational data storage |
| **ORM** | Django ORM | Built-in | Database abstraction layer |
| **Frontend** | HTML5 / CSS3 | — | Page structure and styling |
| **CSS Framework** | Tailwind CSS | CDN | Utility-first responsive design |
| **JavaScript** | Vanilla JS | ES6+ | Client-side interactivity |
| **Font** | Google Fonts (Inter) | — | Modern typography |
| **Environment** | python-dotenv | — | Environment variable management |
| **Version Control** | Git + GitHub | — | Source code management |

---

## 8. Team Members

| Name | Role | Responsibilities |
|------|------|------------------|
| *[Member 1]* | Project Lead / Backend Developer | Architecture, Models, Views, Business Logic |
| *[Member 2]* | Frontend Developer | Templates, CSS, Responsive Design, Dark Mode |
| *[Member 3]* | Database / Testing | Database design, Data integrity, Testing |
| *[Member 4]* | Documentation / QA | SRS, Proposal, Presentation, User testing |

> ⚠️ **Note:** Update the table above with your actual team member names and roles.

---

## 9. Project Timeline

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| Requirements & Planning | Week 1–2 | Project proposal, ER diagram, wireframes |
| Core Development | Week 3–6 | Auth, Patient, Doctor, Consultation modules |
| Inventory & Notifications | Week 7–8 | Medicine catalog, batch tracking, FEFO, alerts |
| UI/UX Redesign | Week 9–10 | Design system, responsive templates, dark mode |
| Testing & Documentation | Week 11–12 | SRS, bug fixes, presentation preparation |
| Final Presentation | Week 13 | Demo and defense |

---

## 10. Expected Outcomes

1. A fully functional web application managing patients, doctors, consultations, prescriptions, and inventory.
2. Automated inventory control with FEFO dispensing and real-time stock alerts.
3. A modern, responsive UI with dark/light mode support.
4. Documentation including Project Proposal, SRS, and Presentation materials.
5. Source code hosted on GitHub with proper version control history.

---

## 11. References

1. Django Documentation — https://docs.djangoproject.com/
2. Tailwind CSS Documentation — https://tailwindcss.com/docs
3. MySQL Documentation — https://dev.mysql.com/doc/
4. Python Official Documentation — https://docs.python.org/3/
5. WHO Guidelines on Medicine Inventory Management — https://www.who.int/
