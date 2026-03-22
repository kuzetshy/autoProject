import telebot
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
import os

# 🔑 НОВЫЙ ТОКЕН (сбрось старый в @BotFather, раз он попал в чат!)
TOKEN = '8799469888:AAGMHHivLLysIVXGbMTLMNlYBy7Xmn5PXzc'
bot = telebot.TeleBot(TOKEN)

# 📂 ПУТИ К ФАЙЛАМ
# Находит путь к папке autoProject
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Склеивает путь: autoProject -> models -> car_price_model_FINAL.cbm
MODEL_PATH = os.path.join(BASE_DIR, "models", "car_price_model_FINAL.cbm")

# 🧠 ЗАГРУЗКА МОДЕЛИ
model = CatBoostRegressor()

print(f"🔍 Ищу модель по пути: {MODEL_PATH}")

if os.path.exists(MODEL_PATH):
    model.load_model(MODEL_PATH)
    print(f"✅ УРА! Модель успешно загружена.")
else:
    print(f"❌ ОШИБКА: Файл не найден!")
    print(f"Я искал тут: {MODEL_PATH}")
    print(f"Содержимое папки autoProject: {os.listdir(BASE_DIR)}")
    # Если папка models существует, покажем что в ней
    models_dir = os.path.join(BASE_DIR, "models")
    if os.path.exists(models_dir):
        print(f"Содержимое папки models: {os.listdir(models_dir)}")

# --- ОСТАЛЬНОЙ КОД БОТА ---
user_data = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Приветик! 🚗 Я помогу тебе оценить авто.\n"
                          "Напиши марку машины (например: skoda, bmw):")
    bot.register_next_step_handler(message, get_brand)

def get_brand(message):
    user_data[message.chat.id] = {'brand': message.text.lower()}
    bot.send_message(message.chat.id, "Год выпуска? (например: 2018):")
    bot.register_next_step_handler(message, get_year)

def get_year(message):
    try:
        user_data[message.chat.id]['year'] = int(message.text)
        bot.send_message(message.chat.id, "Пробег в км?:")
        bot.register_next_step_handler(message, get_mileage)
    except:
        bot.send_message(message.chat.id, "Введи год цифрами!")
        bot.register_next_step_handler(message, get_year)

def get_mileage(message):
    user_data[message.chat.id]['mileage'] = int(message.text)
    bot.send_message(message.chat.id, "Мощность в kW?:")
    bot.register_next_step_handler(message, get_power)

def get_power(message):
    user_data[message.chat.id]['power'] = int(message.text)
    bot.send_message(message.chat.id, "Тип топлива? (petrol, diesel, electric):")
    bot.register_next_step_handler(message, get_fuel)

def get_fuel(message):
    user_data[message.chat.id]['fuel'] = message.text.lower()
    bot.send_message(message.chat.id, "Коробка? (manual, automatic):")
    bot.register_next_step_handler(message, get_gearbox)

def get_gearbox(message):
    user_data[message.chat.id]['gearbox'] = message.text.lower()
    data = user_data[message.chat.id]
    
    df_input = pd.DataFrame([{
        'brand': data['brand'],
        'year': data['year'],
        'mileage': data['mileage'],
        'fuel': data['fuel'],
        'gearbox': data['gearbox'],
        'power': data['power'],
        'car_age': 2026 - data['year'],
        'segment': "2",
        'is_4x4': 0,
        'is_automatic': 1 if 'auto' in data['gearbox'] else 0,
        'is_sport': 0,
        'has_led': 1
    }])

    prediction_log = model.predict(df_input)
    prediction_real = np.expm1(prediction_log)[0]

    bot.send_message(message.chat.id, f"🎯 Оценка для {data['brand'].upper()}:\n"
                                      f"💰 Рекомендуемая цена: *{prediction_real:,.0f} CZK*", 
                     parse_mode="Markdown")

if __name__ == '__main__':
    bot.infinity_polling()