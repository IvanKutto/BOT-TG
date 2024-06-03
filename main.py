# Импортируем необходимые библиотеки
import telebot
import random


# Получаем токен Телеграм и инициализируем бота
token = "XXXxxxXXX"
bot = telebot.TeleBot(token=token)


# Создаем хендлер команды старт: Приветствие с указанием имени отправителя
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Здравствуйте, {name}! Приветствую Вас в чате Ивана Кутто! \n Напишите: "Привет" или "Как дела". \n Я обязательно отвечу👋'.format(name=message.from_user.full_name)) 


# Создаем хендлер для сообщений "Привет" и "Как дела"
@bot.message_handler(content_types=['text']) 
# При получении ботом текстового сообщения, отрабатывает 
# функция ответа, в зависимости от текста входящего сообщения
def get_hello(message):


    # Список рандомных ответов
    list_of_answer = ['Отлично!🔥', 'Превосходно!😎', 'Замечательно!👍', 'Всё ОК!👌']
    # Список возможных входящих приветов
    list_of_hello = ['Привет!', 'привет!', 'привет', 'Привет']
    # Список возможных входящих "как дела"
    list_of_how_are_you = ['Как дела?', 'Как дела', 'как дела?', 'как дела']
    

    # Если входящий "привет" - отвечаем приветом с указанием имени отправителя
    if message.text in list_of_hello:
        bot.reply_to(message, 'Привет, {name}!🖐'.format(name=message.from_user.full_name))


    # Если входящий "как дела" отвечаем рандомно из списка
    elif message.text in list_of_how_are_you:
        bot.reply_to(message, random.choice(list_of_answer))


# Запускаем непрерывный поллинг
if __name__ == '__main__':
    bot.polling(none_stop=True)