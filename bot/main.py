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
    chat_id = call.message.chat.id
    user = BotUsers.objects.filter(user_id = chat_id)[0]
    if call.data == "uz":
        user.lang = 'Uz'
        user.save()
        return menu_bot(call)
    elif call.data == "ru":
        user.lang = "Ru"
        user.save()
        return menu_bot(call)
    else:
        return create_user(call)

        

@bot.message_handler(commands=["start"])
def start_bot(message:types.Message):
    chat_id = message.chat.id
    #BotUsers.objects.create(user_id = chat_id)   ##for creating admins it for this time after I will create command for admin for creating admins
    
    try:
        user = BotUsers.objects.filter(user_id = chat_id)[0]
        user.username = message.from_user.username
        user.situation = start_bot.__name__
        user.save()
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
    

def menu_bot(call:types.CallbackQuery):
    chat_id = call.message.chat.id
    user = BotUsers.objects.filter(user_id = chat_id)[0]
    user.situation = menu_bot.__name__
    lang = user.lang
    dct = tools.parse_data(location = menu_bot.__name__, lang = lang)
    text = dct["text"]
    mark = types.InlineKeyboardMarkup(row_width = int(dct["row_num"]))
    buttons = []
    for i in dct["buttons"]:
        if lang == "Uz":
            text1 = i.text_uz
        else:
            text1 = i.text_ru
        buttons.append(types.InlineKeyboardButton(text = text1, callback_data = i.call_back_data))
    mark.add(*buttons)
    bot.delete_message(chat_id=chat_id,
                    message_id=call.message.id)
    bot.send_message(chat_id = chat_id,
                    text = text,
                    reply_markup=mark)

def create_user(call):
    chat_id = call.message.chat.id
    user = BotUsers.objects.filter(user_id = chat_id)[0]
    usr = Users.objects.create(situation = 1)
    user.situation = create_user.__name__
    lang = user.lang
    dct = tools.parse_data(location = create_user.__name__, lang = lang)
    text = dct["text"]
    bot.delete_message(chat_id = chat_id,
                    message_id = call.message.id)
    bot.send_message(chat_id = chat_id,
                    text = text,)

@bot.message_handler()
def message_handler_func(message):
    situate = 0
    chat_id = message.chat.id
    user = Users.objects.filter(situation = 1)
    BotUser = BotUsers.objects.filter()
    if user.situation == create_user.__name__:
        situate = 1
    else:
        situate += 1
    return universal(message, situate)


def universal(message:types.Message, situation):
    chat_id = message.chat.id
    BotUser = BotUsers.objects.filter(user_id = chat_id)[0]
    BotUser.situation = universal.__name__
    user = Users.objects.filter(situation = situation)[0]
    text = tools.parse_find(location = user.situation)
    bot.send_message(chat_id=chat_id,
                    text = text)






if __name__ == "__main__":
    bot.polling(non_stop=True)
    bot.infinity_polling()    



