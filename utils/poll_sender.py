import random
from aiogram import Bot

async def send_quiz_poll(bot: Bot, chat_id: int, question_obj, correct_id: int):
    await bot.send_poll(
        chat_id=chat_id,
        question=question_obj["question"],
        options=question_obj["options"],
        type="quiz", #regular
        correct_option_id=correct_id,
        is_anonymous=False
    )
