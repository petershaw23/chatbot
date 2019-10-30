#!/usr/bin/python3

import chatbot_token # imports local file with bot token
token = chatbot_token.token

HOST = "irc.twitch.tv"              # the Twitch IRC server
PORT = 6667                         # always use port 6667!
NICK = "twitch_username"            # your Twitch username, lowercase
PASS = token                        # your Twitch OAuth token
CHAN = "#bud_lan_b"                 # the channel you want to join
RATE = (20/30)                      # messages per second
