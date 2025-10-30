# LifeTimeApp

A small Django application for tracking and managing working time and related reports.

## Overview

LifeTimeApp is a Django-based project that provides user management, time tracking, and reporting features (adjust this description to match the project's actual scope). It includes the following Django apps (examples):

- `users` — user registration and profiles
- `working_time` — logging and reporting time entries

## Features

- User registration and authentication
- Time tracking and reporting
- Admin area (Django admin)

## Requirements

- Python 3.10+ (verify in `pyproject.toml` and adjust if needed)
- Virtual environment (venv) or Poetry recommended
- Database: SQLite (included as `db.sqlite3`) for development; Postgres/MySQL recommended for production

## Quick installation

Recommended: create and activate a virtual environment first.

1) Using venv + pip

```bash
python3 -m venv .venv
source .venv/bin/activate
# If you have a requirements.txt
pip install -r requirements.txt
# Or, if the project is built via pyproject.toml:
pip install -e .
```

2) Using Poetry

```bash
poetry install
poetry shell
```

## Configuration

Set environment variables (for example in a `.env` file or via your deployment system):

- `SECRET_KEY` — Django secret key
- `DEBUG` — `True` or `False`
- `DATABASE_URL` — if you use a database other than SQLite
- any other settings you need (email, allowed hosts, etc.)

Example `.env.example`:

```
SECRET_KEY=replace_this_with_a_secret
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## Database setup

From the project root (where `manage.py` is located):

```bash
python manage.py migrate
python manage.py createsuperuser  # optional: create admin user
```

## Run development server

```bash
python manage.py runserver
# visit http://127.0.0.1:8000
```

## Tests

If the project includes tests, run:

```bash
python manage.py test
```

Add a short description of what the tests cover and how to run specific test modules if relevant.

## Deployment recommendations

- Set `DEBUG=False` in production
- Use a secure `SECRET_KEY`
- Use a production-grade database (Postgres recommended)
- Serve the app with a WSGI server such as Gunicorn behind nginx
- Run `python manage.py migrate` during deployment
- Collect static files: `python manage.py collectstatic`

## Project structure (high level)

- `manage.py` — Django management entry point
- `life_time_app/` — Django project settings and core
- `users/`, `working_time/` — Django apps
- `db.sqlite3` — local development database (if present)

## Contributing

- Fork the repository, create a feature branch, and open a pull request with a clear description of changes
- Run tests and linters before submitting a PR
- Optionally document code style / linters used (e.g., `black`, `flake8`)

## License

Specify a license (e.g., MIT, GPL). If you prefer not to publish a license, write "All rights reserved".

## Contact

Provide author/contact information (name, email, GitHub link) here.

## Extras (optional)

- Docker support: add a `Dockerfile` and `docker-compose.yml` for local development
- CI: add a GitHub Actions workflow for tests and linters
- Screenshots or demo links

---

If you want, I can also:

- create a `.env.example` file in the repository
- add a simple `docker-compose.yml` and `Dockerfile`
- add a basic GitHub Actions workflow to run tests

Let me know which of the above you'd like me to add and I will update the repo.

