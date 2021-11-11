FROM alpine:3.5 as intermediate

RUN apk update
RUN apk add git

FROM prestashop/prestashop:1.7.1.0

RUN mkdir ssl
COPY ssl/000-default.conf /ssl/000-default.conf
COPY ssl/ssl.sh /ssl/ssl.sh
COPY cacert.pem /ssl/cacert.pem
COPY cert/localhost/localhost.key /etc/ssl/private/apache-selfsigned.key
COPY cert/localhost/localhost.crt /etc/ssl/certs/apache-selfsigned.crt

EXPOSE 443
