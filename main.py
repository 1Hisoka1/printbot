import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = telebot.TeleBot("5525980677:AAHMUEahn0YvDHTFKgZmHSWVcq5sRRDjTbI", parse_mode=None)
delete = types.ReplyKeyboardRemove(selective=False)
#реплай клава начало заполнения
def form_mar():
    markup = types.ReplyKeyboardMarkup(True)
    btnform = types.KeyboardButton('Начать заполнение формы')
    markup.add(btnform)
#конопка загрузить
def download_but():
    markupdow = types.ReplyKeyboardMarkup(True)
    btndow = types.KeyboardButton('Загрузить')
    markupdow.add(btndow)
#иналайн выбора места
def inline_form():
    markupinlineform = InlineKeyboardMarkup()
    markupinlineform.row_width = 2
    markupinlineform.add(InlineKeyboardButton("Указать адрес", callback_data='adress'), InlineKeyboardButton("Передать местоположение", callback_data='mest'))
    return markupinlineform
#иналайн адрессов
def inline_adresa():
    markupinlineadresa = InlineKeyboardMarkup()
    markupinlineadresa.row_width = 2
    markupinlineadresa.add(InlineKeyboardButton("Товарищеская 40Б", callback_data='t40b'), InlineKeyboardButton("Карла Маркса 68", callback_data='km68'))
    return markupinlineadresa

#команды
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Список команд:\n/start Начать\n/help - Получить справку\n/start_copy_center - Начать заполнение формы', reply_markup=form_mar())
    if message.text == '/help':
        bot.send_message(message.chat.id, 'Свяжитесь с поддержкой @ggomg1228')
@bot.message_handler(content_types = ['text'])
def send_form(message):
    if message.text == 'Начать заполнение формы' or message.text=='/start_copy_center':
        bot.send_message(message.chat.id, 'Хорошо, приступим к заполнению необходимых данных\n'
                                          'Я поддерживаю следующие форматы файлов [''''PDF'''', ''''DOC'''',''''DOCX''''], будьте внимательны!'
                                          '\nДля начала укажи свой адрес'
                                          '\nИли передайте свое местоположение', reply_markup=inline_form())
#делал для адресса забыл зачем пусть булет мб вспомню
def adresa_print(message):
    if message.text == 'Выберите адрес':
        pass


#Ответы на инлайн кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    #ответ из form
    if call.data == "adress":
        bot.send_message(call.message.chat.id, "Выберите адрес", reply_markup=inline_adresa())
    #ответ из form
    if call.data == "mest":
        bot.send_message(call.message.chat.id, "Отправить местоположение")
    #ответ из адреса
    elif call.data == "t40b":
        bot.send_message(call.message.chat.id, "Вы выбрали улицу: Товарищеская 40Б", reply_markup=download_but())
    # ответ из адреса
    elif call.data == "km68":
        bot.send_message(call.message.chat.id, "Вы выбрали улицу: Карла Маркса 68", reply_markup=download_but())


bot.infinity_polling()