Made by Gaurav Panchal:

This project is based on Library Management System. It uses Django as Backend Server and HTML for Frontend.
The Project can be run on any device.

Steps to run this project:
1. Install Python on the device.
2. Create a virtual Environment in order to freeze the updates.
3. PIP install the requirements.txt file.
4. Then navigate to the folder containing manage.py file and run "python manage.py runserver" to run the project.
5. The Project will be up and running. Now open the "localhost:8000" site on your web browser.


Currently in order to make changes in the database the user needs to have special permissions from the administrator.
So after registration you will need to navigate to "localhost:8000/admin" and login with "gorop:1234567890" credentials or create your own superuser ( administrator ) using following command "python manage.py createsuperuser" and then after logging in you can choose to give special permissions to other users.

In order to update or delete the records from the system, the user needs to be administrator or gain permissions from the administrator. The records are visible to everyone.