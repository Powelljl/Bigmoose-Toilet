#!/bin/sh
# Create the service unit files
echo "[Unit]
Description=Big moose python script
After=network.target

[Service]
User=$(whoami)
WorkingDirectory=$PWD
ExecStart=$PWD/button-start.sh

[Install]
WantedBy=multi-user.target" > big-moose-button.service
echo "[Unit]
Description=Big moose forest sounds
After=network.target

[Service]
User=$(whoami)
WorkingDirectory=$PWD
ExecStart=$PWD/forest-start.sh

[Install]
WantedBy=multi-user.target" > big-moose-forest.service
# Move the service files to the systemd folder
sudo mv big-moose-button.service /etc/systemd/system/
sudo mv big-moose-forest.service /etc/systemd/system/
# Make startup scripts executable
sudo chmod +x button-start.sh
sudo chmod +x forest-start.sh
# Set them to start at startup
sudo systemctl enable big-moose-button
sudo systemctl enable big-moose-forest
# Start the services
sudo systemctl start big-moose-button
sudo systemctl start big-moose-forest
# Create the python venv and install required packages
sudo apt install -y python3-pip python3-venv mplayer
if [ ! -d directory ]; then
  python3 -m venv env
fi
source env/bin/activate
python3 -m pip install -r requirements.txt
deactivate
echo "Done! The service names are big-moose-button and big-moose-forest"