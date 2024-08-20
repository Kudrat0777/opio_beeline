from aiogram import Dispatcher, types
from aiogram.filters import CommandStart

# Обработчик команды /start
async def start_command_handler(message: types.Message) -> None:
    """
    Обработчик команды /start
    """
    await message.answer(f"Привет, {message.from_user.full_name}!")

# Обработчик echo
async def echo_handler(message: types.Message) -> None:
    """
    Эхо-бот. Обрабатывает любые типы сообщений и отправляет копию назад пользователю.
    """
    try:
        # Отправляем копию полученного сообщения
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # Обрабатываем типы сообщений, которые не могут быть скопированы
        await message.answer("Неподдерживаемый тип сообщения!")

# Функция для регистрации обработчиков
def register_handlers_basic(dp: Dispatcher):
    dp.message.register(start_command_handler, CommandStart())
    dp.message.register(echo_handler)
