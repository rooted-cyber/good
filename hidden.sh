cd ~
if [ -e HiddenEye ];then
rm -rf HiddenEye
fi
check-git () {
	cd $PREFIX/bin
	if [ -e git ];then
	clear
	printf "\n\033[92m Successfully install git\n"
	else
	ins
	fi
	}
	ins () {
apt update
apt upgrade
apt install git
py-c
check-git
hidd
}
ins-p () {
	apt install python
	}
py-c() {
	cd $PREFIX/bin
	if [ -e python ];then
	apt remove python
	apt install python
	clear
	printf "\n \033[92m python is installed\n"
	else
	ins-p
	fi
	}
	hidd () {
		clear
		cd $HOME
		printf "\n\n\033[93m Cloning hiddeneye....\n"
		git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git
		cd HiddenEye
		pip3 install requests
		pip3 install wget
		printf "\n \033[96m Press enter to open\n"
		read
		check-h
		}
		check-h () {
			cd $HOME
			if [ -e HiddenEye ];then
			cd ~/HiddenEye
			python3 HiddenEye.py
			else
			hidd
			fi
			}
			ins
		
		