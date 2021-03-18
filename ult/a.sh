downn() {
for a in __pycache__.py fonts.py funts.py functions.py progress.py memeifyhelpers.py progress.py qhelper.py __init__.py;do
wget https://raw.githubusercontent.com/Sh1vam/javes-3.0/master/ub/helpers/$a
done
}
if [ -e pyfile ];then
cd pyfile
downn
else
mkdir pyfile
cd pyfile
downn
fi
