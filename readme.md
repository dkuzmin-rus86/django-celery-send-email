Using Celery with Django to handle background tasks
=================
A simple demo for using Celery with Django to handle background tasks.

## Clone repo:
```
git clone https://github.com/dkuzmin-rus86/django-celery-send-email.git
cd django-celery-send-email
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Start project:
```
cd django-celery-send-email
./manage.py runserver
```

## Run a Redis server on Docker:
```
docker run --name my-redis -p 6379:6379 --restart always --detach redis
```

## Start Celery:
```
celery -A config worker --loglevel=debug --concurrency=4
```

## Start Celery beat for schedule task:
```
celery -A config beat
```

View the demo by navigating to `http://127.0.0.1:8000/`