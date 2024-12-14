import aiogram
from aiogram.fsm.state import StatesGroup, State
from dialogs import questions

class Form(StatesGroup):
    FIO = State()
    questions.LIST_QUESTIONS = State()
    End = State()
    