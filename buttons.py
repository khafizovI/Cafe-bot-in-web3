from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton , KeyboardButton , ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

WEB3_SHOP_URL = url="https://67c4369db81cfb03654969c7--glittering-flan-0773cf.netlify.app/"
WEB3_CART_URL = url= "https://67c40fc6068a060112ffac1a--magnificent-crepe-ff3ca2.netlify.app/"

def get_admin_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ Mahsulot qo‘shish"),KeyboardButton(text="🗑 Mahsulotlarni ochirish")],
            [KeyboardButton(text="🔙 Orqaga")]
        ],
        resize_keyboard=True
    )

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛍 Menu", web_app=WebAppInfo(url=WEB3_SHOP_URL))],
            [KeyboardButton(text="✍️ Taklif va shikoyatlar"),KeyboardButton(text="🛒 Savatcha",web_app=WebAppInfo(url=WEB3_CART_URL))],
            [KeyboardButton(text="📍 Bizning manzil")]
        ],
        resize_keyboard=True
    )

def back_menu():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🔙 Orqaga")]],
        resize_keyboard=True
    )