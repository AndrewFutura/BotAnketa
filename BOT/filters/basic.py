from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from setings.data_base import Dict_raw_data_user
from setings.setings import ID_ADMIN_our

import re

__all__ = ['CommandStart',
           'Command',
           'filter_fio',
           'questions_index_filter_for_text',
           'return_question']

questions_index_filter_for_text = [2, 4, 6, 7, 10]


def filter_fio(message: Message):
    try:
        Dict_raw_data_user[message.from_user.id]
        # проверка пользователя на БД
    except KeyError: # Если человека нет в словаре, то мы проверяем его имя
        reg = r'[А-Я]{1}[а-я]+ [А-Я]{1}[а-я]+ [А-Я]{1}[а-я]+'
        res = re.match(reg, message.text)
        if res is None:
            return False
        else:
            return True
    else:
        return False


def return_question(Number_question):
    # отправка следующего вопроса
    if Number_question not in questions_index_filter_for_text:
        # возвращаем "no_yes", если следующий вопрос не текстовый
        return "no_yes"
    else:
        return 'text'



def checkId(message: Message):
    if message.from_user.id == ID_ADMIN_our:
        return True
    else:
        return False



