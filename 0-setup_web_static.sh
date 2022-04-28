#!/usr/bin/env bash
# Bash script that set up my web server
if [ "$(dpkg-query -W -f="${Status}" nginx 2>/dev/null | grep -c "ok installed")" -eq 0 ]
then
sudo apt update
sudo apt install nginx -y
fi
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/current
echo -e '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/\tserver_name _;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
