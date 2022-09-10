import telebot
import config
from telebot import types
import tools
from backend.models import Users, BotUsers


bot = telebot.TeleBot(token = config.TOKEN,
                    parse_mode="HTML",
                    threaded=2)


@bot.callback_query_handler(func= lambda call: True)
def inli(call):
    pass
        

@bot.message_handler(commands=["start"])
def start_bot(message):
    chat_id = message.chat.id
    #BotUsers.objects.create(user_id = chat_id)   ##for creating admins it for this time after I will create command for admin for creating admins
    try:
        user = BotUsers.objects.filter(user_id = chat_id)[0]
        lang = user.lang
        text = tools.parse_find(location=start_bot.__name__, lang=lang)
        mark = types.InlineKeyboardMarkup()
        mark1 = types.InlineKeyboardButton(text = "🇺🇿 O'zbek", callback_data="uz")
        mark2 = types.InlineKeyboardButton(text = "🇷🇺 Rus tili", callback_data="ru")
        mark.add(mark1, mark2)
        bot.send_message(chat_id = chat_id,
                    text = text,
                    reply_markup=mark
                    )
    except:
        text = "Assalomu alaykum, Afsus siz bizning botimizdan foydalana olmaysiz!!"
        bot.send_message(chat_id = chat_id,
                    text = text,
                    )    
    
if __name__ == "__main__":
    bot.polling(non_stop=True)
    bot.infinity_polling()    
