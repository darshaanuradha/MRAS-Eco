# MRAS Eco — Presentation Slides
## Medical Room Automation System

> 🎯 **How to use this:** Each `## Slide X` section below represents one presentation slide. Copy the content into PowerPoint, Google Slides, or Canva. The **Speaker Notes** under each slide tell you what to say.

---

## Slide 1 — Title Slide

### MRAS Eco
#### Medical Room Automation System

**Module:** Python Programming  
**Group:** *[Your Group Name]*  
**Members:** *[List names]*  
**Date:** July 2026

**Speaker Notes:**  
"Good morning/afternoon. We are presenting MRAS Eco — a Medical Room Automation System built with Python and the Django web framework. Our system digitizes the entire workflow of a medical room — from patient registration to prescription dispensing and inventory management."

---

## Slide 2 — Problem Statement

### ❌ The Problem

- 📋 Paper-based patient records → Loss, duplication, hard to search
- 💊 Manual medicine tracking → Expired medicines go unnoticed
- 📝 Handwritten prescriptions → No traceability to inventory batches
- ⚠️ No alerts → Stock-outs during critical times, medicine wastage
- 🐌 Slow operations → Delayed patient care

> **Impact:** Patient safety risks, medicine wastage, regulatory non-compliance

**Speaker Notes:**  
"Most small clinics and university medical rooms still use paper-based systems. This leads to several problems: patient files get lost, expired medicines sit on shelves because nobody tracks expiry dates, and when a doctor prescribes medicine, there's no way to know if it's even in stock. We built MRAS Eco to solve these problems."

---

## Slide 3 — Our Solution

### ✅ MRAS Eco — What It Does

| Module | Capability |
|--------|-----------|
| 🏥 **Patients** | Digital records with search |
| 👨‍⚕️ **Doctors** | Directory with active/inactive status |
| 📋 **Consultations** | Record diagnosis + prescriptions |
| 💊 **Inventory** | Batch-level stock with expiry tracking |
| 🔔 **Notifications** | Alerts for expired, expiring & low-stock |
| 📊 **Dashboard** | Real-time KPIs at a glance |

**Speaker Notes:**  
"Our solution is a web-based application with 5 core modules. The key differentiator is that consultations are directly linked to inventory — when a doctor prescribes medicine, the system automatically checks stock and deducts it from the correct batch."

---

## Slide 4 — Objectives

### 🎯 Project Objectives

1. **Digitize** patient and doctor management with full CRUD operations
2. **Automate** consultation-to-inventory workflow with inline prescriptions
3. **Implement FEFO** — First-Expired, First-Out stock deduction algorithm
4. **Real-time alerts** for expired, expiring, and low-stock medicines
5. **Modern UI** — Responsive design with dark/light mode support
6. **Data integrity** — Database transactions for critical operations

**Speaker Notes:**  
"We had 6 key objectives. The most technically challenging was objective 3 — implementing the FEFO algorithm, which automatically selects the medicine batch closest to expiry when dispensing. This is the same strategy used in real pharmaceutical warehouses."

---

## Slide 5 — System Architecture

### 🏗️ Architecture Overview

```
┌──────────────────────────┐
│    Browser (Client)      │
│  HTML + CSS + JavaScript │
└────────────┬─────────────┘
             │ HTTP
┌────────────▼─────────────┐
│    Django Framework      │
│  ┌────┐ ┌────┐ ┌──────┐ │
│  │View│→│Form│→│Templ.│ │
│  └──┬─┘ └────┘ └──────┘ │
│     │                    │
│  ┌──▼──┐  ┌───────────┐ │
│  │Model│──│ Django ORM │ │
│  └─────┘  └─────┬─────┘ │
└─────────────────┼────────┘
           ┌──────▼──────┐
           │    MySQL     │
           │   Database   │
           └─────────────┘
```

**Speaker Notes:**  
"We use Django's MVT — Model View Template — pattern. The user interacts with the browser, which sends HTTP requests to Django. Views contain business logic, Forms handle validation, and Templates render the HTML response. Models define our database schema, and Django's ORM translates Python code to SQL queries against our MySQL database."

---

## Slide 6 — ER Diagram

### 📐 Entity Relationship Diagram

```
Patient (1) ──────────── (M) Consultation (M) ──────────── (1) Doctor
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

**7 Tables:** Patient, Doctor, Consultation, Medicine, Inventory, PrescriptionItem, PrescriptionAllocation

**Speaker Notes:**  
"Our database has 7 tables. The most important relationships are: a Patient has many Consultations, each Consultation has many PrescriptionItems, and each PrescriptionItem connects to a Medicine. When dispensed, PrescriptionAllocations track exactly which inventory batch supplied each prescription. This gives us full traceability — we can answer: 'which batch of paracetamol did patient X receive on date Y?'"

---

## Slide 7 — Technology Stack

### 🛠️ Technologies Used

| Layer | Technology | Why We Chose It |
|-------|-----------|----------------|
| **Language** | Python 3.x | Module requirement, readability, extensive libraries |
| **Framework** | Django 5.x | Built-in ORM, auth, admin, forms — rapid development |
| **Database** | MySQL 8.x | Industry-standard relational DB, ACID compliance |
| **Frontend** | Tailwind CSS + Custom CSS | Utility-first responsive design with design tokens |
| **JS** | Vanilla JavaScript | No framework overhead, handles sidebar, notifications, theme |
| **Fonts** | Google Fonts (Inter) | Modern, clean, professional typography |
| **VCS** | Git + GitHub | Collaboration and version control |
| **Config** | python-dotenv | Secure environment variable management |

**Speaker Notes:**  
"We chose Django because it's a Python framework with batteries included — authentication, ORM, admin panel, and form handling are all built-in. For the database, MySQL gives us ACID compliance which is critical for inventory transactions. For styling, we use a combination of Tailwind CSS utility classes and a custom design system with CSS custom properties."

---

## Slide 8 — Demo: Authentication

### 🔐 Authentication System

**Features:**
- Split-screen login page with branded gradient panel
- Registration with email-as-username pattern
- Password validation (match check, Django validators)
- Session-based authentication with `@login_required` protection
- Success/error toast notifications

**Demo Points:**
1. Show the login page design (split-screen with gradient)
2. Register a new account
3. Log in and show redirect to dashboard
4. Show that direct URL access is blocked when logged out

**Speaker Notes:**  
"Let me show the authentication system. Notice the split-screen design — the left panel shows our branding, the right panel has the form. We use Django's built-in User model but authenticate with email as the username. All protected pages redirect to login if the user isn't authenticated."

---

## Slide 9 — Demo: Dashboard

### 📊 Dashboard

**Features:**
- 4 KPI stat cards with icons and hover animations
- Pending consultations table (latest 5)
- Low stock medicines table with restock links
- Personalized greeting

**KPIs:**
- Total Patients | Pending Consultations | Low Stock Items | Active Doctors

**Speaker Notes:**  
"The dashboard gives staff an immediate overview of the facility. These 4 cards show real-time counts from the database — they update every time the page loads. Below that, we show the 5 most recent pending consultations and any medicines that need restocking."

---

## Slide 10 — Demo: Patient Management

### 👥 Patient Management

**Features:**
- Full CRUD: Add, View, Edit, Delete
- Search by name (case-insensitive)
- Patient detail page with avatar initial
- Delete confirmation dialog

**Key Code:** `Patient.objects.filter(name__icontains=query)`

**Speaker Notes:**  
"The patient module provides standard CRUD operations. The search bar filters patients by name using Django's `icontains` lookup — that's a case-insensitive LIKE query. Each patient has a detail page showing all their information, and deletion requires confirmation to prevent accidents."

---

## Slide 11 — Demo: Doctor Management

### 👨‍⚕️ Doctor Directory

**Features:**
- Doctor list with avatar initials and specialization
- Active/Inactive status badges (green/grey)
- Full CRUD operations
- Timestamps: `created_at`, `updated_at` (auto-managed)

**Key Design Decision:**  
`on_delete=SET_NULL` — Deleting a doctor doesn't delete their consultations; the doctor field becomes NULL.

**Speaker Notes:**  
"The doctor module manages the facility's medical staff. We use color-coded badges to show active vs inactive doctors. An important design decision: when a doctor is deleted, their existing consultation records are preserved — the doctor field just becomes null. We chose SET_NULL over CASCADE to protect historical medical data."

---

## Slide 12 — Demo: Consultation System

### 📋 Consultation + Prescriptions

**Features:**
- Two-section form: Details + Prescriptions
- **Inline Formset:** Add multiple medicines dynamically (JavaScript)
- Status workflow: Pending → Completed / Cancelled
- Stock validation before save

**Key Code:**
```python
PrescriptionFormSet = inlineformset_factory(
    Consultation, PrescriptionItem,
    form=PrescriptionItemForm,
    extra=1, can_delete=True
)
```

**Speaker Notes:**  
"This is the heart of the system. The consultation form has two sections — consultation details on top, and prescriptions below. Staff can add multiple medicines using the formset. The '+Add Medicine' button dynamically adds rows via JavaScript. When saved, the system validates that enough stock exists for each prescribed medicine."

---

## Slide 13 — FEFO Algorithm (★ Key Feature)

### 💊 FEFO: First-Expired, First-Out

> The **star feature** of MRAS Eco

```
When status = "Completed":
    For each prescribed medicine:
        1. Query batches WHERE current_stock > 0
           ORDER BY expiry_date ASC  ← earliest first
        
        2. Deduct from Batch 1 (soonest to expire)
           └─ If Batch 1 insufficient → continue to Batch 2
        
        3. Create PrescriptionAllocation records
           (tracks exactly which batch supplied how many units)
        
        4. All wrapped in transaction.atomic()
           └─ If anything fails → entire operation rolls back
```

**Speaker Notes:**  
"FEFO stands for First-Expired, First-Out. This is the same algorithm used in real pharmaceutical warehouses. When a consultation is completed, the system automatically picks the medicine batch closest to its expiry date and deducts from that first. If one batch doesn't have enough, it moves to the next. Every deduction is recorded in the PrescriptionAllocation table for full traceability. The entire operation is wrapped in a database transaction — if anything goes wrong, everything rolls back cleanly."

---

## Slide 14 — Demo: Inventory Management

### 📦 Inventory System

**Features:**
- Medicine catalog with search
- Batch-level stock tracking (batch number, expiry, quantity)
- Color-coded stock levels (🔴 red = low, 🟢 green = normal)
- Add new stock batches to existing medicines
- Total stock aggregation using `Sum()` annotation

**Key Code:**
```python
medicines = Medicine.objects.annotate(
    total_stock=Sum('inventory__current_stock')
)
```

**Speaker Notes:**  
"The inventory module has two layers. First, the Medicine catalog — this is the master list of all medicines. Second, the Inventory batches — each medicine can have multiple batches with different expiry dates and quantities. The total stock shown in the list is calculated on-the-fly using Django's Sum aggregation across all batches."

---

## Slide 15 — Demo: Notification System

### 🔔 Real-Time Alerts

**3 Alert Types:**

| Alert | Trigger | Color |
|-------|---------|-------|
| 🔴 Expired | `expiry_date < today` AND `stock > 0` | Red |
| 🔵 Expiring Soon | Expires within 30 days | Blue |
| 🟡 Low Stock | `total_stock ≤ min_stock_level` | Amber |

**Implementation:** Django Context Processor → runs on every authenticated request

**Speaker Notes:**  
"The notification system uses a Django context processor — a function that runs on every page load and injects alert data into every template. It checks for three conditions: expired batches still in stock, batches expiring in the next 30 days, and medicines below their minimum stock level. The red badge in the navbar shows the total count."

---

## Slide 16 — UI/UX Design System

### 🎨 Design System

**Before → After:** From basic Bootstrap-like templates to a professional healthcare SaaS platform

- **Design Tokens:** 100+ CSS custom properties (colors, spacing, shadows, radii)
- **Component Library:** Buttons (6 variants), cards, tables, badges, toasts, avatars
- **Typography:** Inter font family, 5 weight levels
- **Animations:** Fade-in-up, hover-lift, staggered children, toast slides
- **Responsive:** 6 breakpoints from 320px to 1440px
- **Dark Mode:** Full theme toggle with `localStorage` persistence
- **Color Palette:** Cyan primary (#06B6D4), slate neutrals, semantic colors

**Speaker Notes:**  
"We invested significant effort in the UI/UX. We built a complete design system from scratch with CSS custom properties. This ensures every page looks consistent. We have 6 button variants, standardized cards and tables, and micro-animations for a premium feel. The dark mode toggle switches all colors by overriding CSS custom properties on the root element."

---

## Slide 17 — Dark Mode

### 🌗 Light & Dark Mode

**Implementation:**
1. CSS custom properties in `:root` (light) and `.dark` scope
2. Toggle button in topbar (sun/moon icons)
3. Preference saved to `localStorage`
4. Anti-flash script in `<head>` loads theme before page render

*[Show a side-by-side comparison screenshot of light vs dark mode]*

**Speaker Notes:**  
"Dark mode was implemented using CSS custom property scoping. All our colors reference variables like `--bg-card` and `--text-heading`. When the `.dark` class is added to the HTML element, those variables get new values. We also have a small inline script in the head tag that applies the saved theme before the page renders, preventing the common 'flash of white' problem."

---

## Slide 18 — Challenges & Solutions

### 🧩 Challenges We Faced

| Challenge | Solution |
|-----------|----------|
| FEFO stock splitting across batches | Iterate through batches sorted by expiry, deduct progressively |
| Form validation + stock check atomicity | `transaction.atomic()` wrapping both form save and stock deduction |
| Dynamic formset rows in JavaScript | Clone empty form template, update `__prefix__` indices |
| Preventing re-dispensing on edit | Check `item.allocations.exists()` before dispensing |
| Notification performance on every request | Context processor with `select_related()` to minimize queries |
| Dark mode flash on page load | Inline `<script>` in `<head>` applies theme before render |

**Speaker Notes:**  
"We faced several technical challenges. The hardest was the FEFO algorithm — when a prescription needs 100 tablets but one batch only has 60, the system needs to take 60 from that batch and 40 from the next. We also had to ensure atomicity — if stock deduction fails midway, the entire consultation save must roll back. We solved this using Django's transaction.atomic decorator."

---

## Slide 19 — Future Enhancements

### 🚀 What's Next?

- 📅 **Appointment Scheduling** — Calendar-based booking for doctors
- 📱 **REST API** — Mobile app integration via Django REST Framework
- 📧 **Email/SMS Alerts** — Push notifications for critical stock events
- 📊 **Reports & Analytics** — Monthly consumption, prescription patterns
- 🏥 **Multi-Facility Support** — Branch-level inventory management
- 💳 **Billing Module** — Invoice generation and payment tracking
- 🔒 **Role-Based Access** — Separate permissions for doctors, nurses, pharmacists

**Speaker Notes:**  
"If we had more time, these are the features we would add next. The most impactful would be a REST API for mobile access and an analytics dashboard for consumption trend reporting."

---

## Slide 20 — Thank You & Q&A

### 🙏 Thank You!

**MRAS Eco** — Making Medical Rooms Smarter

📂 **Source Code:** github.com/darshaanuradha/MRAS-Eco  
🛠️ **Tech Stack:** Python • Django • MySQL • Tailwind CSS  
⭐ **Key Feature:** FEFO-based automated inventory management

---

### Questions?

**Speaker Notes:**  
"Thank you for your attention. We're happy to answer any questions. We can also do a live demo of any specific feature if you'd like to see it in action."

---

---

# 📝 Appendix: Likely Q&A Questions & Answers

Prepare for these questions from your evaluators:

### Q1: "Why did you choose Django over Flask?"
**A:** "Django provides built-in authentication, ORM, admin panel, form validation, and template engine out of the box. For a system with 7 database tables and complex relationships like ours, Django's 'batteries included' approach saved us significant development time compared to Flask where we'd need to add each component separately."

### Q2: "How does the FEFO algorithm handle insufficient stock?"
**A:** "If the total available stock across all batches is less than the prescribed quantity, the form validation catches it first — the PrescriptionItemForm.clean() method checks total stock before saving. If somehow it gets past validation, the dispense_stock function raises a ValueError, and since everything is inside transaction.atomic(), the entire operation rolls back."

### Q3: "Why MySQL instead of SQLite?"
**A:** "SQLite is fine for development but doesn't support concurrent write operations well. MySQL provides proper ACID compliance, concurrent access, and is an industry-standard choice for production healthcare applications. Our settings.py dynamically reads database credentials from environment variables, making it easy to switch environments."

### Q4: "How is the notification system implemented?"
**A:** "We use a Django context processor — a function registered in settings.py that runs on every authenticated request. It queries for three conditions: expired batches, batches expiring in 30 days, and low-stock medicines. The results are injected into every template's context, making the notification data available globally without modifying individual views."

### Q5: "What happens if you delete a patient who has consultations?"
**A:** "The Consultation model has `on_delete=CASCADE` for the patient foreign key, so deleting a patient cascades the deletion to all their consultations and prescription items. For doctors, we use `on_delete=SET_NULL` so consultation history is preserved even if a doctor leaves. For medicines, we use `on_delete=RESTRICT` to prevent deletion if any prescriptions reference that medicine."

### Q6: "How did you implement dark mode?"
**A:** "We defined all layout colors as CSS custom properties (variables). In the default `:root` scope, they have light values. Under a `.dark` selector, they're overridden with dark values. A JavaScript function toggles the `dark` class on the `<html>` element and saves the preference to `localStorage`. An inline script in the `<head>` applies the saved theme before the page renders, preventing a flash of light mode."

### Q7: "Is this system secure?"
**A:** "We implement several security measures: CSRF tokens on all forms, password hashing using Django's PBKDF2 algorithm, session-based authentication, @login_required decorators on all views, and sensitive configuration stored in environment variables using python-dotenv — never in source code."

### Q8: "What is the PrescriptionAllocation table for?"
**A:** "It provides batch-level traceability. When 100 tablets of paracetamol are prescribed and the system deducts 60 from Batch A and 40 from Batch B, PrescriptionAllocation records exactly which batches supplied how many units. This is crucial for pharmaceutical compliance — if a batch is recalled, we can identify every patient who received medicine from that batch."
