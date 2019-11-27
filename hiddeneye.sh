clear
cd ~
rm -Rf HiddenEye
apt update
apt upgrade
apt install git
apt remove python
apt install python
git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git
cd HiddenEye
pip3 install wget
python3 HiddenEye.py