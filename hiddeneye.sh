clear
ll="e"
saf="clear"
i="c"
k="h"
h="o"
o="-e"
lal="\033[91m"
bulu_me="\033[94m"
ajib_me="\033[96m"
dd="$lal[+]$ajib_me Remove python......"
pila_me="\033[93m"
hara_me="\033[92m"
ee="$bulu[+]$hara_me Installing python....."
ajib_me="\033[1;96m"
gg="$lal[+]$bulu_me Installing Requirements......"
nhi_pta="\033[95m"
ff="$pila[+]$ajib_me Cloning Hiddeneye........"
cc="$pila[+]$hara_me Installing git......."
so_jao="sleep"
bb="$nhi_pta[+]$ajib_me Now updating........"
aa="$bulu_me[+]$hara_me Old HiddenEye deleting......"
cd ~
$ll$i$k$h $o "$aa"
rm -Rf HiddenEye
$so_jao 1
$saf
$ll$i$k$h $o "$bb"
$so_jao 1
apt update
apt upgrade
$saf
$ll$i$k$h $o "$cc"
$so_jao 1
apt install git
$saf
$ll$i$k$h $o "$dd"
$so_jao 1
apt remove python
$saf
$ll$i$k$h $o "$ee"
$so_jao 1
apt install python
$saf
$ll$i$k$h $o "$ff"
$so_jao 1
git clone -b Termux-Support-Branch https://github.com/DarkSecDevelopers/HiddenEye.git
$saf
cd HiddenEye
$ll$i$k$h $o "$gg"
pip3 install wget
$ll$i$k$h $o "$hara Press enter to open Hiddeneye"
read
python3 HiddenEye.py