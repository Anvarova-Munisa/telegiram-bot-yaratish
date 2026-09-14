from aiogram import Router, filters, types
from states.InfoState import InfoState
from aiogram.fsm.context import FSMContext
router = Router()
@router.message(filters.Command("info"))
async def info(msg: types.Message, state: FSMContext):
    await msg.answer("Ismingizni kiriting")
    await state.set_state(InfoState.first_name)
@router.message(InfoState.first_name)  # & Munisa
async def first_name(msg: types.Message, state: FSMContext):
    ism = msg.text.strip()
    if not ism.replace(" ", "").isalpha():
        await msg.answer("Ismni xato kiritdingiz! Qaytadan kiriting:")
        return
    await state.update_data(first_name=msg.text)
    await msg.answer(f"{ism} endi familiyangizni kiriting")
    await state.set_state(InfoState.last_name)
@router.message(InfoState.last_name)
async def last_name(msg: types.Message, state: FSMContext):
    matn = msg.text.strip()
    if not matn.replace("v", "a").isalpha():
        await msg.answer("Familiya faqat harflardan iborat bo'lishi kerak! Qaytadan kiriting:")
        return
    if not matn.lower().endswith(('v', 'a')):
        await msg.answer(
            "Familiya xato  Qaytadan kiriting:")
        return
    await state.update_data(last_name=msg.text)
    await msg.answer("Yoshingizni kiriting:")
    await state.set_state(InfoState.age)
@router.message(InfoState.age)
async def age(msg: types.Message, state: FSMContext):
    yosh2 = msg.text
    if not yosh2.isdigit():
        await msg.answer("Iltimos, yoshingizni faqat raqamlarda kiriting!")
        return
    if len(yosh2) != 2:
        await msg.answer("Iltimos, faqat 2 xonali son kiriting!")
        return
    await state.update_data(age=yosh2)
    data = await state.get_data()
    await state.clear()
    ism2 = data["first_name"]
    familya = data["last_name"]
    yosh = int(yosh2)
    oxirgi_harf = familya.lower()[-1]
    if oxirgi_harf == "a":
        murojaat = "singlim" if yosh < 18 else "opa"
    elif oxirgi_harf == "v":
        murojaat = "ukam" if yosh < 18 else "aka"
    else:
        murojaat = "jigarim"
    m = f"{ism2} {murojaat}, ma'lumotlaringiz qabul qilindi.\n\nIsmingiz: {ism2}\nFamiliyangiz: {familya}\nYoshingiz: {yosh}"
    await msg.answer(m)


