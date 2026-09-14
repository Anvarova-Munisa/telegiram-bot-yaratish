from aiogram import Router, types
router = Router()
samaya = "AwACAgIAAxkBAAICbWqn7Qg4FM55hDgqRlfnHKYW-8YMAALbpgAC1fNBSc_t9Oj1r28nPQQ"
brak = "AwACAgIAAxkBAAICbmqn75qAY6NCFFOjQjv_Lczqq7aFAAL5pgAC1fNBSXHwyl9Ed8KmPQQ"
hayy = "AwACAgIAAxkBAAICcGqn8AiLmHT3mL0whmZ8RrYhlTMwAAIFpwAC1fNBSS-mzqZ20UTbPQQ"
aqilli_gap = "AwACAgIAAxkBAAICcWqn8EPMf811fONPVr_1XDspVtHWAAIMpwAC1fNBSSJoQj2PUL_2PQQ"
kuyov = "AwACAgIAAxkBAAICcmqn8J77YEc0CjEYrfF-SxzSywEqAAIOpwAC1fNBSS9_84Uw0Ob6PQQ"
asalim = "AwACAgIAAxkBAAICdGqn8Sh9UP1mMMf8dhVSenAki9DXAAISpwAC1fNBSe3VCe9vWMdvPQQ"
keyin = "AwACAgIAAxkBAAICdmqn8ZCITBOQWV3w-sgQLf0AAbjyWQACGacAAtXzQUkW3WrAohN_QT0E"
nomalum = "AwACAgIAAxkBAAICwGqn-JsaZkYYVR9ulLkLBLwQPdNPAAKJpwAC1fNBSaKp5JshClYuPQQ"
@router.message()
async def ovoz(msg: types.Message):
    if msg.text == "samaya":
        await msg.reply_voice(samaya)
    elif msg.text == "brak_inson":
        await msg.reply_voice(brak)
    elif msg.text == "hayy":
        await msg.reply_voice(hayy)
    elif msg.text == "aqilli_gap":
        await msg.reply_voice(aqilli_gap)
    elif msg.text == "kuyov":
        await msg.reply_voice(kuyov)
    elif msg.text == "asalim":
        await msg.reply_voice(asalim)
    elif msg.text == "keyin":
        await msg.reply_voice(keyin)
    else:
        await msg.reply_voice(nomalum)
# @router.message()
# async def test(msg: types.Message):
    # if msg.caption:
    #     await msg.answer("siz rasm va xabar yubordingiz")
    # elif msg.photo:
    #     await msg.answer("siz rasm yubordingiz")
    # elif msg.video:
    #    await msg.answer("siz yubordingiz")
    # elif msg.voice:
    #     ovoz = msg.voice.file_id
    #     await msg.answer_voice(ovoz)
    #     print(ovoz)