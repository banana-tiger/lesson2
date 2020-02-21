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
import ephem

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
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def receive_planet(bot, update):
    test_dict = {"Mercury": ephem.Mercury('2020/01/01'), "Venus": ephem.Venus('2020/01/01'), "Mars": ephem.Mars('2020/01/01'),
                 "Jupiter": ephem.Jupiter('2020/01/01'), "Saturn": ephem.Saturn('2020/01/01'), "Uranus": ephem.Uranus('2020/01/01'),
                 "Neptune": ephem.Neptune('2020/01/01'), "Pluto": ephem.Pluto('2020/01/01')}
    text = update.message.text
    try:
        user_planet = update.message.text.split()[1]
        constellation = ephem.constellation(test_dict[user_planet])
        update.message.reply_text(f"Планета {user_planet} находится в созвездии {constellation[1]}")
    except KeyError:
        update.message.reply_text(f"{user_planet} нет в списке, попробуйте ввести планету еще раз")

 

def main():
    mybot = Updater("1059535934:AAEogOPYQZ3fAA2u5VCoOWRMJdDCFe-PciU", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", receive_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
