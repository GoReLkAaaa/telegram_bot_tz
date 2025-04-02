from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



def main_menu__():
    text = ('👋 Добро пожаловать!'
            ' Здесь вы можете узнать'
            ' о подписках на наши программы'
            ' и связаться с техподдержкой для их приобретения.'
            ' Выберите нужное действие: '
            )
    keyboard_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='⭐Программы школы')],
            [KeyboardButton(text='✨Мои подписки')],
            [KeyboardButton(text='💭Связаться с тех.поддержкой')],
        ],
        resize_keyboard=True,
    )
    return text, keyboard_menu


def program_school__():
    text = ('Вот доступнык подписки:\n'
            '1.📚Подписка на обучение\n'
            '2.🚀Подписка для маштабирования\n'
            'Выберите интересующую вас подписку,чтобы узнать подробности'
            )
    keyboard_program_school_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='📚Подписка на обучение')],
            [KeyboardButton(text='🚀Подписка на масштабирования')],
            [KeyboardButton(text='🔙Назад')],
        ],
        resize_keyboard=True,
    )
    return text, keyboard_program_school_menu


def subscription_by_education_menu__():
    text = ('📚Подписка на обучение\n\n'
            'Описание:Данная подписка включает'
            'доступ к лучшим учебным материалам,'
            'курсам и вебинарам по теме.\n\n'
            'Включенные калалы и группы:\n'
            '-Канал 1: Обучение основам\n'
            '-Канал 2: Вебинары для продвинутых\n'
            'Для оформления подписки свяжитесь с техподдержкой')
    keyboard_subscription_by_education_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='💭Связаться с тех.поддержкой')],
            [KeyboardButton(text='🔙Назад')],
        ],
        resize_keyboard=True,
    )
    return text, keyboard_subscription_by_education_menu


keyboard_my_subscription_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📚Подписка на обучение')],
        [KeyboardButton(text='🚀Подписка на масштабирования')],
        [KeyboardButton(text='➕Продлить подписку')],
        [KeyboardButton(text='🔙Назад')],
    ],
    resize_keyboard=True,
)


keyboard_my_subscription_all_channels = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Канал 1')],
        [KeyboardButton(text='Группа 1')],
        [KeyboardButton(text='Канал 2')],
        [KeyboardButton(text='🔙Назад')],
    ],
    resize_keyboard=True,
)


keyboard_not_active_subscription_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='⭐Программы школы')],
        [KeyboardButton(text='💭Связаться с тех.поддержкой')],
        [KeyboardButton(text='🔙Назад')],
    ],
    resize_keyboard=True,
)


