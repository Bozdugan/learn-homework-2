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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import API_KEY
import ephem
from ephem import *
from datetime import *

logging.basicConfig(filename='bot.log', level=logging.INFO)


def planet_info_answer(update, context):
    planets = {
        'Mercury': ephem.Mercury(),
        'Venus': ephem.Venus(),
        'Mars': ephem.Mars(),
        'Jupiter': ephem.Jupiter(),
        'Saturn': ephem.Saturn(),
        'Uranus': ephem.Uranus(),
        'Neptune': ephem.Neptune()
    }
    user_text = update.message.text
    user_planet = user_text.split(' ')[1]
    if user_planet in planets.keys():
        planet_data = planets.get(user_planet)
        planet_data.compute(datetime.now(tz=None))
        planet_position = constellation(planet_data)
        return update.message.reply_text(f'В данный момент планета {user_planet} находится в созвездии {planet_position}')
    else:
        return update.message.reply_text('Уточните имя планеты на английском')


def main():
    my_bot = Updater(API_KEY, use_context=True)

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler('planet', planet_info_answer))

    logging.info("Бот стартовал")
    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()

