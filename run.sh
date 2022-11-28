cd /home/mrk/stripe &&
source conf &&
source venv/bin/activate  &&
gunicorn config.wsgi