import time
from twitchobserver import Observer
import chatbot_token # imports local file with bot token
token = chatbot_token.token
channel = 'bud_lan_b'
nick = 'bud_lan_b'

with Observer(nick, token) as observer:
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
