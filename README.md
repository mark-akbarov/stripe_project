Stripe Project


Project Setup

Create Database:
  - create role stripe_user with login password '2404';
  - create database stripe_db with owner stripe_user;
  
Django Setup:
 - git clone the project
 - python -m venv venv
 - source venv/bin/activate
 - source .env
 - pip install -r requirements.txt
 - python manage.py migrate
