don() {
	for i in img.py my.py help.py code.py dp.py cmd.py actressdp.py live.py open.py repack.py cmd_list.py phone.py linux.py get_bot.py get_admin.py all.py get_id.py adduser.py dm.py; do
	wget https://raw.githubusercontent.com/rooted-cyber/good/master/cat/$i
	done
	}
	che() {
		rm ld
		wget https://raw.githubusercontent.com/rooted-cyber/good/master/cat/ld
		cat ld
		}
		check-bot() {
			ca=$(cat alive.py | grep -e Cat)
			if [ -z "$ca" ];then
			printf "\n\n First install cat userbot !!!\n\n"
			exit
			fi
			}
	printf "\n\n Downloaded and install all plugins\n\n"
	menu() {
		check-bot
		che
		cd us*/pl*
		rm eval*
		rm help.py
		don
		}
		menu