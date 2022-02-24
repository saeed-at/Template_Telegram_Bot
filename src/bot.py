import os
from termios import TIOCPKT_DOSTOP

import emoji
import requests
import telebot
from loguru import logger
from telebot import types

from src.constants import keyboards

class Bot:
        """
        Template For Telegram bot 
        """
        
        def __init__(self):
                self.bot = telebot.TeleBot(os.environ["anonymous_telebot_token"])
                # message_handler(func=lambda message: True) use self.echo_all as input for decrator and return it again
                # so we dont need to use message_handler(func=lambda message: True) before echo_all.(actually we can use
                # because we need to use self.echo_all out of def and this is not possible)
                self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)
                # self.send_fal = self.bot.message_handler(commands=['fal'])(self.send_fal)

        def run(self):
                logger.info("Bot is running")
                self.bot.infinity_polling()

        def echo_all(self, message):
                self.bot.send_message(message.chat.id, message.text, reply_markup = keyboards.main)
                print(emoji.demojize(message.text))
                #we can monitor user whom contact to bot by sending logs to out chat(1871265971 is my temporary chat)
                # self.bot.send_message('1871265971', f"{message.from_user.username} sent message to bot.\n message : {message.text}") 

# TODO  :Add faal feature to the bot
### faal hafez api
# @bot.message_handler(commands=['fal'])
# def send_fal(message):
#         logger.info(f"api request from user : {message.from_user.username}")
#         BASE_URL = 'https://one-api.ir/hafez/?token=946518:6216a532d23ae8.08076926'
#         response = requests.get(f"{BASE_URL}")
#         bot.reply_to(message,f"‍‍‍‍‍‍─┅━━━━┅─فال─┅━━━━┅─\n {response.json()['result']['RHYME']}\n ─┅━━━━┅─تعبیر─┅━━━━┅─\n {response.json()['result']['MEANING']}\n ")

if __name__ == "__main__":
        logger.info("Bot has been started!")
        bot = Bot()
        bot.run()
