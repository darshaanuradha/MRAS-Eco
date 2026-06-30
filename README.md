# MRAS Eco

MRAS Eco is a Django-based medical room automation project for managing authentication, patients, inventory, and staff-facing dashboard pages.

## Current Status

The project currently includes:

- User authentication: register, login, logout, and dashboard access
- Shared UI shell with sidebar, top-level layout, and toast messages
- Pages for patients, inventory, and doctors
- A dashboard home page
- A root `.gitignore` for Python and Django development files

Some areas are still scaffolded and ready for further development, including richer models, forms, tests, and business logic for the app modules.

## Project Structure

```text
MRAS-Eco/
├── README.md
├── .gitignore
├── requirements.txt
├── mras/
│   ├── manage.py
│   ├── mydb.py
│   ├── accounts/
│   ├── doctors/
│   ├── inventory/
│   ├── patients/
│   ├── templates/
│   └── mras/
└── data/
```

## Prerequisites

- Python 3.10 or newer
- Git
- A virtual environment tool such as `venv`
- MySQL if you want to use the current database settings

## Clone and Start Development

### 1. Clone the repository

```bash
git clone https://github.com/darshaanuradha/MRAS-Eco.git
cd MRAS-Eco
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Install from the root requirements file:

```bash
pip install -r requirements.txt
```

If you are working inside the `mras` folder and using its local requirements file, you can install that too:

```bash
pip install -r mras/requirements.txt
```

### 4. Configure the database

The current Django settings use MySQL with the following values in `mras/mras/settings.py`:

- Database name: `mras`
- User: `root`
- Password: empty
- Host: `localhost`
- Port: `3306`

If your local MySQL setup is different, update the database settings before running migrations.

You can also use the helper script in `mras/mydb.py` to create the database if needed.

### 5. Run migrations

From the folder that contains `manage.py`:

```bash
cd mras
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Common Django Commands

Run these from the `mras` directory where `manage.py` lives.

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp <app_name>
python manage.py check
python manage.py shell
python manage.py test
```

## Apps Included

- `accounts`: authentication and dashboard access
- `patients`: patient page and future patient data handling
- `inventory`: inventory page and future stock tracking
- `doctors`: doctor module scaffold

## Useful Development Notes

- The main templates are in `mras/templates/`.
- App-specific templates are stored inside each app under `templates/`.
- `base.html` controls the shared layout and sidebar.
- `home.html` is the main dashboard page.
- `sidebar.html` contains the navigation menu used across the UI.

## Next Steps For Contributors

If you are a new developer joining the project, the recommended next tasks are:

1. Add proper models for patients, inventory, and doctors.
2. Create forms and CRUD views for those modules.
3. Add unit tests for auth and app workflows.
4. Improve the dashboard with live counts from the database.
5. Review the database settings and make them environment-based for safer local setup.

## Troubleshooting

- If `python manage.py` fails, make sure you are inside the `mras` folder.
- If Django cannot be imported, activate your virtual environment and install dependencies again.
- If MySQL errors appear, confirm the database exists and your credentials in `settings.py` are correct.

## License

No license has been added yet.