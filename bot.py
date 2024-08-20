import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import basic  # Импорт обработчиков

# Токен бота из окружения
TOKEN = "7202449071:AAHICPKUcBDpaeJFOLJA5ObgOaSdhiNmIpo"

# Создаем диспетчер
dp = Dispatcher()

# Логирование
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# Регистрация обработчиков из модуля basic
basic.register_handlers_basic(dp)

# Основная функция для запуска бота
async def main() -> None:
    # Инициализируем экземпляр бота с настройками
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Запускаем диспетчер событий
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем основной цикл бота
    asyncio.run(main())
