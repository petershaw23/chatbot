#!/usr/bin/python3
#https://github.com/JoshuaSkelly/twitch-observer/wiki/Cookbook#voting
import votebot_token # imports local file with bot token (.gitignored, so create chatbot_token.py locally!). get twitch oauth from https://twitchapps.com/tmi/

import goslate
from twitchobserver import Observer

gs = goslate.Goslate()

nick = 'budLAN_votebot'
channel = 'bud_lan'
native_lang_id = 'en'

with Observer(nick, votebot_token.token) as observer:
    observer.join_channel(channel)

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE' and event.nickname != observer._nickname and event.message:
                    language_id = gs.detect(event.message)

                    if language_id != native_lang_id:
                        translation = gs.translate(event.message, native_lang_id)
                        language_name = gs.get_languages()[language_id]

                        observer.send_whisper(nick, '{}({}): {}'.format(event.nickname, language_name, translation))

        except KeyboardInterrupt:
            observer.leave_channel(channel)
