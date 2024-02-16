#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-install -y nginx

# Create the folders
sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir -p /data/web_static/releases/test

# Create a fake HTML file
echo "webstatic_deployment" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo rm -f /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
sudo sed -i '38i\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
