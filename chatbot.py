
#!/usr/bin/python3
#documentation: https://github.com/joshuaskelly/twitch-observer
import time
import os
from twitchobserver import Observer
import chatbot_token # imports local file with bot token (.gitignored, so create chatbot_token.py locally!). get twitch oauth from https://twitchapps.com/tmi/
time.sleep(15)
channel = 'bud_lan_b'
nick = 'bud_lan_b'

with Observer(nick, chatbot_token.token) as observer:
    observer.join_channel(channel)
    observer.send_message('Hallo. Ich bin ein Chat-Bot. !commands zeigt alle meine Befehle. Tommy stinkt übrigens!', channel)

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE' and event.nickname != observer._nickname and event.message:
                    if event.message == '!commands':
                        observer.send_message('es gibt noch keine commands, ausser !help', event.channel)
                    if event.message == '!help':
                        observer.send_message('versuch mal !commands', event.channel)
                    if event.message == '!demo1':
                        os.system('sudo systemctl stop lightdm')
                        os.system('pkill retroarch')
                        os.system('pkill emulation*')
                        observer.send_message('demo1 start', event.channel)
                        os.system("bash /home/pi/pi-music-bot/twitch1.sh &")

            time.sleep(1)

        except KeyboardInterrupt:
            observer.send_message('Bye. P.S.: Tommy ist doof.', channel)
            observer.leave_channel(channel)
            break
