from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from BotAnketa.main import dp
from dialogs import dialogs_bot
from dialogs import questions
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keybords import basic
from aiogram import User
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils import executor
from dialogs import dialogs_bot
from dialogs.questions import LIST_QUESTIONS
from filters.basic import *
from aiogram import F
from aiogram.types import Message, CallbackQuery


QUESTIONS = questions.LIST_QUESTIONS

class checkstate(StatesGroup):
    QUESTIONS = State()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(text=dialogs_bot.WELCOME)
    print(message.from_user.id == 2087444504)

async def ask_next_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    current_question = data['current_question']

    if current_question < len(QUESTIONS):
        question = QUESTIONS[current_question]


    if question["type"] == 'text':
        await message.answer(question["text"], reply_markup=ReplyKeyboardRemove())

    elif question["type"] == "bool":
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(KeyboardButton("Да"), KeyboardButton("Нет"))
            await message.answer(question["text"], reply_markup=keyboard)



