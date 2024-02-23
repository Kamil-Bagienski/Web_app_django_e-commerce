# Web_app_django_e-commerce
Sales Management App using Django and SQLite. Manages customers, products, orders, payments with SQL joins for data analysis. Includes data visualization with chart.js. Code in English for clarity. Tested on Windows 11 and Arch Linux. Available on GitHub for educational purposes.
This is a web application project as part of the SQL Language/Database Management System course. It is one of the three tasks we were to choose from for the project. Its description is as follows:
Sales Process Management Application with Multiple SQL Tables:
• Project goal: To create an application for managing the sales process, which uses an SQL database to store and analyze data.
• Functionalities: The application enables management of customers, products, orders, and payments. It utilizes various types of joins (equi joins, non-equi joins) for the analysis of sales data.

I built the application on the Django framework. It handles the database in an ORM form, using SQLite for its construction, and HTML templates for frontend purposes. For the backend, it uses object-oriented Python. I won't describe the framework itself, as it is well-known to many people. However, it is a very large framework, which is rather used for bigger projects. Yet, in these small ones, it works great as a start of a bigger project. Thanks to this task, I have learned how to work within this framework, and I am now fascinated by it. In the documentation, I will present its operation and the solutions I applied. In the attached files, I give the entire code for the application. After evaluating my work, the application will be available on GitHub as an educational aid for anyone who wants to build a small application on this framework. Variables in Python have been written in English for greater clarity. Data analysis is presented in chart.js; initially, it was supposed to be handled by a module dedicated to Django, but unfortunately, it is not compatible with the latest Python and the latest Django, so I had to finally do data visualization in chart.js. This project has been tested by me for operation on Windows 11 and Arch Linux.


Application Launch:

1. Python Installation: Visit python.org, download Python for your OS, and install it, adding Python to the PATH environment variable.
2. Verify Python and pip: Open terminal, check versions with python --version and pip --version.
3. Django Installation: In terminal, pip install django.
4. Prepare Django App: Unzip the received Django app (Web_app_django_e-commerce.zip).
5. Database Migrations: Navigate to the Django project's root where manage.py is, then in terminal: python manage.py makemigrations and python manage.py migrate.
6. Create Superuser: For admin panel access, python manage.py createsuperuser.
7. Start Development Server: Run python manage.py runserver.
8. Access Application: Open browser to http://localhost:8000/ for the app, and http://localhost:8000/admin for admin panel.

Documentation in polish.
