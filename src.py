import os, sys
import time
try:
    from pygame import *
except:
    print("\n Installing Dependencies...")
    os.system("python3 -m pip install pygame")
    print(" Done.\n")
    time.sleep(1)
    os.system("clear")

logo = """
	 \033[1;33m         (                    
	  \033[1;33m(  (    )\ )  (              
	\033[1;33m  )\))(  (()/(  )\    )  (     
	\033[1;33m ((_)()\  /(_))((_)( /(  )\ )  
	\033[1;33m( ()((_)(_)) \033[1;32m _ \033[1;33m )(_))(()/(  
	\033[1;31m | __| \033[1;32m| _ \ | |\033[1;33m((_)_  )(_)) 
	\033[1;31m |__ \ \033[1;32m|  _/ | |/ _` || || | 
	\033[1;31m |___/ \033[1;32m|_|   |_|\__,_| \_, | 
	          \033[1;32m             |__/  \033[0;0m
\033[1;36m       CONTACT: https://linktr.ee/5HR3D
\033[1;32m --------------------------------------------
\033[1;32m  [\033[1;33m1\033[1;32m]\033[1;36mPause \033[1;32m[\033[1;33m2\033[1;32m]\033[1;36mPlay \033[1;32m[\033[1;33m3\033[1;32m]\033[1;36mReplay \033[1;32m[\033[1;33m4\033[1;32m]\033[1;36mExit \033[1;32m[\033[1;33m5\033[1;32m]\033[1;36mList 
\033[1;32m --------------------------------------------\033[1;0m"""

def menu():
    print(logo)
    x = input(" Enter Choice:> ")
    return x.strip()

def list_songs(songs):
    os.system("clear")
    print(logo)
    print('\033[1;36m List of songs in the present directory:\n\033[1;0m')
    for i, song in enumerate(songs):
        print(i+1, ". ", song)
    return int(input("\n\033[1;36m Enter the song number you want to play:> \033[1;33m"))

def action(songs,x):
    if x == '1':
        mixer.music.pause()
        print(" Status: Song Paused.")
    if x == '2':
        mixer.music.unpause()
        print(" Status: Song Playing.")
    if x == '3':
        mixer.music.play(-1)
        print(" Status: Replaying Song. ")
    if x == '4':
        mixer.music.stop()
        print(" Status: Quitting...")
        print(logo)
        print("\n Goodbyee!")
    if x == '5':
        mixer.music.load(songs[list_songs(songs)-1])
        mixer.music.play(-1)
        print(" Status: Listing songs.. ")

def play_music(songs,choice):
    mixer.init()
    mixer.music.load(songs[choice])
    mixer.music.play(-1)
    while mixer.music.get_busy():
        x = menu()
        os.system("clear")
        action(songs,x)

def check_baseDir():
    songs=[]
    if len(sys.argv)>1:
        baseDir = sys.argv[1]
    else:
        baseDir = None
    if baseDir:
        for items in os.listdir(os.chdir(baseDir)):
            if items.endswith('.mp3'):
                songs.append(items)            
    else:
        for items in os.listdir(os.getcwd()):
            if items.endswith('.mp3'):
                songs.append(items)
    songs.sort()
    return songs

def main():
    songs=check_baseDir()

    #If there are any songs in the directory
    if len(songs)>=1:
        os.system("clear")
        print(logo)
        try:
            choice=list_songs(songs)
            assert choice>=1
        except AssertionError:
            print('Please select at least one song')
        else:
            play_music(songs,choice-1)
    else:
        os.system("clear")
        print(logo)
        print('Sorry! There are no mp3s detected in your directory')
        print('Try stating another directory when you call this script.')

if __name__ == '__main__':
    main()