cd us*/pl*
ls |grep -c .py
cl="$(ls | grep -c .py)"
if [ "$cl" != "351" ];then
printf "\n Update available\n"
printf "\n\n Update command : `.update now`"
else
printf "\n Up to date\n"
fi