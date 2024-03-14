import os

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from g4f.client import Client
import g4f

router = Router()

client = Client()





@router.message(F.text == '/start')
async def command_start(message: Message):
    await message.answer(text='hello')

@router.message()
async def all_message(message: Message):
    
    response = await g4f.ChatCompletion.create_async(
    model=g4f.models.gpt_35_turbo_16k,
    messages=[{"role": "user", "content": message.text}],
    )

    await message.answer(text= response)