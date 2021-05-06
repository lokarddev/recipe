Recipe project
--------------
This is my first project with Python & Django. This web app provides us a simple recipe sharing service.

Stack
-----
Python3
Django
Redis
PostgreSQL
GraphQL
JWT

Recipe app has it's own graphql API. API giving an access to almost all data stored in database or another data storages.


To run the project on your computer you have to:
------------------------------------------------
1. Choose where to clone the project, then `git clone https://github.com/lokarddev/recipe.git`
2. `cd recipe`
3. `git checkout with_fixtures` We should use this branch if u don't want to create some initial data by yourself, or skip this step
4. Here you have to make sure that your postgresql and redis server are running, otherwise you should install them and run.
5. Create database for project
6. `touch recipe_config/.env` This file needed to store some environment variables to use in our project settings
    .env file data should be for example like this:
    
DEBUG=True

SECRET_KEY='uvop9ac6r2334eiq+00)z(wg=%*xe3_45ks(6%&gsdf+g3894#sgtcv4dq)dim69a'`here should be your secret key`

DATABASE_NAME=<db_name>

DATABASE_USER=<db_user_name>

DATABASE_PASSWORD=<db_user_password>

DATABASE_HOST=<db_host>

DATABASE_PORT=<db_port>

CACHE_URL=127.0.0.1:11211 `here should be your cache url. by default u can use this`

REDIS_URL=redis://localhost:6379 `here should be your redis url. by default u can use this`

  
7.  Create virtual environment for project, then `source venv/bin/activate`
8. `pip install -r requirements.txt`
9. `python manage.py migrate`
10. `python manage.py loaddata fixtures/test_data.json`
11. `python manage.py createsuperuser`
12. `python manage.py runserver`

From here u can go http://localhost:8000/ and interact with website.

For running celery task manager you should add some commands from project folder and virtualenv activated:
1. `celery -A recipe_config worker -l INFO`
2. `celery -A recipe_config beat -l INFO`

