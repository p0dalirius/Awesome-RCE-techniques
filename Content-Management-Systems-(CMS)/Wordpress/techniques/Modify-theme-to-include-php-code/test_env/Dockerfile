FROM debian:latest

ENV WORDPRESS_VERSION 4.6.6

RUN apt-get -y -q update; \
    apt-get -y -q install apache2 xxd git unzip wget php php-simplexml php-gd php-ldap php-zip php-imap php-mysql php-mbstring mariadb-client mariadb-server

RUN service mariadb start;\
    mysql -u root -e "CREATE DATABASE db; CREATE USER 'db'@'%' IDENTIFIED BY 'db'; GRANT ALL PRIVILEGES ON *.* TO 'db'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;"

RUN wget -q https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz -O /tmp/wordpress.tar.gz ;\
    cd /var/www/html/; rm index.html; tar xf /tmp/wordpress.tar.gz

RUN chown www-data: -R /var/www/

RUN echo "#!/bin/bash" > /entrypoint.sh ;\
    echo "service mariadb start" >> /entrypoint.sh ;\
    echo "apachectl -D FOREGROUND" >> /entrypoint.sh ;\
    chmod +x /entrypoint.sh

EXPOSE 80

CMD /entrypoint.sh
