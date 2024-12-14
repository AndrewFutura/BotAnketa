from setings.setings import dp
from aiogram import F
from aiogram.types import Message, CallbackQuery
from filters.basic import checkId

@dp.message(checkId, commands=['statistic'])
async def get_statistic():
    pass

