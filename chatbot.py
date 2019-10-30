import time
from twitchobserver import Observer
import chatbot_token # imports local file with bot token
token = chatbot_token.token
channel = 'bud_lan_b'
nick = 'bud_lan_b'

with Observer(nick, token) as observer:
    observer.join_channel(channel)
    observer.send_message('Hello', channel)

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE':
                    observer.send_message(event.message, event.channel)

            time.sleep(1)

        except KeyboardInterrupt:
            observer.send_message('Bye', channel)
            observer.leave_channel(channel)
            break
