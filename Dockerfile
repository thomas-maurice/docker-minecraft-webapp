FROM alpine:latest
MAINTAINER Thomas Maurice <thomas@maurice.fr>

# ENV VARIABLES
ENV MINECRAFT_DOCKER 1

# Basic deps install
RUN apk update && \
    apk upgrade && \
    apk add \
        wget \
        openjdk7-jre-base \
        curl \
        vim \
        openssh \
        sudo \
        py-pip \
        nginx \
        bash \
        logrotate

# Creation of the users and the groups
# Also the base directories for the minecraft user
RUN addgroup -g 4242 minecraft && \
    adduser -S www-data && \
    adduser -S -G minecraft -s /bin/bash -u 4242 -h /home/minecraft minecraft && \
    mkdir -p /home/minecraft/volume \
             /home/minecraft/runtime \
             /home/minecraft/.ssh

# Download the server from Amazon
RUN wget https://s3.amazonaws.com/Minecraft.Download/versions/1.8.8/minecraft_server.1.8.8.jar -O /home/minecraft/runtime/server.jar && \
    chown minecraft:minecraft /home/minecraft/runtime/server.jar

# Useful for debugging purposes
COPY misc/authorized_keys /home/minecraft/.ssh/authorized_keys
RUN echo "minecraft ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/minecraft
RUN mkdir /var/run/sshd && ssh-keygen -A

# Pip installs
RUN pip install supervisor && \
    mkdir /var/log/supervisor && \
    ln -s /etc/supervisor/supervisord.conf /etc/supervisord.conf

COPY server/eula.txt /home/minecraft/runtime/eula.txt
COPY cron/backup /etc/crontabs/minecraft
COPY nginx/default /etc/nginx/sites-enabled/default
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY logrotate/minecraft /etc/logrotate.d/minecraft
COPY misc/bashrc /etc/bash.bashrc
COPY server/server.properties /home/minecraft/runtime/server.properties.default
COPY server/server.properties.variable /home/minecraft/runtime/server.properties.variable.default
COPY supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisor/minecraft.conf \
     supervisor/webapp.conf \
     supervisor/nginx.conf \
     /etc/supervisor/conf.d/
COPY webapp_build /home/minecraft/webapp
COPY textures /var/www/textures

RUN chown -R www-data:minecraft /var/www/textures

RUN ln -s /etc/bash.bashrc /root/.bashrc && \
    ln -s /etc/bash.bashrc /home/minecraft/.bashrc

RUN cd /home/minecraft/webapp && \
    pip install -r requirements.txt && \
    chown -R minecraft:minecraft /home/minecraft

EXPOSE 22 80 25565

VOLUME /home/minecraft/volume

COPY run.sh /run.sh
COPY generate_server_properties.sh /generate_server_properties.sh
COPY backup.sh /backup.sh

CMD /run.sh
