from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
# from config import cnt

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет!\n\n\n Я Бот ВАЛОДКЛИКЕР.\n\n\n Жми Тап!',
                         reply_markup=kb.tapik)

cnt=0

@router.message(F.text == 'Тап!')
async def tapok(message: Message):
    cnt+=1
    await message.reply(str(cnt))
