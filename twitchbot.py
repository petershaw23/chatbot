#!/usr/bin/python3

import socket
import string
import random
import time
import json
import threading
import os
import traceback
import re
import requests
import sys
import datetime
import chatbot_token # imports local file with bot token
token = chatbot_token.token
time.sleep(15)

#pulls channel name from the commandline. if there is no arg, channel name defaults to bud_lan_b
try:
    CHAN = sys.argv[1]
except:
    CHAN = 'bud_lan_b'
    
# connecting to Twitch IRC 
HOST = "irc.twitch.tv"  
NICK = "bud_lan_b"  
PORT = 6667

try:
    PASS = sys.argv[2]
except:
    PASS = token #get token from chatbot_token.py (.gitignored!)

readbuffer = ""
MODT = False

CHANNEL_NAME = CHAN
CHANNEL_NAME = CHANNEL_NAME.lower()
SLEEP_TIME = 120
IRC_CHANNEL = "#" + CHANNEL_NAME

# Connecting to Twitch IRC by passing credentials and joining a certain channel
s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS %s\r\n" % PASS, "UTF-8"))
s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("JOIN #%s\r\n" % CHAN, "UTF-8"))
s.send(bytes("CAP REQ :twitch.tv/membership\r\n", "UTF-8"))
s.send(bytes("CAP REQ :twitch.tv/commands\r\n", "UTF-8"))
s.send(bytes("CAP REQ :twitch.tv/tags\r\n", "UTF-8"))

def socketconnection():
    global s, HOST, PORT, NICK, CHAN 
    try:
        s.close()
        s.socket.socket()
        s.connect((HOST, PORT))
        s.send(bytes("PASS %s\r\n" % PASS, "UTF-8"))
        s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
        s.send(bytes("JOIN #%s\r\n" % CHAN, "UTF-8"))
        s.send(bytes("CAP REQ :twitch.tv/membership\r\n", "UTF-8"))
        s.send(bytes("CAP REQ :twitch.tv/commands\r\n", "UTF-8"))
        s.send(bytes("CAP REQ :twitch.tv/tags\r\n", "UTF-8"))
    except:
        print(traceback.format_exc())


def puppet():
    try:
        while True:
            message = input(' assuming direct control: ') 
            sendmessage(message)
            commands(message, 'bud_lan_b')
    except BrokenPipeError:
        socketconnection()
        

def sendmessage(text):
    # Method for sending a message
    s.send(bytes("PRIVMSG #" + CHAN + " :" + str(text) + "\r\n", "UTF-8"))

def commands(message, username):
    
    if message == "!commands":
        sendmessage("!demo1 !demo2 !snes !exit !meme !github !whoami")
    if message == "!help":
        sendmessage("!demo1 !demo2 !snes !exit !meme !github !whoami")
        
    if message == "!demo1":
        os.system('sudo systemctl stop lightdm')
        os.system('pkill retroarch')
        os.system('pkill emulation*')  
        os.system("bash /home/pi/pi-music-bot/twitch1.sh &")
        sendmessage("demo 1 starting!")
        

    if message == "!demo2":
        os.system('sudo systemctl stop lightdm')
        os.system('pkill retroarch')
        os.system('pkill emulation*')  
        os.system("bash /home/pi/pi-music-bot/twitch2.sh &")
        sendmessage("demo 2 starting!")


    if message == "!snes":
        os.system('sudo systemctl stop lightdm')
        os.system('pkill retroarch')
        os.system('pkill emulation*')  
        os.system("bash /home/pi/pi-music-bot/snes.sh &")
        sendmessage("snes starting!")
        
    if message == "!exit":
        os.system('pkill retroarch')
        sendmessage("exiting emulators!")        
        
    if message == "!meme":
        sendmessage("EleGiggle")

    if message == "!whoami":
        sendmessage(username)

    if message == '!github':
        sendmessage('https://github.com/petershaw23/twitch-chat/')

sendmessage('HeyGuys')

t = threading.Thread(target=puppet).start()

def messageloop():
    while True:
        global s, readbuffer
        
        try:
            readbuffer = readbuffer+s.recv(1024).decode("UTF-8") 
        except KeyboardInterrupt:
            raise
        except:
           print(traceback.format_exc())   
        
        temp = str.split(readbuffer, "\r\n")
        readbuffer = temp.pop()
               
        for line in temp:
            if(line[0] == "PING"):
                s.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))
            else:
                parts = str.split(line, ":")

                try:
                    message = parts[2][:len(parts[2])]
                    
                except:
                    message = ""

                usernamesplit = str.split(parts[1], "!")
                username = usernamesplit[0]

                
                
                print(username + ": " + message)
                commands(message.lower(), username.lower())

while True:
    try:
        messageloop()
    except KeyboardInterrupt:
        raise 
    except:
        print(traceback.format_exc())
        socketconnection()
        messageloop()
