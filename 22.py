import telebot
from telebot import types
TOKEN = '600646028:AAFFemARUokbtOCLspFLY_7w7ETDeHivneg'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['📈Курс', 'ℹИнформация']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['🥇Bounty программа', '💬Чат']]) 
    keyboard.add(*[types.KeyboardButton(name) for name in ['✅Этапы', '🔧Техническая поддержка']])  
    bot.send_message(m.chat.id, 'Здравствуйте. Данный проект поможет вам в реализации ваших идей', 
		reply_markup=keyboard)
    bot.register_next_step_handler(m, name)
def name(m):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  keyboard.add(*[types.KeyboardButton(name) for name in ['📈Курс', 'ℹИнформация']])
  keyboard.add(*[types.KeyboardButton(name) for name in ['🥇Bounty программа', '💬Чат']]) 
  keyboard.add(*[types.KeyboardButton(name) for name in ['✅Этапы', '🔧Техническая поддержка']])  
  if m.text =='📈Курс':
    bot.send_message(m.chat.id, 'На данном этапе курс YTAcoin составляет 0,40р . Покупаю валюту на данном этапе вы получите 25% бонус в монетах проекта.\n')
  if m.text == '🥇Bounty программа':
    bot.send_message(m.chat.id, ' «Bounty» - это программа (от английского bounty), которая позволит вам получить вознаграждение за участие в нашем проекте.\n'
    	'Для этого вам нужно только лишь завести бесплатный кошелек в нашей системе (см. Раздел инструкции)\n'
    	' При успешном привлечении новых участников в проект вы будете получать 10% от их вложений, а так же 10% от их бонусов во внутренней валюте, которую вы можете продать на этапе ico или воспользоваться ей в дальнейшем в партнерских программах.\n'
    	'Выплаты вознаграждений возможны в любом удобном для вас формате.', 
		reply_markup=keyboard )	
  if m.text == '✅Этапы':
    bot.send_message(m.chat.id, ' На данный момент проект находится на этапе PRE-ICO\n' 
    	'Этот этап позволяет получить вам максимальную прибыль\n'
    	'5.06.2018 - запуск pre ICO (Производим выпуск и первоначальную продажу 1,000,000 монет)\n'
    	'16.09.2018 - запуск ICO',        
        reply_markup=keyboard)
  if m.text == '🔧Техническая поддержка':
    bot.send_message(m.chat.id, 'По всем техническим вопросам обращаться в чат тех.поддержки в телеграмме  https://t.me/joinchat/Emvc1UcgtYtOdHEUNx7H8w\n' 
        'Так же вы можете связаться через группу Вконтакте https://vk.com/ytacoin',		
		reply_markup=keyboard)
  if m.text =='ℹИнформация':
    bot.send_message(m.chat.id, ' Мы - амбициозная команда профессиональных специалистов, желающих стимулировать развитие IT технологий в России.\n' 
    	'Для реализации этих целей мы запускаем подготовительный этап программы сбора средств на долгосрочное инвестирование в иновационные проекты.\n'	
    	' Среди поставленных целей мы выделяем :\n'
    	'1) Формирование майнинг пула для добычи криптовалюты\n'
    	'2) Создание криптовалютной корзины\n'
    	'3) Выход на европейский рынок криптовалют в декабре 2018\n',
		reply_markup=keyboard)
  if m.text == '💬Чат':
    bot.send_message(m.chat.id, 'Общий чат проекта вы сможете найти по ссылке http://t-do.ru/ytacoin', 
		reply_markup=keyboard)
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  keyboard.add(*[types.KeyboardButton(name) for name in ['📈Курс', 'ℹИнформация']])
  keyboard.add(*[types.KeyboardButton(name) for name in ['🥇Bounty программа', '💬Чат']]) 
  keyboard.add(*[types.KeyboardButton(name) for name in ['✅Этапы', '🔧Техническая поддержка']])  
  bot.register_next_step_handler(m, name)

bot.polling()