from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


tapik= ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Тап!')]
],
input_field_placeholder='PLAY!')

