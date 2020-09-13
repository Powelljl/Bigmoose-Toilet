# Bigmoose Button

Bigmoose Button is run from two scripts that run the button in the toilet in Bigmoose Cardiff, The button triggers a sound effect and there is also background music running on a loop.
#### Demo
[![Demo Bigmoose Button](https://media.giphy.com/media/WT3dnzmtPDhz3PwqiX/200w_d.gif)](https://media.giphy.com/media/WT3dnzmtPDhz3PwqiX/source.mp4)


### Tech

Bigmoose Button uses a number of open source projects to work properly:
#### Software
* [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Used for the background music looping.
* [Python](https://www.python.org/) - Used in the script to detect button press and triggering sound effect.
* [Pygame](https://www.pygame.org/) - Used in the script to detect button press and triggering sound effect.
#### Hardware
* [Rasberry Pi 3b+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) - Used as the Microcontroller/Mini PC.
* [Adafruit I2S 3W Stereo Speaker Bonnet](https://www.adafruit.com/product/3346) - Used as Speakers in the Toilet. 


### Installation

Simply run the `install.sh` script and it'll take care of everything for you (make sure it's executable with `chmod +x install.sh`!), including making two systemd service files (`big-moose-button` and `big-moose-forest`), enabling them at startup, creating a python venv and installing the required packages to the venv.
You must run the install script as a user with sudo permissions, but do _not_ run it as sudo - it will ask for sudo elevation during the installation procedure.

----
Licence
MIT


**Free Software, Hell Yeah!**