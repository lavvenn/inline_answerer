import hashlib

from aiogram import Router, F 
from aiogram.types import InlineQuery, InlineQueryResultArticle,InputTextMessageContent


from g4f.client import Client
import g4f

client = Client()

irouter = Router()

@irouter.inline_query()
async def inline_answer(query: InlineQuery):

    if str(query.query).endswith("*"):

        text = await g4f.ChatCompletion.create_async(
        model=g4f.models.gpt_35_turbo_16k,
        messages=[{"role": "user", "content": query.query + "постарайся ответить на мой вопрос используя максимум 1 предложения"}],
        )
        print('ANSWER IS READY')


        inputcontent = InputTextMessageContent(message_text=text)
        result_id = hashlib.md5(text.encode()).hexdigest()

        item = InlineQueryResultArticle(
            input_message_content=inputcontent,
            id=result_id,
            title='GPT3.5'
        )

        await query.answer([item])
    else:
        print('neee')