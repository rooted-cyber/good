cd us*/pl*
ls |grep -c .py
cl="$(ls | grep -c .py)"
if [ "$cl" != "352" ];then
printf "\n Update available\n"
printf "\n\n Update This"
else
printf "\n Up to date\n"
fi