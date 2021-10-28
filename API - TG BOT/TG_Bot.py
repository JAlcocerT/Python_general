# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:18:25 2021

@author: jesus.tagua
"""

#Look for @GodFather Bot in Telegram
#write in the chat: /start
#then: /newbot
#name it and give at an username
#You will find it at t.me/TG_downloads_bot.
#also, tg will provide the access token to the hhtp API in the form: 
#Keep your token secure and store it safely, it can be used by anyone to control your bot.

#For a description of the Bot API, see this page: https://core.telegram.org/bots/api

#To see the options, the following are needed for the bot to be part of groups: Botsettings
#/setjoingroups
#/setprivacy



#It will give information of any message that has been sent to the bot:
#https://api.telegram.org/bot9999999999:AAAAAABBBBBBBBCCCCCCDDDDEEEEEEFFFFF/getUpdates

#Add the bot to a group chat
#From there we can take chat details: CHAT_to_TEST
#"chat":{"id":-999999999,"title":"chat_t","type":"group","all_members_are_administrators":true},
#chat id: -999999999



#pip install requests
import requests
import time

#list of possible jokes

text_to_send = ['Trying first sentence. ',
'It can work with 12345 too.'
]

#print(text_to_send)

#https://api.telegram.org/bot9999999999:AAAAAABBBBBBBBCCCCCCDDDDEEEEEEFFFFF/
#base_url = 'https://api.telegram.org/bot<<token>>/sendMessage?chat_id=-999999999&text="

#test a sample message by browsing:
#https://api.telegram.org/bot9999999999:AAAAAABBBBBBBBCCCCCCDDDDEEEEEEFFFFF/sendMessage?chat_id=-548977370&text=your_sample_message

for item in text_to_send:
    base_url = 'https://api.telegram.org/bot9999999999:AAAAAABBBBBBBBCCCCCCDDDDEEEEEEFFFFF/sendMessage?chat_id=-999999999&text="{}"'.format(item) 
    requests.get(base_url) #it calls the url
    time.sleep(15) #seconds
    