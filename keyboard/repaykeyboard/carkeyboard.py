from aiogram.utils.keyboard import ReplyKeyboardBuilder
b_type = ReplyKeyboardBuilder()
types = ["oddiy", "elektro", "inamarka"]
for t in types:
    b_type.button(text=t)
b_type.adjust(3)
b_oddiy = ReplyKeyboardBuilder()
cars = ["tiko", "matiz", "jiguli", "nexia", "cobalt", "jentra", "damas"]
for car in cars:
    b_oddiy.button(text=car)
b_oddiy.adjust(3)
b_inamarka = ReplyKeyboardBuilder()
cars = ["malibu", "tracker", "onix", "bmw", "bugatti"]
for car in cars:
    b_inamarka.button(text=car)
b_inamarka.adjust(3)
b_elektro = ReplyKeyboardBuilder()
cars = ["byd", "tesla", "kia", "tesla2", "tesla3"]
for car in cars:
    b_elektro.button(text=car)
b_elektro.adjust(3)