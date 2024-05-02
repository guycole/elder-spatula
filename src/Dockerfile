#
# elder-spatula
#
# docker build . -t elder-spatula:1
# docker run --rm --name spatula -it -p 8088:80 elder-spatula:1
# docker exec -it <container id> sh
#
# docker run -d -p 80:80 elder-spatula:1 
# docker run -d -p 80:80 ghcr.io/guycole/elder-spatula/app:latest
# docker exec --rm -it elder-spatula:1 sh
# docker system prune --all
#
# django wants 8000
#
# kubectl run es --rm -it --image=elder-spatula:1 --restart=Never -- sh
#
# https://www.nginx.com/blog/deploying-nginx-nginx-plus-docker/
# https://docs.nginx.com/nginx/admin-guide/web-server/web-server/
#
FROM debian:11-slim
LABEL build_date="2024-05-05"
LABEL description="elder-spatula"
LABEL maintainer="guycole@gmail.com"
LABEL org.opencontainers.image.description DESCRIPTION "fresh description"
#
RUN apt-get update && apt-get install -y 
RUN apt-get install -y curl nginx iputils-ping net-tools vim
RUN apt-get install -y python3 python3-virtualenv
#
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install django gunicorn
#
RUN mkdir django
RUN django-admin startproject spatula django
#
#RUN virtualenv -p /usr/bin/python3 venv
#
#source venv/bin/activate
#pip install Django

#
#COPY nginx.conf /etc/nginx/nginx.conf
#COPY default.conf /etc/nginx/conf.d/default.conf
#COPY index.html /usr/share/nginx/html/index.html
#COPY page2.html /usr/share/nginx/html/page2.html
#
# pod command and args
#ENTRYPOINT [ "/app/crocodile" ]
#CMD [ "bogus" ]
#
