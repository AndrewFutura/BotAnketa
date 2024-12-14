from aiogram import F
from aiogram.types import Message, CallbackQuery
import setings

from setings.setings import dp
from setings.data_base import DB, Dict_raw_data_user

# из пaкета dialogs
from dialogs import dialogs_bot
from dialogs.questions import LIST_QUESTIONS

# из пакета фильтров
from filters.basic import *

# из пакета кнопок
from keybords.basic import INLINE_YES_NO_Q1, BUTTON_YES_NO_Q1, ReplyKeyboardRemove
from busienes_logic.basic import save_data_in_db, check_user
from setings.setings import USERS_QUESTION_NUMBER

__all__ = ['start',
           'write_fio',
           'heandler_no',
           'heandler_yes',
           'handlers_questions_text'] # для импорта только хэндлеров



@dp.message(CommandStart())
async def start(message: Message):
    """Команда старт, запуск бота"""
    await message.answer(text=dialogs_bot.WELCOME)
    print(message.from_user.id == 2087444504)

"""ОСНОВНОЙ ХЕНДЛЕР"""
@dp.message(filter_fio)
async def write_fio(message: Message):
    # проверка на регистрацию ранее
    if check_user(message.from_user.id):
        Dict_raw_data_user[message.from_user.id] = []
        Dict_raw_data_user[message.from_user.id].append(message.from_user.id) # сохраняем id
        Dict_raw_data_user[message.from_user.id].append(message.text) # сохраняем имя
        USERS_QUESTION_NUMBER[message.from_user.id] = 0
        await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]], reply_markup=BUTTON_YES_NO_Q1)
    else:
        await message.answer(dialogs_bot.ERROR_USER)
"""_________________________"""

"""ХЕНДЛЕР ДЛЯ ТЕСТА"""

@dp.message(filter_fio)
async def write_fio(message: Message):
    # проверка на регистрацию ранее

    Dict_raw_data_user[message.from_user.id] = []
    Dict_raw_data_user[message.from_user.id].append(message.from_user.id) # сохраняем id
    Dict_raw_data_user[message.from_user.id].append(message.text) # сохраняем имя
    USERS_QUESTION_NUMBER[message.from_user.id] = 0
    await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]])

"""_________________________"""
# print(type())



# @dp.message(F.data == 'answer_question_no')
# async def heandler_no(message: CallbackQuery):
#     '''Проверка вопроса "нет"'''
#
#     Dict_raw_data_user[message.from_user.id].append(False)
#     USERS_QUESTION_NUMBER[message.from_user.id] += 1 # номер следующего вопроса
#
#     if USERS_QUESTION_NUMBER[message.from_user.id] not in questions_index_filter_for_text:
#         await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]],
#                              reply_markup=INLINE_YES_NO_Q1)
#
#     else:
#         await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]])
#
#
#
# @dp.message(F.data == 'answer_question_yes')
# async def heandler_yes(message: CallbackQuery):
#     '''Проверка вопроса "да"'''
#
#     Dict_raw_data_user[message.from_user.id].append(True)
#     USERS_QUESTION_NUMBER[message.from_user.id] += 1 # номер следующего вопроса
#     print(USERS_QUESTION_NUMBER[message.from_user.id])
#
#
#     if USERS_QUESTION_NUMBER[message.from_user.id] not in questions_index_filter_for_text:
#         await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]],
#                              reply_markup=INLINE_YES_NO_Q1)
#
#     else:
#         await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]])

@dp.message(F.text == 'Да✅')
async def heandler_no(message: Message):
    '''Проверка вопроса "нет"'''
    try:
        if USERS_QUESTION_NUMBER[message.from_user.id] not in questions_index_filter_for_text:

            Dict_raw_data_user[message.from_user.id].append(False)
            USERS_QUESTION_NUMBER[message.from_user.id] += 1  # номер следующего вопроса

            if USERS_QUESTION_NUMBER[message.from_user.id] not in questions_index_filter_for_text:
                await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]],
                                 reply_markup=BUTTON_YES_NO_Q1)

            else:
                await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]],
                                     reply_markup=ReplyKeyboardRemove())
    except KeyError:
        await message.answer(dialogs_bot.ERROR_PASSING)


@dp.message(F.text == 'Нет❌')
async def heandler_yes(message: Message):
    '''Проверка вопроса "да"'''

    try:
        if USERS_QUESTION_NUMBER[message.from_user.id] not in questions_index_filter_for_text:
            Dict_raw_data_user[message.from_user.id].append(True)
            USERS_QUESTION_NUMBER[message.from_user.id] += 1  # номер следующего вопроса


            if USERS_QUESTION_NUMBER[message.from_user.id] not in questions_index_filter_for_text:
                await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]],
                                 reply_markup=BUTTON_YES_NO_Q1)

            else:
                await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]],
                                     reply_markup=ReplyKeyboardRemove())
    except KeyError:
        await message.answer(dialogs_bot.ERROR_PASSING)

@dp.message()
async def handlers_questions_text(message: Message):
    '''Проверка текстового вопроса'''
    try:
        if USERS_QUESTION_NUMBER[message.from_user.id] in questions_index_filter_for_text:
            Dict_raw_data_user[message.from_user.id].append(message.text)

            if USERS_QUESTION_NUMBER[message.from_user.id] == questions_index_filter_for_text[-1]:
                save_data_in_db(tuple(Dict_raw_data_user[message.from_user.id])) # регистрируем человека в БД, удаляем из словаря Dict_raw_data_user, USERS_QUESTION_NUMBER
                del Dict_raw_data_user[message.from_user]
                del USERS_QUESTION_NUMBER[message.from_user.id]
                await message.answer(text=dialogs_bot.THANKS_FOR_PASSING)
            else:
                USERS_QUESTION_NUMBER[message.from_user.id] += 1

                if USERS_QUESTION_NUMBER[message.from_user.id] not in questions_index_filter_for_text:
                    await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]],
                                         reply_markup=BUTTON_YES_NO_Q1)

                else:
                    await message.answer(text=LIST_QUESTIONS[USERS_QUESTION_NUMBER[message.from_user.id]],
                                         reply_markup=ReplyKeyboardRemove())

        else:
            await message.answer(dialogs_bot.ERROR_TEXT_QUESTION)

    except KeyError:
        await message.answer(dialogs_bot.ERROR_PASSING)



@dp.message()
async def end(message: Message):
    await message.answer(text=dialogs_bot.THANKS_FOR_PASSING)
    print(message.from_user.id == 2087444504)
