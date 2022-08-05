FROM debian:buster

RUN apt-get -y -q update; \
    apt-get -y -q install git pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev

RUN cd /opt/ \
    && git clone https://github.com/php/php-src/ ./php/

WORKDIR /opt/php

RUN git checkout c730aa26bd52829a49f2ad284b181b7e82a68d7d \
    && ./buildconf \
    && mkdir -p /etc/php/8.1.0-dev/ \
    && ./configure --with-config-file-path=/etc/php/8.1.0-dev/php.ini \
    && make -j4 \
    && make install

RUN apt-get -y -q install apache2

RUN rm /var/www/html/index.html \
    && echo '<html><body><h1>Dummy in HTML</h1></body></html>' > /var/www/html/dummy.html \
    && echo '<?php echo "<html><body><h1>Dummy in PHP</h1></body></html>"; ?>' > /var/www/html/dummy.php \
    && echo '<?php phpinfo(); ?>' > /var/www/html/phpinfo.php \
    && chown www-data: -R /var/www/html/

RUN echo "#!/bin/bash" > /entrypoint.sh ;\
    echo "apachectl -D FOREGROUND" >> /entrypoint.sh ;\
    chmod +x /entrypoint.sh

EXPOSE 80

CMD /entrypoint.sh
