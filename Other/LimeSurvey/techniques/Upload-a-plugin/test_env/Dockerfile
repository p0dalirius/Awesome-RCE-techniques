FROM debian:buster

RUN apt-get -y -q update; \
    apt-get -y -q install apache2 xxd git unzip wget php php-simplexml php-gd php-ldap php-zip php-imap php-mysql php-mbstring mariadb-client mariadb-server

RUN service mysql start;\
    mysql -u root -e "CREATE USER 'db'@'%' IDENTIFIED BY 'db'; UPDATE mysql.user set plugin = 'mysql_native_password' WHERE User = 'db'; GRANT ALL PRIVILEGES ON *.* TO 'db'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;"

RUN wget https://github.com/LimeSurvey/LimeSurvey/archive/refs/tags/5.2.4+211129.zip -O /tmp/LimeSurvey.zip ;\
    cd /var/www/html/; rm index.html; unzip /tmp/LimeSurvey.zip; mv LimeSurvey-5.2.4-211129/* .

RUN chown www-data: -R /var/www/

RUN echo "#!/bin/bash" > /entrypoint.sh ;\
    echo "service mysql start" >> /entrypoint.sh ;\
    echo "apachectl -D FOREGROUND" >> /entrypoint.sh ;\
    chmod +x /entrypoint.sh

EXPOSE 80

CMD /entrypoint.sh
