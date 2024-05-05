#
# elder-spatula
#
# docker build . -t elder-spatula:1
# docker run --rm --name spatula -it -p 8080:80 elder-spatula:1
# docker exec -it <container id> sh
#
FROM debian:11-slim
LABEL build_date="2024-05-05"
LABEL description="elder-spatula"
LABEL maintainer="guycole@gmail.com"
LABEL org.opencontainers.image.description DESCRIPTION "fresh description"
#
RUN apt-get update && apt-get install -y 
RUN apt-get install -y curl nginx iputils-ping net-tools vim
RUN apt-get install -y python3 python3-pip
#
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install django djangorestframework gunicorn
#
COPY django /app/django
#
COPY src/default.conf /etc/nginx/conf.d/default.conf
COPY src/index.html /var/www/html/index.html
COPY src/page2.html /var/www/html/page2.html
#
COPY src/entrypoint.sh /app/entrypoint.sh
RUN chmod +x entrypoint.sh
#
ENTRYPOINT [ "/app/entrypoint.sh" ]
#
