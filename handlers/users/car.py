from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from keyboard.repaykeyboard.carkeyboard import b_type, b_oddiy, b_inamarka, b_elektro
from states.carstates import CarState

router = Router()

@router.message(Command("car"))
async def car(msg: types.Message, state: FSMContext):
    n = "Avto Salonga xush kelibsiz, mashina turini tanlang!"
    await msg.answer(n, reply_markup=b_type.as_markup(resize_keyboard=True))
    await state.set_state(CarState.type)

@router.message(CarState.type)
async def car_type(msg: types.Message, state: FSMContext):
    if msg.text == "oddiy":
        kb = b_oddiy
    elif msg.text == "elektro":
        kb = b_elektro
    elif msg.text == "inamarka":
        kb = b_inamarka
    else:
        await msg.answer("Iltimos, menyudan birini tanlang!")
        return
    await msg.answer(f"{msg.text} mashinalardan birini tanlang", reply_markup=kb.as_markup())
    await state.update_data(type=msg.text)
    await state.set_state(CarState.car_name)

@router.message(CarState.car_name)
async def car_name(msg: types.Message, state: FSMContext):
    await state.update_data(car_name=msg.text)
    await msg.answer("Mashina rangini kiriting:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(CarState.color)

@router.message(CarState.color)
async def car_color(msg: types.Message, state: FSMContext):
    await state.update_data(color=msg.text)
    await msg.answer("Mashina ishlab chiqarilgan yilini kiriting:")
    await state.set_state(CarState.year)

    @router.message(CarState.year)
    async def car_year(msg: types.Message, state: FSMContext):
        if not msg.text.isdigit() or not (1990 <= int(msg.text) <= 2026):
            await msg.answer("Yilni to'g'ri kiriting (masalan: 2020)")
            return
        await state.update_data(year=msg.text)
        contact_kb = ReplyKeyboardBuilder()
        contact_kb.button(text="🤳 Telefon raqamni yuborish", request_contact=True)
        contact_kb.adjust(1)

        await msg.answer("Mashinani band qildingiz! Endi telefon raqamingizni yuboring:",reply_markup=contact_kb.as_markup(resize_keyboard=True) )
        await state.set_state(CarState.info)
@router.message(CarState.info, F.contact)
async def car_contact(msg: types.Message, state: FSMContext):
    if msg.contact.user_id != msg.from_user.id:
        await msg.answer("Iltimos, faqat OʻZINGIZNING raqamingizni yuboring!")
        return
    data = await state.get_data()
    n = (
        f"turi: {data['type']}\n"
        f"nomi: {data['car_name']}\n"
        f"rangi: {data['color']}\n"
        f"yili: {data['year']}\n"
        f"tel: {msg.contact.phone_number}"
    )
    await msg.answer(n, reply_markup=types.ReplyKeyboardRemove())
    await msg.answer("Tanlovingiz uchun raxmat sizga o'zimiz aloqaga chiqamiz 🤗")
    await state.clear()
@router.message(CarState.info)
async def car_info_wrong(msg: types.Message, state: FSMContext):
    await msg.answer("Faqat telefon raqamingizni (contact) yuboring, boshqa hech narsa qabul qilinmaydi!")