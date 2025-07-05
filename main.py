from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN, ADMIN_ID

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Salom! Bu Free Fire, PUBG, ML va FIFA uchun donation bot.")

@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.answer("/start - Botni boshlash\n/help - Yordam")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
