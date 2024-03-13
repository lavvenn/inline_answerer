from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(F.text == '/start')
async def command_start(message: Message):
    await message.answer(text='hello')

@router.message()
async def all_message(message: Message):
    answer = 'wow'
    await message.answer(text=answer)