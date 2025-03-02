from aiogram import Bot, Dispatcher, types, F
from aiogram.types import CallbackQuery, BotCommand , Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from buttons import main_menu
import asyncio
import admin
import logging

TOKEN = "YOUR_TOKEN"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_router(admin.router)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Xush kelibsiz! Kerakli bo‘limni tanlang:", reply_markup=main_menu())

@dp.message(Command("id"))
async def get_id(message: types.Message):
    await message.answer(f"🆔 Sizning ID: {message.from_user.id}")

@dp.callback_query(F.data == "admin_add_product")
async def admin_add_product(callback_query: CallbackQuery, state: FSMContext):
    await admin.product_picture(callback_query.message, state)
    await callback_query.answer()

@dp.message(F.text == "📍 Bizning manzil")
async def send_location(message: Message):
    latitude, longitude = 41.340709, 69.268608
    await message.answer("📍 Bizning filial manzili:")
    await message.answer_location(latitude=latitude, longitude=longitude)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
    ]
    await bot.set_my_commands(commands)

if __name__ == "__main__":
    async def main():
        logging.basicConfig(level=logging.INFO)
        await set_commands(bot)
        await dp.start_polling(bot)

    asyncio.run(main())
