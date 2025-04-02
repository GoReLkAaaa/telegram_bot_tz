from aiogram import Bot, Dispatcher
import os
import asyncio
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.fsm.storage.memory import MemoryStorage
import re
from text.keyboard_text_func import (
                                        main_menu__,
                                        program_school__,
                                        subscription_by_education_menu__,
                                     )
from sympy.abc import lamda

load_dotenv()


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(storage=MemoryStorage())


EMAIL_CHECK = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PHONE_NUMBER_CHEK = re.compile(r"^\+?\d{1,3}[-.\s]?\(?\d{2,3}\)?[-.\s]?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}$")


class UserData(StatesGroup):
    full_name = State()
    email = State()
    phone_number = State()


class MenuState(StatesGroup):
    MAIN_MENU = State()
    PROGRAM_SCHOOL_MENU = State()
    MY_SUBSCRIPTIONS_MENU = State()
    SUBSCRIPTION_BY_EDUCATION_MENU = State()
    MY_SUBSCRIPTIONS_ALL_CHANNELS = State()
    NOT_ACTIVE_SUBSCRIPTIONS_MENU = State()


@dp.message(Command('start'))
async def start_command(message: Message, state: FSMContext):
    text = ('Привет! 👋 Для начала работы'
            ' нам нужно собрать некоторые ваши данные.'
            'Пожалуйста, введите ваше полное имя (Ф.И.О.):'
            )
    await message.answer(text)
    await state.set_state(UserData.full_name)


@dp.message(UserData.full_name)
async def full_name(message: Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer('Спасибо!Теперь пожалуйста, укажите ваш Email-адрес для связи:')
    await state.set_state(UserData.email)


@dp.message(UserData.email)
async def mail(message: Message, state: FSMContext):
    mail = message.text
    if EMAIL_CHECK.match(mail):
        await state.update_data(email=mail)
        await message.answer('Отлично! Наконец, укажите ваш номер телефона')
        await state.set_state(UserData.phone_number)
    else:
        await message.answer('Пожалуйста введите свою почту!')


@dp.message(UserData.phone_number)
async def phone(message: Message, state: FSMContext):
    phone = message.text
    if PHONE_NUMBER_CHEK.match(phone):
        await state.update_data(phone_number=phone)
        await menu(message, state)
        await state.clear()
    else:
        await message.answer('Пожалуйста введите свой номер телефона')


@dp.message(lambda message: message.text == '⭐Программы школы')
async def program_school(message: Message, state: FSMContext):
    await state.set_state(MenuState.PROGRAM_SCHOOL_MENU)
    text, keyboard_program_school_menu = program_school__()
    await message.answer(
        text,
        reply_markup=keyboard_program_school_menu,
    )


@dp.message(lambda message: message.text == '📚Подписка на обучение')
async def subscription_by_education(message: Message, state: FSMContext):
    await state.set_state(MenuState.SUBSCRIPTION_BY_EDUCATION_MENU)
    text, keyboard_subscription_by_education_menu = subscription_by_education_menu__()
    await message.answer(
        text,
        reply_markup=keyboard_subscription_by_education_menu,
    )


@dp.message(lambda message: message.text == "🔙Назад")
async def back_handler(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == MenuState.PROGRAM_SCHOOL_MENU:
        await state.set_state(MenuState.MAIN_MENU)
        text, keyboard_menu = main_menu__()
        await message.answer(text, reply_markup=keyboard_menu)
    elif current_state == MenuState.SUBSCRIPTION_BY_EDUCATION_MENU:
        await state.set_state(MenuState.PROGRAM_SCHOOL_MENU)
        text, keyboard_program_school_menu = program_school__()
        await message.answer(text, reply_markup=keyboard_program_school_menu)
    elif current_state == MenuState.MY_SUBSCRIPTIONS_MENU:
        pass


@dp.message()
async def menu(message: Message, state: FSMContext):
    await state.set_state(MenuState.MAIN_MENU)
    text, keyboard_menu = main_menu__()
    await message.answer(
        text,
        reply_markup=keyboard_menu,
    )


async def main():
    await dp.start_polling(bot)


asyncio.run(main())

if __name__ == '__main__':
    asyncio.run(main())