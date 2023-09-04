import telebot
import webbrowser
from telebot import types
from telebot.types import InputMediaPhoto
import sqlite3

bot = telebot.TeleBot("6550927915:AAEHknV7FAkDty1jN4Dd1jztzI-cjwMUA9M")
name = None

#Ненужный контент
@bot.message_handler(content_types=['video, photo, audio'])
def othermaterial(message):
    bot.reply_to(message, '''Хотите сделать заказ по типу отправленного файла?)
Вперед! Пропишите команду /makeorder для оформления заказа💫''')


# #Начальные кнопки
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton("Просмотр работ")
#     btn2 = types.KeyboardButton("Просмотр отзывов")
#     markup.row(btn1,btn2)

#Функция для кнопок
@bot.message_handler(content_types=['text'])
def on_click(message):
    if message.text == "Просмотр работ" or message.text == "/checkworks":
        checkworks(message)
    elif message.text == "Просмотр отзывов" or message.text == "/checkfeedback":
        checkfeedback(message)
    elif message.text == "Сделать заказ" or message.text == "/makeorder":
        makeorder(message)
    elif message.text == "Просмотр работ" or message.text == "/checkbonus":
        checkbonus(message)

#Команды
#Начало
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Просмотр работ")
    btn2 = types.KeyboardButton("Просмотр отзывов")
    markup.row(btn1,btn2)
    btn3 = types.KeyboardButton("Сделать заказ")
    btn4 = types.KeyboardButton("Посмотреть бонусные баллы")
    markup.row(btn3,btn4)
    bot.send_message(message.from_user.id, 
    f'''Приветствую, {message.from_user.first_name} {message.from_user.last_name} ! Меня зовут Алина, я графический дизайнер. Больше года профильно создаю дизайн карточек товаров для Wildberries 🔥

Открыли магазин на Wildberries, но продаж мало? Не беда! Повысить продажи и обогнать конкурентов поможет продающий дизайн для карточек товаров 🚀

⭐ За моими плечами большое количество довольных клиентов и 970+ оформленных карточек за 2022 год

⭐ Провожу качественный анализ и разрабатываю лучший дизайн для выделения Вашей карточки среди конкурентов

⭐ Максимально раскрываю все преимущества товара и доношу ценность до покупателей

⭐ Выполняю работу быстро и сдаю проекты в срок

⭐ Вы получите гарантированно крутой результат

В этом боте Вы можете посмотреть мои работы, а также узнать много полезной информации о дизайне🧡

💭Пропишите команду /help чтобы узнать о возможностях бота''', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


#ГруппаВК
@bot.message_handler(commands=['openvk'])
def main(message):
    link = types.InlineKeyboardMarkup()
    link.add(types.InlineKeyboardButton("Перейти на группу ВК", url ="https://vk.com/lina_pro_design"))
    text = "Здесь вы можете посмотреть на нашу группу ВК🔥"
    bot.send_message(message.from_user.id, text, reply_markup= link)
    
#Работы
@bot.message_handler(commands=['checkworks'])
def checkworks(message):
    link = types.InlineKeyboardMarkup()
    link.add(types.InlineKeyboardButton("Посмотреть мои остальные работы", url ="https://vk.com/lina_pro_design?z=album-195896248_272596449"))
    text = "Здесь вы можете ознакомиться с моими работами💜"
    with open("works/1.jpg","rb") as photo1, open("works/2.jpg","rb") as photo2,open("works/3.jpg","rb") as photo3, open("works/4.jpg","rb") as photo4, open("works/5.jpg","rb") as photo5:
        bot.send_media_group(message.from_user.id, [InputMediaPhoto(photo1), InputMediaPhoto(photo2), InputMediaPhoto(photo3),  InputMediaPhoto(photo4), InputMediaPhoto(photo5)])
    bot.send_message(message.from_user.id, text, reply_markup= link)

#Отзывы
@bot.message_handler(commands=['checkfeedback'])
def checkfeedback(message):
    link = types.InlineKeyboardMarkup()
    link.add(types.InlineKeyboardButton("Посмотреть остальные отзывы", url ="https://vk.com/topic-195896248_48849283"))
    text = "Здесь вы можете ознакомиться с отзывами о моей работе💜"
#    with open("feedbacks/2.jpg","rb") as photo1:
#        bot.send_media_group(message.from_user.id, photo1, caption = text, reply_markup= link)
    with open("feedbacks/1.jpg","rb") as photo1, open("feedbacks/2.jpg","rb") as photo2,open("feedbacks/3.jpg","rb") as photo3, open("feedbacks/4.jpg","rb") as photo4, open("feedbacks/5.jpg","rb") as photo5:
        bot.send_media_group(message.from_user.id, [InputMediaPhoto(photo1), InputMediaPhoto(photo2), InputMediaPhoto(photo3),  InputMediaPhoto(photo4), InputMediaPhoto(photo5)])
    bot.send_message(message.from_user.id, text, reply_markup= link)

#Создание заказа
#@bot.message_handler(commands=['makeorder'])
@bot.callback_query_handler(func=lambda call: True)
def makeorder(call):
    conn = sqlite3.connect("alinawb.sql")
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info+= f'Имя: {el[1]}, Пароль {el[2]}\n'


    cur.close()
    conn.close()

    bot.send_message(call.chat.id, info)

#Просмотр бонусов
@bot.message_handler(commands=['checkbonus'])
def checkbonus(message):
    conn = sqlite3.connect("alinawb.sql")
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(60), pass varchar(60))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,'''Хотите открыть бонусную систему?
Напишите ваше имя💫''')
    bot.register_next_step_handler(message,user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id,'''Осталось только ваш пароль записать! Введите ваш пароль💫''')
    bot.register_next_step_handler(message,user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect("alinawb.sql")
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name,pass) VALUES ('%s','%s')" % (name,password))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,'''Отлично! Вы успешно зарегистрировались! Сделайте первый заказ и вам начислются бонусы💫''')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.from_user.id, 
        f'''Желаете посмотреть мои работы или может хотите узнать количество бонусных баллов?
Или может собираетесь сделать заказ? То для этого помогут следующие команды, просто наберите их и узнайте поподробнее о нужном вопросе!🤩
    
🔸/start - Кто я? Информация про меня, как графического дизайнера
🔸/checkbonus - Есть накопленные баллы? Просмотр бонусных баллов
🔸/checkfeedback - Желаете посмотреть отзывы наших клиентов? Тут найдете их
🔸/checkworks - Не можете определиться с дизайном? Посмотрите мои работы
🔸/makeorder - Определились с заказом? Здесь можете сделать заказ
🔸/openvk - Где нас можно еще найти? Открыть группу ВК''')

@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id,"Hii, how are you?")
    elif message.text == "Bye":
        bot.send_message(message.chat.id,"Oh, okay. Goodbye, my friend!")
    elif message.text == "meow":
        bot.send_message(message.chat.id,"Cat! You are alive!???")
    elif message.text == "nose":
        bot.send_message(message.chat.id,"Oh, it's a human organ")
bot.polling(none_stop=True, interval=0)
