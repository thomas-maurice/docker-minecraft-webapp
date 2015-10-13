FROM alpine:latest
MAINTAINER Thomas Maurice <thomas@maurice.fr>

RUN apk update && apk add nodejs bash git && \
    npm install -g grunt grunt-cli bower && \
    echo '{"interactive": false}' > /root/.bowerrc

COPY run.sh /run.sh

VOLUME /build

WORKDIR /build
CMD /run.sh
