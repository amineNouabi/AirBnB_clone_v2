#!/usr/bin/env bash
#Sets up web server for the deployment of web_static

#Check if system is running ubuntu
if [ ! -d "/etc/apt" ]; then
	echo "This script is only for Ubuntu systems"
	exit 1
fi

#Install nginx
if ! dpkg -l | grep -q nginx; then
	sudo apt-get update
	sudo apt-get -y install nginx

	sudo service nginx start
	sudo ufw allow 'Nginx HTTP'
fi

#Create directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

HTML="<!DOCTYPE html>
<html> 
  <head>
  </head>
  <body>
    Hello World!
  </body>
</html>
"

#Create fake html file
echo "$HTML" >/data/web_static/releases/test/index.html

#Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#Change ownership of /data/**/* to ubuntu
sudo chown -R ubuntu:ubuntu /data/

#Add alias to nginx configuration
if ! grep -q "location /hbnb_static {" /etc/nginx/sites-available/default; then
	sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

#Restart nginx
sudo service nginx restart
