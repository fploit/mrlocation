#/usr/bin/env python3
# code by mrsploit
# mrlocation v2
# t.me/ZoneH
import telebot, sys

try:
    
    f = open("bot-data.txt","r").read().splitlines()
    for d in f:
        df = d.split("$")
        token = df[0]
        chat_id = df[1]
        loc = sys.argv[1].split(":")
        bot = telebot.TeleBot(token)
        bot.send_location(chat_id, loc[0], loc[1])

except Exception as e:
    print(e)
