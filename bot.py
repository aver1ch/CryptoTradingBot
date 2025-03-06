import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telebot import types  # для указание типов
import time
import io_json
bot = telebot.TeleBot() # добавь свой api-ключ


def convert_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return days, hours, minutes, seconds


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.from_user.id not in []: # сюда можно записать свой peerID из телеграма, чтобы доступ к боту был только у тебя)
        bot.send_message(message.chat.id, text="Тебя здесь не ждут :)")
        print(message.chat.id)
        return 0

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Я умею торговать :3")
        bot.send_message(message.from_user.id, "Для получения списка команд отправте команду /help")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Меню"))
        bot.send_message(message.chat.id, text="Меню", reply_markup=markup)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Доступные команды")
        bot.send_message(message.from_user.id, "(некоторые команды доступны только определённым пользователям)")
        command_list = open("command_list.txt", encoding='utf-8', mode='r')
        bot.send_message(message.from_user.id, str(command_list.read()))
        command_list.close()

    elif message.text == "сука":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Меню"))
        bot.send_message(message.chat.id,
                         text="Меня", reply_markup=markup)

    elif message.text == "Меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Информация")
        btn2 = types.KeyboardButton("PANIC!!!!")
        btn3 = types.KeyboardButton("Связь с поддержкой")
        btn4 = types.KeyboardButton("Транзакции")
        btn5 = types.KeyboardButton("Курс")
        markup.add(btn1, btn2)
        markup.add(btn5)
        markup.add(btn4)
        markup.add(btn3)

        bot.send_message(message.chat.id,
                         text="Перехожу в меню, {0.first_name}".format(message.from_user), reply_markup=markup)

    elif message.text == "Курс":
        dict_of_params = io_json.read_parameters_from_json("params.json")
        string = ""
        string += "Курс: " + str(round(dict_of_params.get('price'), 2)) + "\n"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Курс"))
        markup.add(types.KeyboardButton("Меню"))
        bot.send_message(message.chat.id, text=string, reply_markup=markup)

    elif message.text == "Информация":
        dict_of_params = io_json.read_parameters_from_json("params.json")
        dict_sys = io_json.read_parameters_from_json("system.json")
        start_t = dict_sys.get('start_time')
        curr_t = dict_sys.get('current_time')
        time_to_print = curr_t-start_t
        days, hours, minutes, seconds = convert_seconds(time_to_print)
        string = "Работает " + str(int(days)) + " день и " + str(int(hours)) + ":" + str(int(minutes)) + ":" + str(int(seconds)) + "\n"
        string += "Курс: " + str(round(dict_of_params.get('price'), 2)) + "\n"
        string += "Баланс: " + str(round(dict_of_params.get('balance'), 2)) + "\n"
        string += "Результат последней сделки: " + str(round(dict_of_params.get('income'), 9)) + "\n"

        if dict_of_params.get('is_order_open') == True:
            string += "Открыта ли сделка: Да " + "\n"
            string += "Цена покупки: " + str(dict_of_params.get('buy_price')) + "\n"
        else:
            string += "Открыта ли сделка: Нет " + "\n"
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Информация")
        markup.add(btn1)
        markup.add(types.KeyboardButton("Меню"))
        bot.send_message(message.chat.id, text=string, reply_markup=markup)

    # доделать транзакции, чтобы логи выкидывало
    elif message.text == "Транзакции":
        file1 = "transactions.txt"
        f = open(file1, 'r')
        Lines = f.readlines()

        string = "Транзакции: " + "\n\n"
        string += str(Lines[-1]) + "\n" + "\n"
        string += str(Lines[-2]) + "\n" + "\n"
        string += str(Lines[-3]) + "\n" + "\n"
        string += str(Lines[-4]) + "\n" + "\n"
        string += str(Lines[-5]) + "\n" + "\n"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Меню"))
        bot.send_message(message.chat.id, text=string, reply_markup=markup)

    elif message.text == "PANIC!!!!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Меню"))
        bot.send_message(message.chat.id, text="А ты не реализовал эту кнопку, отсыхай дружелёчек))", reply_markup=markup)

    elif message.text == "Связь с поддержкой":
        bot.send_message(message.from_user.id, "Для связи с разработчиками напишите")
        bot.send_message(message.from_user.id,"или https://t.me/averichie\n")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Меню"))
        bot.send_message(message.chat.id, text="Меню", reply_markup=markup)


    else:
        bot.send_message(message.from_user.id, "Команда не распознана. Воспользуйтесь /help")


while True:
    try:
        # bot.polling(none_stop=True)
        bot.infinity_polling(timeout=2)

    except Exception as e:
        bot.stop_polling()
        print("Бот умер")
        print(e)
        bot = telebot.TeleBot('7134311077:AAGYLkDXgmQDOyXnXT8VM-YHmNsOhRyNfdY')
