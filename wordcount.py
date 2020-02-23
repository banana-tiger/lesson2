"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import string

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {
    'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = "Вызван /start"
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def count_words(bot, update):
    user_text = update.message.text.split()
    words_counted = 0
    for word in user_text:
        splitted_word = word.split()
        for letter in splitted_word:
            if letter in string.ascii_letters.split():
                words_counted +=1
    print(words_counted)
    update.message.reply_text(words_counted)

def main():
    mybot = Updater("1059535934:AAEogOPYQZ3fAA2u5VCoOWRMJdDCFe-PciU", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, count_words))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
