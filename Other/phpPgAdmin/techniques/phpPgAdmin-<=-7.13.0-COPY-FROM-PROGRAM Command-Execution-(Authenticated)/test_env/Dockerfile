FROM debian:buster

RUN apt-get -y -q update \
    && apt-get -y -q install wget tar git pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev libapr1-dev libaprutil1-dev libpcre3 libpcre3-dev zlib1g-dev libpng-dev

# Building and installing apache2
RUN mkdir -p /build/ \
    && cd /build/ \
    && wget https://dlcdn.apache.org/httpd/httpd-2.4.54.tar.gz -O httpd.tar.gz \
    && tar xvf httpd.tar.gz \
    && cd httpd-2.4.54/ \
    && ./configure --enable-so \
    && make \
    && make install

# Building and installing php-8.1.0-dev
RUN mkdir -p /build/ \
    && cd /build/ \
    && git clone https://github.com/php/php-src/ /build/php/ \
    && cd /build/php/ \
    && git checkout c730aa26bd52829a49f2ad284b181b7e82a68d7d \
    && ./buildconf \
    && ./configure --with-apxs2=/usr/local/apache2/bin/apxs --with-pdo-mysql \
    && make -j4 \
    && make install \
    && echo "LoadModule php_module /build/php/libs/libphp.so" >> /usr/local/apache2/conf/httpd.conf \
    && echo '<FilesMatch \.php$>' >> /usr/local/apache2/conf/httpd.conf \
    && echo '    SetHandler application/x-httpd-php' >> /usr/local/apache2/conf/httpd.conf \
    && echo '</FilesMatch>' >> /usr/local/apache2/conf/httpd.conf

RUN mkdir -p /usr/local/apache2/htdocs \
    && rm /usr/local/apache2/htdocs/index.html \
    && echo '<html><body><h1>Dummy in HTML</h1></body></html>' > /usr/local/apache2/htdocs/dummy.html \
    && echo '<?php echo "<html><body><h1>Dummy in PHP</h1></body></html>"; ?>' > /usr/local/apache2/htdocs/dummy.php \
    && echo '<?php phpinfo(); ?>' > /usr/local/apache2/htdocs/phpinfo.php \
    && chown www-data: -R /usr/local/apache2/htdocs/

RUN echo "#!/bin/bash" > /entrypoint.sh \
    && echo "echo '===[Checking if backdoor is here]========================================================================'" >> /entrypoint.sh  \
    && echo "grep -rain zerodium -n5 /build/php/ext/zlib/zlib.c" >> /entrypoint.sh  \
    && echo "echo '========================================================================================================='" >> /entrypoint.sh  \
    && echo "/usr/local/apache2/bin/apachectl -D FOREGROUND" >> /entrypoint.sh \
    && chmod +x /entrypoint.sh

EXPOSE 80

CMD /bin/bash

