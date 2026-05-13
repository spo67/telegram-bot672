import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

BOT_TOKEN = ""  # токен будет на Railway

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# КНОПКА
def start_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💬 راسلنا",
                    url="https://t.me/Faditr"
                )
            ]
        ]
    )


# START
@dp.message(CommandStart())
async def start(msg: types.Message):

    text = (
        "أرسل لنا أي رسالة خاصة، وسنرد عليك بأسرع وقت ممكن "
        "ونقدّم لك عدة خيارات للربح — سواء عبر روبوت التداول، "
        "أو إشارات التداول، أو الصفقات الجاهزة.\n\n"

        "اضغط على زر «راسلنا» ولنبدأ بتحقيق الأرباح معًا!"
    )

    try:
        photo = FSInputFile("photo.jpg.jpg.jpg")

        await msg.answer_photo(
            photo=photo,
            caption=text,
            reply_markup=start_kb()
        )

    except:
        await msg.answer(
            text,
            reply_markup=start_kb()
        )


# ЗАПУСК
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())