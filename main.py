import telebot

with open("./token.txt") as file:
    token = file.readline()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Hello")


try:
    bot.infinity_polling()
except BaseException:
    with open("./error.txt") as file:
        file.write(BaseException)
