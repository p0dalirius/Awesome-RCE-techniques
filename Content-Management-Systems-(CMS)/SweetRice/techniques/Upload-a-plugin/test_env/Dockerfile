FROM debian:latest

RUN apt-get -y -q update ;\
    apt-get -y -q install apache2 xxd git unzip wget php php-mysql mariadb-client mariadb-server

RUN service mariadb start ;\
    mysql -u root -e "CREATE USER 'db'@'%' IDENTIFIED BY 'db'; GRANT ALL PRIVILEGES ON *.* TO 'db'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;"

RUN rm /var/www/html/index.html; git clone "https://github.com/sweetrice/SweetRice" /var/www/html/

RUN chown www-data: -R /var/www/

RUN echo "#!/bin/bash" > /entrypoint.sh ;\
    echo "service mariadb start" >> /entrypoint.sh ;\
    echo "apachectl -D FOREGROUND" >> /entrypoint.sh ;\
    chmod +x /entrypoint.sh

EXPOSE 80

CMD /entrypoint.sh
