#!/bin/bash

chown -R www-data:www-data .
mkdir -p app/cache/prod
cp /ssl/cacert.pem app/cache/prod/
find themes/etrendlite/mails -type f -exec sed -i "s/localhost/localhost/" {} \;
rm -rf /etc/apache2/sites-available/000-default.conf
cp /ssl/000-default.conf /etc/apache2/sites-available/000-default.conf
a2enmod ssl
a2enmod rewrite
apachectl -D FOREGROUND
