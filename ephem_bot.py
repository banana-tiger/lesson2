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
import datetime

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
    text = f'Привет! С помощью этого бота вы можете посмотреть в каком созвездии сейчас находится та или иная планета солнечной системы.' \
           f'Просто введите команду /planet вместе с одной из следующих планет: Mercury, Venus, Mars, Jupiter, Saturn, ' \
           f'Uranus, Neptune, Pluto. Команду вводите одной строкой, например "/planet Mars"'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = "Введите команду /start"
    print(user_text)
    update.message.reply_text(user_text)


def get_today():
    today = datetime.date.today().strftime("%Y/%m/%d")
    return today


def receive_planet(bot, update):
    today_str = datetime.date.today().strftime("%Y/%m/%d")
    planets_dict = {"Mercury": ephem.Mercury(), "Venus": ephem.Venus(),
                    "Mars": ephem.Mars(),
                    "Jupiter": ephem.Jupiter(), "Saturn": ephem.Saturn(),
                    "Uranus": ephem.Uranus(),
                    "Neptune": ephem.Neptune(), "Pluto": ephem.Pluto()}
    #text = update.message.text
    #try:

    splitted_input = update.message.text.split()
    if len(splitted_input) <2:
       update.message.reply_text(f"Введите команду /planet и искомую планету одной строкой")

    input_planet = update.message.text.split()[1]

    if input_planet not in planets_dict:
        update.message.reply_text(f"{input_planet} нет в списке, попробуйте ввести планету еще раз")
        return
    user_planet = planets_dict[input_planet]
    user_planet.compute(today_str)
    constellation = ephem.constellation(user_planet)
    update.message.reply_text(f"Сегодня планета {input_planet} находится в созвездии {constellation[1]}")
    #except KeyError:
        #update.message.reply_text(f"{user_planet} нет в списке, попробуйте ввести планету еще раз")

def receive_full_moon_date(bot, update):
    trash_list = [",", ".", "\\", "-"]
    splitted_user_text = update.message.text.split()[1]
    for word in splitted_user_text:
        for symbol in word:
            if symbol in trash_list:
                splitted_user_text = splitted_user_text.replace(symbol, "/")
            else:
                break
    splitted_date = splitted_user_text.split("/")

    for index, number in enumerate(splitted_date):
        if len(number) > 3:
            year = splitted_date.pop(index)
            if index == 0:
                month = splitted_date.pop(index + 1)
                day = splitted_date.pop()
            elif index == 2:
                month = splitted_date.pop(index - 1)
                day = splitted_date.pop(index - 2)
        else:
            continue


    correct_date_for_fullmoon = "/".join([year, month, day])
    update.message.reply_text(f"Следующее полнолуние состоится {ephem.next_full_moon(correct_date_for_fullmoon)}")

def main():
    mybot = Updater("1059535934:AAEogOPYQZ3fAA2u5VCoOWRMJdDCFe-PciU", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", receive_planet))
    dp.add_handler(CommandHandler("next_full_moon", receive_full_moon_date))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
