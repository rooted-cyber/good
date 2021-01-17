don() {
	for i in ld pastebinn.py screenlong.py hel.py dp.py cm2.py open.py repack.py; do
	wget https://raw.githubusercontent.com/rooted-cyber/good/master/dc/$i
	done
	cd /app/userbot
	for j in ut.py jconfig.py; do
	wget https://raw.githubusercontent.com/rooted-cyber/good/master/dc/$j
	done
	}
	che() {
		rm ld
		wget https://raw.githubusercontent.com/rooted-cyber/good/master/dc/ld
		cat ld
		}
		check-bot() {
			cd us*/pl*
			pwd
			ls ali*
			cat alive.py | grep -e dark
			ca=$(cat alive.py | grep -e dark)
			if [ -z "$ca" ];then
			printf "\n\n First install  dark cobra userbot !!!\n\n"
			exit
			fi
			}
			icheck() {
				cd us*/pl*
				if [ -e ld ];then
				printf "\n\n Downloaded and install all plugins\n\n"
				else
				printf "\n\n Not install any plugins !!!\n\n"
				fi
				}
				
	menu() {
		check-bot
		che
		cd us*/pl*
		don
		icheck
		}
		menu