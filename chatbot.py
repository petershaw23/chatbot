
#!/usr/bin/python3
#documentation: https://github.com/joshuaskelly/twitch-observer
import time
from twitchobserver import Observer
import chatbot_token # imports local file with bot token (.gitignored, so create chatbot_token.py locally!). get twitch oauth from https://twitchapps.com/tmi/

channel = 'bud_lan_b'
nick = 'bud_lan_b'

with Observer(nick, chatbot_token.token) as observer:
    observer.join_channel(channel)
    observer.send_message('Hallo. Ich bin ein Chat-Bot. !commands zeigt alle meine Befehle. Tommy stinkt übrigens!', channel)

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE':
                    observer.send_message(event.message, event.channel)

            time.sleep(1)

        except KeyboardInterrupt:
            observer.send_message('Bye. P.S.: Tommy ist doof.', channel)
            observer.leave_channel(channel)
            break
