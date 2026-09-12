from aiogram.fsm.state import State,StatesGroup
class InfoState(StatesGroup):
    last_name  = State()
    first_name = State()
    age = State()