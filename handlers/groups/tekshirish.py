from aiogram import Router,types

rt = Router()

@rt.message()
async def start(msg: types.Message):
    user = msg.from_user.first_name
    if msg.group_chat_created:

        await msg.answer(f" {user}yangi guruh yaratildi")
        # print(msg.group_chat_created)
    elif msg.new_chat_members:
        new_user = msg.new_chat_members[0].first_name
        await msg.answer(f"{new_user} ni qoshdi")
        # print(msg.new_chat_members)
    elif msg.left_chat_member:
        left_user = msg.left_chat_member.first_name
        await msg.answer(f"{left_user}ni chiqarb yubordi")
        # print(msg.left_chat_member)
    elif msg.caption:
        caption = msg.caption
        n = f"{user} bu caption"
        await msg.answer(caption)
        await msg.answer(n)
    elif msg.new_chat_title:
        title = msg.new_chat_title
        n = f"{user} guruh nomini {title} ga ozgartirdi"
        await msg.answer(n)
        # print(user)
    elif msg.new_chat_photo:
        photo = msg.new_chat_photo[-1].file_id
        n = f"{user} guruh rasmini ozgartirdi"
        await msg.answer(photo)
        await msg.answer(n)
        # rasm = msg.new_chat_photo
        # print(rasm)
        # await msg.answer_photo(rasm)
    elif msg.delete_chat_photo:
        n = f"{user} guruh rasmini ochirdi"
        await msg.answer(n)
        # print(msg.delete_chat_photo)