#!/usr/bin/env bash
## Installing configuration

## Update and install nginx
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y

## Create a folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

## Create a file index.html
sudo echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

## Create a simbolink link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

## Owner and group belong to ubuntu user
sudo chown -R ubuntu:ubuntu /data

## Update the nginx configuration
new_string="a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/listen 80 default_server;/$new_string" /etc/nginx/sites-available/default

## Restarting the nginx service
sudo service nginx restart
