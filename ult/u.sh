cd addons
dow() {
	for a in bins.py cemoji.py uspam.py fonts2.py poto.py mark.py pm.py nekobot.py read.py loads.py anim.py em.py bots2.py tss.py dp.py check2.py;do
wget https://raw.githubusercontent.com/rooted-cyber/good/master/ult/$a
done
}
if [ -e check2.py ];then
printf "Already downloaded files \n\n"
printf "\n Load this file \n
bins
cemoji
uspam
fonts2
poto
mark
pm
nekobot
read
anim
bots2
dp
check2"
else
printf "\n Downloading plugins\n"
dow
fi
if [ -e dp.py ];then
printf "\n\n`.load dp`"
fi
if [ -e tss.py ];then
printf "\n\n Installing gtts \n\n"
sleep 1
pip install gtts
fi
