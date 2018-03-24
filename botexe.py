#Это бот, который работает со списком учеников
import telebot
import Funksii

token = '544257192:AAG5Z42_l4QfXgfOBC-5kI4KN0Kt_xSOzG8'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def check_message(message):
    if message.text == "писок студентов":
        for student in Funksii.getListStudents():
            bot.send_message(message.chat.id, student[0])
    elif message.text == 'Сред. оценка':
        bot.send_message(message.chat.id, Funksii.getAverageMarks())
    elif message.text.isdigit():
        bot.send_message(message.chat.id,Funksii.getByIndex(int(message.text))[0])
        bot.send_message(message.chat.id,Funksii.getByIndex(int(message.text))[1])
    else:
        bot.send_message(message.chat.id, "Такой команды нет")

        
bot.polling(none_stop=True)
