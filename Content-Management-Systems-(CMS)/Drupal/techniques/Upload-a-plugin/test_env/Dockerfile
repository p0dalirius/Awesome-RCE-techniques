FROM debian:buster

ENV DRUPALVERSION "9.2.1"

RUN apt-get -y -q update; \
    apt-get -y -q install apache2 xxd git unzip wget php php-simplexml php-gd php-ldap php-zip php-imap php-mysql php-mbstring mariadb-client mariadb-server composer

COPY ./files/apache2.conf /etc/apache2/apache2.conf
RUN a2enmod rewrite

RUN service mysql start;\
    mysql -u root -e "CREATE USER 'db'@'%' IDENTIFIED BY 'db'; UPDATE mysql.user set plugin = 'mysql_native_password' WHERE User = 'db'; GRANT ALL PRIVILEGES ON *.* TO 'db'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;"

RUN wget "https://ftp.drupal.org/files/projects/drupal-${DRUPALVERSION}.zip" -O /tmp/drupal.zip ;\
    cd /var/www/html/ ;\
    rm index.html ;\
    unzip /tmp/drupal.zip ;\
    mv drupal-${DRUPALVERSION}/* ./ ;\
    composer install

RUN chown www-data: -R /var/www/

RUN echo "#!/bin/bash" > /entrypoint.sh ;\
    echo "service mysql start" >> /entrypoint.sh ;\
    echo "apachectl -D FOREGROUND" >> /entrypoint.sh ;\
    chmod +x /entrypoint.sh

EXPOSE 80

CMD /entrypoint.sh
