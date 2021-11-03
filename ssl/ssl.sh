find themes/etrendlite/mails -type f -exec sed -i "s/localhost/localhost/" {} \;
rm -rf /etc/apache2/sites-available/000-default.conf
cp /ssl/000-default.conf /etc/apache2/sites-available/000-default.conf
a2enmod ssl
a2enmod rewrite
apachectl -D FOREGROUND
