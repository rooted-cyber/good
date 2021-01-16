don() {
	for i in ld img.py my.py help.py code.py dp.py cmd.py actressdp.py live.py open.py repack.py cmd_list.py phone.py linux.py get_bot.py get_admin.py all.py get_id.py adduser.py dm.py; do
	wget https://raw.githubusercontent.com/rooted-cyber/good/master/cat/$i
	done
	}
	che() {
		rm ld
		wget https://raw.githubusercontent.com/rooted-cyber/good/master/cat/ld
		cat ld
		}
		check-bot() {
			cd us*/pl*
			ca=$(cat alive.py | grep -e Cat)
			if [ -z "$ca" ];then
			printf "\n\n First install cat userbot !!!\n\n"
			exit
			fi
			}
			icheck() {
				cd us*/pl*
				if [ -e ld ];then
				printf "\n\n Downloaded and install all plugins\n\n"
				else
				printf "\n\n Not install any plugings !!!\n\n"
				fi
				}
				
	menu() {
		check-bot
		che
		cd us*/pl*
		rm eval*
		rm help.py
		don
		icheck
		}
		menu