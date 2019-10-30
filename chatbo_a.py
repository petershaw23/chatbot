
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
    "This is an example message to be displayed in chat.",
    "This is an example message that has an URL in it: https://github.com/JoshuaSkelly/twitch-observer/",
    "This is a very very very very very very very very very very very very very very very very very very very very very very very very very long message. Probably too long :)"
]

# Send a message every 3 minutes.
messageSendInterval = 3 * 60


with Observer(nick, chatbot_token_b.token) as observer:
    observer.join_channel(channel)
    observer.send_message('Hallo. Ich bin ein Chat-Bot für den A-Stream. !commands zeigt alle meine Befehle. Tommy stinkt übrigens!', channel)

    while True:
    
        try:
            currentTime = time.time()

            if currentTime - lastTimeMessagedSend >= messageSendInterval:
                randomMessage = messages[random.randint(0, len(messages) - 1)]
                observer.send_message(randomMessage, "channel")

                lastTimeMessagedSend = currentTime
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE' and event.nickname != observer._nickname and event.message:
                    if event.message == '!commands':
                        observer.send_message('!demo1 !demo2 !snes !exit', event.channel)
                    if event.message == '!help':
                        observer.send_message('versuch mal !commands', event.channel)
                    if event.message == '!demo1':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        observer.send_message('demo1 start', event.channel)
                        os.system("bash /home/pi/pi-music-bot/twitch1.sh &")
                    if event.message == '!demo2':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        observer.send_message('demo2 start', event.channel)
                        os.system("bash /home/pi/pi-music-bot/twitch2.sh &")
                    if event.message == '!snes':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        observer.send_message('snes start', event.channel)
                        os.system("bash /home/pi/pi-music-bot/snes.sh &")
                    if event.message == '!exit':
                        os.system('pkill retroarch')
                        os.system('pkill snes.sh')
                        os.system('pkill twitch1.sh')
                        os.system('pkill twitch2.sh')
                        observer.send_message('exiting emulation', event.channel)

            time.sleep(0.3)

        except KeyboardInterrupt:
            observer.send_message('Bye. P.S.: Tommy ist doof.', channel)
            observer.leave_channel(channel)
            break
