import time
from twitchobserver import Observer
import chatbot_token # imports local file with bot token
token = chatbot_token.token

with Observer('bud_lan_b', token) as observer:
    observer.join_channel('bud_lan_b')

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE':
                    observer.send_message(event.message, event.channel)

            time.sleep(1)

        except KeyboardInterrupt:
            observer.leave_channel('channel')
            break
