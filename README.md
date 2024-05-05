# elder-spatula
nginx, gunicorn, django container

## configuration
+ gunicorn on port 8000
+ /api = django REST demo
+ /app = django demo

## manual step
+ must add basic auth (for REST)
+ ```python manage.py createsuperuser --username admin --email admin@example.com```

## curl
+ ```curl -v http://localhost:8000/app/```
+ ```curl -v http://localhost:8000/app/page3/```
+ ```curl -v -i -u admin -H "Content-Type: application/json" http://localhost:8000/api/simple/```
+ ```curl -v -i -u admin -H "Content-Type: application/json" -d "{\"key\":\"aaa\", \"value\":\"bbb\"}" http://localhost:8000/api/simple/```

## links
+ https://www.nginx.com/blog/deploying-nginx-nginx-plus-docker/
+ https://docs.nginx.com/nginx/admin-guide/web-server/web-server/
+ https://www.django-rest-framework.org
+ https://www.codingforentrepreneurs.com/blog/django-gunicorn-nginx-docker/
+ https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu
