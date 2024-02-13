#!/usr/bin/env bash
# Install nginx and create a fake html file

link_dir="/data/web_static/current"
release_folder="/data/web_static/releases/test"
HTML_CONTENT="<html>
    <head>
    </head>
    <body>
	My fake html file
    </body>
</html>"

apt-get -y update >/dev/null 2>&1
apt-get -y install nginx >/dev/null 2>&1
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "$HTML_CONTENT" >/data/web_static/releases/test/index.html
ln -sf "$release_folder" "$link_dir"
chown -R ubuntu:ubuntu /data/
sed -i '/^server {/,/^}/!b;/^}/i\\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}' /etc/nginx/sites-enabled/default
service nginx restart