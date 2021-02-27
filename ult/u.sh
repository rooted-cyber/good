cd addons
do() {
	for a in anim.py em.py bots.py tss.py dp.py check2.py screenshot.py;do
wget https://raw.githubusercontent.com/rooted-cyber/good/master/ult/$a
done
}
if [ -e check2.py ];then
printf "Already downloaded files \n\n"
else
printf "\n Downloading plugins\n"
do
fi
if [ -e dp.py ];then
printf "\n\n
`.load dp`"
fi
if [ -e tss.py ];then
printf "\n\n Installing gtts \n\n"
sleep 1
pip install gtts
fi
