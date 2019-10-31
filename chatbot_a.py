
#!/usr/bin/python3
#documentation: https://github.com/joshuaskelly/twitch-observer
import time
import random
import os
from twitchobserver import Observer
import chatbot_token_a # imports local file with bot token (.gitignored, so create chatbot_token.py locally!). get twitch oauth from https://twitchapps.com/tmi/
time.sleep(17) #to wait for network connection @reboot (crontab)

channel = 'bud_lan'
nick = 'bud_lan'


# Define the messages to display.
messages = [
    "BudLAN. Kommen und Siegen.",
    "BudLAN = BestLAN",
    "Wer BudLAN sagt muss auch BudLBN sagen!",
    "Tommy stinkt.",
    "BudLAN. Oberhausens größtes ESPORTS event, seit 1938.",
    "BudLAN 2019. Get your tickets at www.budlan.de",
    "BudLAN. Oberhausens finest. Since 1938",
    "BudLAN. Just do it!",
    "BudLAN. Perfection.",
    "BudLAN. LANen macht frei",
    "BudLAN. Toasted.",
    "BudLAN. Hier kann man UNREAL TOURNAMENT SPIELEN!",
    "BudLAN: E-GAMING UNLIMITED"
]

# Send a message every 120 sec.
messageSendInterval = 120
currentTime = time.time()
lastTimeMessagedSend = currentTime

with Observer(nick, chatbot_token_a.token) as observer:
    observer.join_channel(channel)
    observer.send_message('Hallo. Ich bin ein Chat-Bot für den A-Stream. !commands zeigt alle meine Befehle. Tommy stinkt übrigens!', channel)

    while True:
        try:
            for event in observer.get_events():
                
                if event.type == 'TWITCHCHATMESSAGE' and event.nickname != observer._nickname and event.message:
                    if event.message == '!commands':
                        observer.send_message('Kommando-Liste: !help !newpoll', event.channel)
                    if event.message == '!help':
                        observer.send_message('versuch mal !commands', event.channel)
                    if event.message == '!newpoll':
                        os.system("python3 /home/pi/chatbot/votebot.py")
                        observer.send_message('starting new poll', event.channel)
                        
                if event.type == 'TWITCHCHATJOIN' and event.nickname != 'TwitchChatBot':
                    observer.send_message('🍺 Welcome {}!'.format(event.nickname), event.channel)
                        
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
