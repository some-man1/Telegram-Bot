from telebot import *
import requests

#-------put your API token here--------------
bot = telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id,"""
    
    /start ---> start the bot 
    /Link ---> start the service
    /MyWebsite ---> https://bitly.ws/Tjyx
    /SourceCode ---> 
    """)

def short(link):
    API = "https://api.shrtco.de/v2/shorten?url="
    respon = requests.get(f"{API}{link}")
    shorted_links = respon.json()
    x = shorted_links["result"]["full_short_link"]
    x2 = shorted_links["result"]["full_short_link2"]
    x3 = shorted_links["result"]["full_short_link3"]
    return x, x2,x3

@bot.message_handler(commands=["Link"])
def Link(message):
    bot.send_message(message.chat.id, "")


@bot.message_handler(commands=["SourceCode"])
def Link(message):
    bot.send_message(message.chat.id, "")




@bot.message_handler(func=lambda message: True)
def main(message):
    if "http" in message.text or "." in message.text:
        url1,url2,url3 = short(message.text)
        bot.send_message(message.chat.id, "لديك ثلاث روابط مقصرة")
        bot.send_message(message.chat.id, f"{url1}")
        bot.send_message(message.chat.id, f"{url2}")
        bot.send_message(message.chat.id, f"{url3}")
    else:
        bot.send_message(message.chat.id, "اكتب اسم موقع حقيقي")


bot.infinity_polling()

