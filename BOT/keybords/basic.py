from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


INLINE_YES_NO_Q1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да✅', callback_data='answer_question_yes')],
                    [InlineKeyboardButton(text='Нет❌', callback_data='answer_question_no')]])


BUTTON_YES_NO_Q1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Да✅'),
                                                  KeyboardButton(text='Нет❌')]],
                                       resize_keyboard=True)

# INLINE_YES_NO_Q2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да✅', callback_data='answer_question2')],
#                     [InlineKeyboardButton(text='Нет❌', callback_data='answer_question2')]])
#
#
# INLINE_YES_NO_Q4 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да✅', callback_data='answer_question4')],
#                     [InlineKeyboardButton(text='Нет❌', callback_data='answer_question4')]])
#
# INLINE_YES_NO_Q6 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да✅', callback_data='answer_question6')],
#                     [InlineKeyboardButton(text='Нет❌', callback_data='answer_question6')]])
#
# INLINE_YES_NO_Q9 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да✅', callback_data='answer_question9')],
#                     [InlineKeyboardButton(text='Нет❌', callback_data='answer_question9')]])
#
# INLINE_YES_NO_Q10 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да✅', callback_data='answer_question10')],
#                     [InlineKeyboardButton(text='Нет❌', callback_data='answer_question10')]])