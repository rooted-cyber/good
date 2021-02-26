cd addons
for a in anim.py dp.py check2.py screenshot.py;do
wget https://raw.githubusercontent.com/rooted-cyber/good/master/ult/$a
done
if [ -e dp.py ];then
printf "Downloaded all files"
fi
