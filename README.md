# 🧑‍💼 Employee Management System

A web-based application built using **Django** and **MySQL (via XAMPP)** to efficiently manage employee records. This system allows organizations to perform CRUD operations (Create, Read, Update, Delete) on employee data with a clean and simple interface.
## 🚀 Features

- ✅ Add new employee records
- ✏️ Edit employee information
- 🗑️ Delete employees
- 📋 View all employee details in a tabular format
- 🧩 MySQL database integration using XAMPP
- 🧼 Clean and responsive UI (HTML + CSS)
  
## 🛠️ Tech Stack
- **Framework**: Django (Python)
- **Database**: MySQL (via XAMPP)
- **Frontend**: HTML, CSS
- **Web Server**: Django Development Server

## ⚙️ Local Setup Instructions (XAMPP + Django)
### 1. Clone the Repository
```bash
git clone https://github.com/premcodeexplorer/employee-management-system.git
cd employee-management-system
```
2. Set Up Virtual Environment
```bash
python -m venv env
```
Activate the virtual environment:
Windows:
```bash
.\env\Scripts\activate
```
macOS/Linux:
```bash
source env/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```

##4. Set Up MySQL Database via XAMPP
Open XAMPP Control Panel
Start Apache and MySQL
Visit http://localhost/phpmyadmin
Create a new database named:
employee_db

##5. Configure MySQL in settings.py
Open emp_management/settings.py and update the DATABASES section:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employee_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

##6. Run Migrations and Start the Development Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
##Then open your browser and go to:

👉 http://127.0.0.1:8000/

##📁 Project Structure
employee-management-system/
├── emp_management/       # Project-level settings
├── employees/            # App with models, views, templates
├── manage.py             # Django CLI entry point
├── requirements.txt      # Python dependencies


## 🖼️ Demo Screenshot

Here's a preview of the Employee Management System interface:
![WhatsApp Image 2025-04-10 at 20 50 15](https://github.com/user-attachments/assets/9b0e14b0-9fea-4bdb-9c68-cc1f81b0eebb)

