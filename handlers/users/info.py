# from aiogram import Router, filters,types
# from states.InfoState import InfoState
# from aiogram.fsm.context import FSMContext
#
# from states.InfoState import InfoState
#
# router = Router()
#
# @router.message(filters.Command("info"))
# async def info(msg:types.Message,state:FSMContext):
#     await msg.answer("Ismingizni kiriting")
#     await state.set_state(InfoState.first_name)
#
# @router.message(InfoState.first_name)
# async def first_name(msg:types.Message,state:FSMContext):
#     ism = msg.text
#     if ism.isalpha():
#         await msg.answer(f"{ism} endi familyangizni kiriting")
#         await state.set_state(InfoState.last_name)
#         await state.update_data(first_name=msg.text)
#     else:
#         await msg.answer(f"ismni xato kiritingiz!")
#         await state.set_state(InfoState.last_name)
#
#
# @router.message(InfoState.last_name)
# async def last_name(msg:types.Message,state:FSMContext):
#     await msg.answer("qabul qilindi yoshingizni kiriting faqt raqamlardan iborat bolishi kerak!")
#     await state.set_state(InfoState.age)
#     await state.update_data(last_name=msg.text)
# # @router.message(InfoState.age)
# # async def age(msg:types.Message,state:FSMContext):
# #     await msg.answer(f" Barcha malumotlar qabul qilindi")
# #     await state.update_data(age=msg.text)
# @router.message(InfoState.age)
# async def age(msg: types.Message, state: FSMContext):
#     yosh2 = msg.text
#
#     if yosh2.isdigit():
#             await state.update_data(age=yosh2)
#
#             data = await state.get_data()
#             await state.clear()
#
#             ism2 = data["first_name"]
#             familya = data["last_name"]
#             yosh = int(yosh2)
#
#             oxirgi_harf = ism2.lower()[-1]
#             if oxirgi_harf in ['a', 'o', 'i', 'e']:
#                 murojaat = "singlim" if yosh < 18 else "opam"
#             else:
#                 murojaat = "ukam" if yosh < 18 else "akam"
#
#
#             n = f"{ism2} {murojaat}, ma'lumotlaringiz qabul qilindi!\n\nfamilyangiz: {familya}\nyoshingiz: {yosh}\n"
#             await msg.answer(n)
#
#         else:
#             await msg.answer("Iltimos, yoshingizni faqat raqamda kiriting!")
#             await state.set_state(InfoState.age)
#     data = await state.update_data()
#     await state.clear()
#     ism2 = data["first_name"]
#     family = data["last_name"]
#     yosh2 = data["age"]
#     n = f"ismingiz: {ism2}\n"
#     n += f"familyangiz: {family}\n"
#     n += f"yoshingiz: {yosh2}\n"
#     await msg.answer(n)


from aiogram import Router, filters, types
from states.InfoState import InfoState
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(filters.Command("info"))
async def info(msg: types.Message, state: FSMContext):
    await msg.answer("Ismingizni kiriting")
    await state.set_state(InfoState.first_name)


@router.message(InfoState.first_name)
async def first_name(msg: types.Message, state: FSMContext):
    ism = msg.text
    if ism.isalpha():
        await msg.answer(f"{ism} endi familyangizni kiriting")
        await state.set_state(InfoState.last_name)
        await state.update_data(first_name=msg.text)
    else:
        await msg.answer(f"ismni xato kiritdingiz!")
        await state.set_state(InfoState.first_name)


@router.message(InfoState.last_name)
async def last_name(msg: types.Message, state: FSMContext):
    await msg.answer("qabul qilindi yoshingizni kiriting faqat raqamlardan iborat bo'lishi kerak!")
    await state.set_state(InfoState.age)
    await state.update_data(last_name=msg.text)


@router.message(InfoState.age)
async def age(msg: types.Message, state: FSMContext):
    yosh2 = msg.text

    if yosh2.isdigit():
        await state.update_data(age=yosh2)

        data = await state.get_data()
        await state.clear()

        ism2 = data["first_name"]
        familya = data["last_name"]
        yosh = int(yosh2)

        oxirgi_harf = ism2.lower()[-1]
        if oxirgi_harf in ['a', 'o', 'i', 'e']:
            murojaat = "singlim" if yosh < 18 else "opam"
        else:
            murojaat = "ukam" if yosh < 18 else "akam"

        n = f"{ism2} {murojaat}, ma'lumotlaringiz qabul qilindi!\n\n ismingiz: {ism2} \nfamilyangiz: {familya}\nyoshingiz: {yosh}\n"
        await msg.answer(n)

    else:
        await msg.answer("Iltimos, yoshingizni faqat raqamda kiriting!")
        await state.set_state(InfoState.age)

