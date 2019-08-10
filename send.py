# code by mrsploit
# Jailbreak & Root TM
# jilrot.com
# t.me/jailbreakandroot
import telebot, sys

f = open("bot-data.txt","r").read().splitlines()
for d in f:
    df = d.split("$")
    token = df[0]
    chat_id = df[1]
    loc = sys.argv[1].split(":")
    bot = telebot.TeleBot(token)
    bot.send_location(chat_id, loc[0], loc[1])
