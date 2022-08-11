FROM debian:buster

RUN apt-get -y -q update \
    && apt-get -y -q install wget tar git libnet-ssleay-perl libauthen-pam-perl libio-pty-perl unzip shared-mime-info

RUN mkdir -p /webmin/ \
    && wget https://github.com/webmin/webmin/releases/download/1.996/webmin_1.996_all.deb -O /webmin/webmin.deb \
    && dpkg -i /webmin/webmin.deb

RUN useradd -s /bin/bash webmin \
    && echo "webmin:webmin" | chpasswd \
    && echo "root:root" | chpasswd

RUN echo "#!/bin/bash" > /entrypoint.sh \
    && echo "service webmin start" >> /entrypoint.sh \
    && echo "service webmin status" >> /entrypoint.sh \
    && chmod +x /entrypoint.sh

EXPOSE 80

CMD /bin/bash

