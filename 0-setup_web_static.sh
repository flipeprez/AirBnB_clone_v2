#!/usr/bin/env bash
# Bash script that set up my web server
sudo apt update
sudo apt install nginx - y
sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/current
# sudo touch /data/web_static/releases/test/index.html
# echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
echo -e '<html>\n<head>\n</head>\n<body>\nHolberton School\n </body>\n</html>' | sudo tee  /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/\tserver_name _;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
