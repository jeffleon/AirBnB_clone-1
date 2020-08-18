#!/bin/env bash 
# set up the information to fabric
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "test Holberton School" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu:ubuntu /data/
sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
