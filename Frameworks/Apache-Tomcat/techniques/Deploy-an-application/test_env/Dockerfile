FROM tomcat:9.0.62-jdk11-openjdk-slim-buster

# https://octopus.com/blog/deployable-tomcat-docker-containers

RUN mv /usr/local/tomcat/webapps /usr/local/tomcat/webapps2 ;\
    mv /usr/local/tomcat/webapps.dist /usr/local/tomcat/webapps

COPY ./files/context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml
COPY ./files/tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

CMD ["catalina.sh", "run"]
