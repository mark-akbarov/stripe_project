# Stripe Project


### Project Setup

<b>Create Database:</b>

  - create role stripe_user with login password '2404';
  - create database stripe_db with owner stripe_user;
  
<b>Django Setup</b>:
 - git clone the project
 - python -m venv venv
 - source venv/bin/activate
 - source .env
 - pip install -r requirements.txt
 - python manage.py migrate
