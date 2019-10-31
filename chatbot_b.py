
#!/usr/bin/python3
#documentation: https://github.com/joshuaskelly/twitch-observer
import time
import random
import os
from twitchobserver import Observer
import chatbot_token_b # imports local file with bot token (.gitignored, so create chatbot_token.py locally!). get twitch oauth from https://twitchapps.com/tmi/
time.sleep(15) #to wait for network connection @reboot (crontab)

channel = 'bud_lan_b'
nick = 'bud_lan_b'

# Define the messages to display.
messages = [
    "BudLAN. So geht gaming heute! Auch hier im B-Stream",
    "BudLAN = BestLAN. Selbst im B-Stream noch besser als Dreamhack.",
    "Wer BudLA-STREAM sagt muss auch BudLB-STREAM sagen!",
    "BudLAN. Oberhausens finest. Since 1938"
]

# Send a message every 120 sec.
messageSendInterval = 120
currentTime = time.time()
lastTimeMessagedSend = currentTime


with Observer(nick, chatbot_token_b.token) as observer:
    observer.join_channel(channel)
    observer.send_message('Hallo. Ich bin ein Chat-Bot für den B-Stream. !commands zeigt alle meine Befehle. Tommy stinkt übrigens!', channel)

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE' and event.nickname != observer._nickname and event.message:
                    if event.message == '!commands':
                        observer.send_message('Kommando-Liste: !demo1  !demo2  !demo3  !demo4 !demo5 !snes !test !exit', event.channel)
                    if event.message == '!help':
                        observer.send_message('versuch mal !commands', event.channel)
                    if event.message == '!demo1':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        os.system('pkill ffmpg*')
                        observer.send_message('demo1 start', event.channel)
                        os.system("bash /home/pi/pi-music-bot/twitch1.sh &")
                    if event.message == '!demo2':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        os.system('pkill ffmpg*')
                        observer.send_message('demo2 start', event.channel)
                        os.system("bash /home/pi/pi-music-bot/twitch2.sh &")
                    if event.message == '!demo3':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        os.system('pkill ffmpg*')
                        observer.send_message('demo3 start!', event.channel)
                        os.system("bash /home/pi/pi-music-bot/twitch3.sh &")
                    if event.message == '!demo4':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        os.system('pkill ffmpg*')
                        observer.send_message('demo4 start!', event.channel)
                        os.system("bash /home/pi/pi-music-bot/twitch4.sh &")
                    if event.message == '!demo5':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        os.system('pkill ffmpg*')
                        observer.send_message('demo5 start!', event.channel)
                        os.system("bash /home/pi/pi-music-bot/twitch5.sh &")    
                    if event.message == '!snes':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        os.system('pkill ffmpg*')
                        observer.send_message('snes start', event.channel)
                        os.system("bash /home/pi/pi-music-bot/snes.sh &")
                    if event.message == '!test':
                        os.system('pkill retroarch')
                        os.system('pkill snes.sh')
                        os.system('pkill twitch1.sh')
                        os.system('pkill twitch2.sh')
                        os.system('pkill twitch3.sh')
                        os.system('pkill twitch4.sh')
                        os.system('pkill twitch5.sh')
                        os.system('pkill ffmpg*')
                        os.system("bash /home/pi/FFMpeg/test.sh &")
                        os.system("bash /home/pi/FFMpeg/test_a.sh &")
                        os.system("bash /home/pi/FFMpeg/test_c.sh &")
                        observer.send_message('test streams started!', event.channel)
                    if event.message == '!exit':
                        os.system('pkill retroarch')
                        os.system('pkill snes.sh')
                        os.system('pkill twitch1.sh')
                        os.system('pkill twitch2.sh')
                        os.system('pkill twitch3.sh')
                        os.system('pkill twitch4.sh')
                        os.system('pkill twitch5.sh')
                        os.system('pkill ffmpg*')
                        observer.send_message('quitting all streams', event.channel)                       
            currentTime = time.time()
            if currentTime - lastTimeMessagedSend >= messageSendInterval:
                randomMessage = messages[random.randint(0, len(messages) - 1)]
                observer.send_message(randomMessage, channel)
                lastTimeMessagedSend = currentTime
    
            time.sleep(0.3)

 

        except KeyboardInterrupt:
            observer.send_message('Bye. P.S.: Tommy ist doof.', channel)
            observer.leave_channel(channel)
            break
