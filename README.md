# Note Pond - Project 2 submission

**Flores CS 422 - Spring 2023**  
**Aiden Duval, Devin Henderling, Carlos Villarreal-Elizondo, Nick Swanson, Zach Weisenbloom**  
**May 21st, 2023**

## Description

forecasTS is a web application that allows users to share and find notes for courses at the University of Oregon. Users
can upload and download notes of various formats, adding tags and associated courses/weeks.

## Dependencies

Dependencies can be found at `NotePond/requirements.txt`.

## Instructions To Start App

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project root directory (where `README.md` is located).
3. Create a Python virtual environment:

$ python -m venv .venv

4. Activate the virtual environment:

Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

macOS
$ source .venv/bin/activate

5. Traverse to forecasTS/ and Install the required dependencies:
   (.venv) $ pip install -r requirements.txt

6. Run the database migrations:
   (.venv) $ python manage.py migrate

7. Create a superuser for the Django admin site:
   (.venv) $ python manage.py createsuperuser

8. Start the development server:
   (.venv) $ python manage.py runserver

9. Load the site at http://127.0.0.1:8000.
