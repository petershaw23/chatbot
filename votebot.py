#!/usr/bin/python3
#https://github.com/JoshuaSkelly/twitch-observer/wiki/Cookbook#voting
import votebot_token # imports local file with bot token (.gitignored, so create chatbot_token.py locally!). get twitch oauth from https://twitchapps.com/tmi/
import time
from twitchobserver import Observer

nick = 'budLAN_votebot'
channel = 'bud_lan'


votes = {}

def handle_event(event):
    if event.type != 'TWITCHCHATMESSAGE':
        return
        
    if event.message[0:2].upper() == '!Y':
        observer.send_message('counted YES!', channel)
        votes[event.nickname] = 1
        print('someone voted yes')
        
    elif event.message[0:2].upper() == '!N':
        observer.send_message('counted NO!', channel)
        votes[event.nickname] = -1
        print('someone voted no')

observer = Observer(nick, votebot_token.token)
observer.subscribe(handle_event)

observer.send_message('Vote !yes or !no. You have 60 seconds!', channel)

observer.start()
observer.join_channel(channel)
time.sleep(30)
observer.send_message('... 30 seconds left ...', channel)
time.sleep(30)
observer.unsubscribe(handle_event)

observer.send_message('Voting is over!', channel)

time.sleep(2)
tally = sum(votes.values())

if tally > 0:
    observer.send_message('The yeas have it!', channel)

elif tally < 0:
    observer.send_message('The nays have it!', channel)

else:
    observer.send_message('Its a draw!', channel)

observer.leave_channel(channel)
observer.stop()
