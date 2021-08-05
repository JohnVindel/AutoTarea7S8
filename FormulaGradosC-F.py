#Tarea 8 - Formula de Grados Cº y Fº
import telebot 

bot = telebot.TeleBot('1883937208:AAEcgBcQnAmqmw0Pd8Ezfex0NXO8RuaoJIs')
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['celcius-fahrenheit', 'c-f', 'fahrenheit'])
def info(mensaje):
    bot.reply_to(mensaje, "ºF= (ºC * 1.8) + 32")
    print("Celcius a Fahrenheit")

@bot.message_handler(commands=['fahrenheit-celcius', 'f-c', 'celcius'])
def info(mensaje):
    bot.reply_to(mensaje, "ºC= (ºF - 32) / 1.8")
    print("Fahrenheit a Celcius")

bot.polling()