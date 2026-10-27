FROM ubuntu:22.04
WORKDIR /app
ARG commit_id
ARG username
RUN apt update && apt install wget unzip -y
COPY apache-tomcat-9.0.123.tar.gz COPY-TAR/
ADD script.sh scripts/
ADD apache-tomcat-9.0.123.tar.gz ADD-TAR/
ADD https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.123/bin/apache-tomcat-9.0.123.tar.gz ADD-URL/
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 APP_VERSION=1.1.0 GIT_COMMIT_ID=${commit_id}
RUN useradd $username && mkdir -p /home/$username && chown -R $username:$username /home/$username
USER $username
EXPOSE 8080
LABEL maintainer=Prayog GIT_COMMIT_ID=${commit_id}
STOPSIGNAL SIGKILL