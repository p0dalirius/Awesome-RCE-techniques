FROM debian:buster

ENV VERSION 1.4

RUN apt-get -y -qq update \
    && apt-get -y -qq install gnupg apt-transport-https lsb-release ca-certificates apache2 git curl unzip wget composer mariadb-client mariadb-server \
    && wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
    && curl https://packages.sury.org/php/apt.gpg | apt-key add - \
    && echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list \
    && apt-get -y -qq update; apt-get -y -qq install php5.6 php5.6-mcrypt php5.6-mysql

# Apache2 configuration + modules
COPY ./files/apache2.conf /etc/apache2/apache2.conf
RUN a2enmod rewrite

# Installing the CMS
RUN wget "https://codeload.github.com/daylightstudio/FUEL-CMS/tar.gz/refs/tags/${VERSION}" -O /tmp/fuelcms.tar.gz \
    && rm /var/www/html/index.html \
    && cd /tmp/ \
    && tar xvf /tmp/fuelcms.tar.gz \
    && rm -rf /var/www/html/ \
    && mv /tmp/FUEL-CMS-${VERSION}/ /var/www/html

RUN cd /var/www/html/ \
    && composer install \
    && sed -i "s/\$config\['admin_enabled'\] = FALSE;/\$config\['admin_enabled'\] = TRUE;/g" /var/www/html/fuel/application/config/MY_fuel.php

# COPY ./files/.htaccess /var/www/html/.htaccess
COPY ./files/database.php /var/www/html/fuel/application/config/database.php
RUN chown www-data: -R /var/www/

# Create database fueldb and populate it
RUN service mysql start && \
    mysql -u root -e "CREATE USER 'db'@'%' IDENTIFIED BY 'db'; GRANT ALL PRIVILEGES ON *.* TO 'db'@'%' WITH GRANT OPTION; FLUSH PRIVILEGES;" && \
    mysql -u root -e "CREATE DATABASE fuelcms; use fuelcms; source /var/www/html/fuel/install/fuel_schema.sql;"

# Create the entrypoint script
RUN echo "#!/bin/bash" > /entrypoint.sh && \
    echo "service mysql start" >> /entrypoint.sh && \
    echo "apachectl -D FOREGROUND" >> /entrypoint.sh && \
    chmod +x /entrypoint.sh

RUN find /etc/php -type f -name "php.ini" -exec sed -i 's/^display_errors = Off$/display_errors = On/g' {} \;

EXPOSE 80

WORKDIR /var/www/html/

CMD /entrypoint.sh
