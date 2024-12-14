import setings
from setings.setings import bot, dp
from setings.setings import dp

# импорт хендлеров
from handlers.basic import *


if __name__ == '__main__':
    dp.run_polling(bot)

