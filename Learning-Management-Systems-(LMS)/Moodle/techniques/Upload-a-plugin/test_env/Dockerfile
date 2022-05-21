FROM debian:latest

ENV DBUSER=moodle
ENV DBPASS=moodle

RUN apt-get -y -qq update; \
    apt-get -y -qq install wget unzip git nano php php-curl php-gd php-zip php-xmlrpc php-soap php-intl php-mysql php-xml php-mbstring apache2 mariadb-server mariadb-client

RUN find /etc/php/ -name "php.ini" -exec sed -i 's/.*max_input_vars = .*/max_input_vars = 6000/g' {} \; ;\
    sed -i 's/^.*bind-address.*=.*$/bind-address = 0.0.0.0/g' /etc/mysql/mariadb.conf.d/50-server.cnf

RUN service mariadb start;\
    mysql -u root -e "CREATE DATABASE db; CREATE USER '${DBUSER}'@'%' IDENTIFIED BY '${DBPASS}'; GRANT ALL PRIVILEGES ON *.* TO '${DBUSER}'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;"

WORKDIR /var/www/html/
RUN wget "https://download.moodle.org/stable400/moodle-latest-400.zip" -O /tmp/moodle.zip ;\
    rm /var/www/html/index.html ;\
    unzip /tmp/moodle.zip ;\
    mv moodle*/* /var/www/html/ ;\
    mkdir -p '/var/www/html/moodledata' ;\
    chown www-data:www-data -R /var/www/

RUN echo '#!/bin/bash' >> /entrypoint.sh; \
    echo "service mariadb start" >> /entrypoint.sh; \
    echo "sleep 2" >> /entrypoint.sh; \
    echo "/usr/sbin/apachectl -D FOREGROUND" >> /entrypoint.sh; \
    chmod +x /entrypoint.sh;

COPY ./files/config.php /var/www/html/config.php
RUN chown www-data:www-data /var/www/html/config.php;

EXPOSE 3306
EXPOSE 80

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
