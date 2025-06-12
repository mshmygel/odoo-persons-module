# 👤 Odoo Persons Module

An Odoo 16 module for managing persons with website display capabilities. Allows creating, editing, and displaying information about people both from the backend and on a custom `/persons` webpage.

---

## 📌 Table of Contents

* [🌐 Overview](#-overview)
* [✨ Features](#-features)
* [🛠 Tech Stack](#-tech-stack)
* [🧹 System Requirements](#-system-requirements)
* [⚙️ Installation](#-installation)
  * [Docker Setup](#docker-setup)
  * [Module Installation](#module-installation)
  * [Running Commands](#running-commands)
* [📚 Module Structure](#-module-structure)
* [🌍 Frontend Page](#-frontend-page)
* [🔐 Admin Usage](#-admin-usage)
* [📝 API Endpoints](#-api-endpoints)
* [🛠️ Development](#-development)

---

## 🌐 Overview

This module allows administrators to manage a list of persons from the Odoo backend and render a stylized team page at `/persons` on the public website. Each person record includes computed fields for age and full name, with validation rules applied.

## ✨ Features

* **Person Management**: Create, edit, and delete person records
* **Automatic Calculations**: Full name and age computation based on birth date
* **Backend Integration**: Form & tree views for CRUD operations
* **Data Validation**: Prevents future birth dates and ensures data integrity
* **Responsive Frontend**: Bootstrap-styled public website display
* **Multi-company Support**: Integration with Odoo company system
* **Role-based Access**: Configurable permissions for different user groups

## 🛠 Tech Stack

* Python 3.10+
* Odoo 16.0
* PostgreSQL 13
* Docker & Docker Compose
* XML for templates and views
* QWeb templating engine

## 🧹 System Requirements

* Docker & Docker Compose
* 2 GB RAM minimum
* 4 GB free disk space
* Modern web browser

## ⚙️ Installation

### Docker Setup

```bash
git clone https://github.com/your-username/odoo-persons-module.git
cd odoo-persons-module
docker-compose up -d
```

### Module Installation

1. **Access Odoo**: Open `http://localhost:8069`
2. **Database Setup**: Create or log into a database
3. **Install Module**:
   - Go to **Apps** → **Update Apps List**
   - Search for **Persons V3**
   - Click **Install**

### Running Commands

```bash
# Start containers
docker-compose up -d

# Stop containers
docker-compose down

# View logs
docker-compose logs -f web

# Restart services
docker-compose restart

# Access Odoo shell
docker-compose exec web odoo shell -d your_database_name
```

## 📚 Module Structure

```
persons_module_v3/
├── __manifest__.py          # Module manifest and dependencies
├── __init__.py              # Module initialization
├── controllers/             # Website controllers
│   ├── __init__.py
│   └── website_persons.py   # Public website routes
├── models/                  # Data models
│   ├── __init__.py
│   └── person.py           # Person model with computed fields
├── views/                   # Backend views
│   ├── person_view.xml     # Form and tree views
│   └── menu.xml            # Menu items and actions
├── templates/               # Website templates
│   └── person_template.xml # QWeb template for public page
├── static/                  # Static files
│   └── description/
│       ├── index.html      # Module description
│       └── image.png       # Module icon
└── security/                # Access control
    └── ir.model.access.csv # User permissions
```

## 🌍 Frontend Page

Visit the public persons page:

```
http://localhost:8069/persons
```

**Features:**
- Modern card-based layout with avatars
- Displays name, company, age, and gender
- Responsive Bootstrap design
- Shows latest 5 persons by default
- Fallback message when no persons exist

## 🔐 Admin Usage

### Adding New Persons

1. **Backend Access**: Navigate to `http://localhost:8069/web`
2. **Enable Developer Mode**: Settings → Activate Developer Mode
3. **Access Menu**: **Administration** → **Persons** → **All Persons**
4. **Create Record**: Click **Create**

### Required Fields

* **First Name** - Person's first name
* **Last Name** - Person's last name

### Optional Fields

* **Birthday** - Birth date (auto-computes age)
* **Sex** - Gender selection (Male/Female/Non-binary)
* **Company** - Associated company (defaults to current user's company)

### Computed Fields

* **Full Name** - Automatically combines first and last name
* **Age** - Calculated from birth date

## 📝 API Endpoints

* `GET /persons` — Public persons listing page
* Backend CRUD operations available through Odoo's standard API

## 🛠️ Development

### Manual Testing

1. **Create Test Data**: Add several persons through the backend
2. **Verify Frontend**: Check `http://localhost:8069/persons`
3. **Test Validation**: Try entering future birth dates (should fail)

### Customization

**Change Display Limit**: Edit `limit=5` in `controllers/website_persons.py`

**Modify Template**: Update `templates/person_template.xml` for styling changes

**Add Fields**: Extend the Person model in `models/person.py`

### Debugging

```bash
# Enable debug mode
docker-compose exec web odoo --dev=all

# View server logs
docker-compose logs -f web

# Access Python shell
docker-compose exec web python3
```

### Best Practices

* Always update `__manifest__.py` when adding new data files
* Use `sudo()` carefully in controllers for security
* Add proper field validation in models
* Follow Odoo naming conventions

---

📦 Standard Odoo module structure. Dockerized for easy deployment. No virtualenv or Poetry needed. Ready for production use with proper security configurations.
```
