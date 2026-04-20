import requests
import telebot
import psycopg2
from sqlalchemy import create_engine, text, insert, MetaData,Table

bot = telebot.TeleBot('7354516664:AAFc7H5o7GIlUkSxffkbwAXxCMmqPvs79HE')

city = 'Ulyanovsk'
weather_api_key = 'c86d292f9a1eb3e7b69c9aa2c03ad8e8'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=ru" # Прогноз на текущий день
url2 = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={weather_api_key}&units=metric&lang=ru" # Прогноз на 5 дней

response = requests.get(url) # Прогноз на текущий день
response2 = requests.get(url2) # Прогноз на 5 дней

#print(response.json())

DATABASE_URL = "postgresql://admin:12345@localhost:5432/test_db"  #Адрес бд (Строка подключения)

# Скрипт бота
cities = {
    "Архангельск": "Arkhangelsk",
    "Астрахань": "Astrakhan",
    "Барнаул": "Barnaul",
    "Белгород": "Belgorod",
    "Брянск": "Bryansk",
    "Великий Новгород": "Veliky Novgorod",
    "Владивосток": "Vladivostok",
    "Владикавказ": "Vladikavkaz",
    "Владимир": "Vladimir",
    "Волгоград": "Volgograd",
    "Вологда": "Vologda",
    "Воронеж": "Voronezh",
    "Грозный": "Grozny",
    "Дербент": "Derbent",
    "Екатеринбург": "Yekaterinburg",
    "Иваново": "Ivanovo",
    "Ижевск": "Izhevsk",
    "Иркутск": "Irkutsk",
    "Йошкар-Ола": "Yoshkar-Ola",
    "Казань": "Kazan",
    "Калининград": "Kaliningrad",
    "Калуга": "Kaluga",
    "Кемерово": "Kemerovo",
    "Киров": "Kirov",
    "Кострома": "Kostroma",
    "Краснодар": "Krasnodar",
    "Красноярск": "Krasnoyarsk",
    "Курган": "Kurgan",
    "Курск": "Kursk",
    "Липецк": "Lipetsk",
    "Магнитогорск": "Magnitogorsk",
    "Махачкала": "Makhachkala",
    "Москва": "Moscow",
    "Мурманск": "Murmansk",
    "Набережные Челны": "Naberezhnye Chelny",
    "Нальчик": "Nalchik",
    "Нижний Новгород": "Nizhny Novgorod",
    "Нижний Тагил": "Nizhny Tagil",
    "Новокузнецк": "Novokuznetsk",
    "Новороссийск": "Novorossiysk",
    "Новосибирск": "Novosibirsk",
    "Норильск": "Norilsk",
    "Омск": "Omsk",
    "Орел": "Oryol",
    "Оренбург": "Orenburg",
    "Пенза": "Penza",
    "Пермь": "Perm",
    "Петрозаводск": "Petrozavodsk",
    "Петропавловск-Камчатский": "Petropavlovsk-Kamchatsky",
    "Псков": "Pskov",
    "Пятигорск": "Pyatigorsk",
    "Ростов-на-Дону": "Rostov-on-Don",
    "Рязань": "Ryazan",
    "Самара": "Samara",
    "Санкт-Петербург": "Saint Petersburg",
    "Саранск": "Saransk",
    "Саратов": "Saratov",
    "Севастополь": "Sevastopol",
    "Симферополь": "Simferopol",
    "Смоленск": "Smolensk",
    "Сочи": "Sochi",
    "Ставрополь": "Stavropol",
    "Сургут": "Surgut",
    "Суздаль": "Suzdal",
    "Сыктывкар": "Syktyvkar",
    "Тамбов": "Tambov",
    "Тверь": "Tver",
    "Тольятти": "Tolyatti",
    "Томск": "Tomsk",
    "Тула": "Tula",
    "Тюмень": "Tyumen",
    "Улан-Удэ": "Ulan-Ude",
    "Ульяновск": "Ulyanovsk",
    "Уфа": "Ufa",
    "Хабаровск": "Khabarovsk",
    "Ханты-Мансийск": "Khanty-Mansiysk",
    "Чебоксары": "Cheboksary",
    "Челябинск": "Chelyabinsk",
    "Череповец": "Cherepovets",
    "Чита": "Chita",
    "Элиста": "Elista",
    "Южно-Сахалинск": "Yuzhno-Sakhalinsk",
    "Якутск": "Yakutsk",
    "Ярославль": "Yaroslavl"
}  #Список городов

@bot.message_handler(commands=['start'])        #  Вступительное сообщение
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nНапиши свой город:"
  bot.send_message(message.chat.id, first_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])        #Обработчик сообщений
def city(message):

    engine = create_engine(DATABASE_URL)  # Создание движка
    metadata = MetaData()  # Объявление контейнера для БД
    table = Table("user_activity_log", metadata, autoload_with=engine)  # Авто-считывание структуры таблицы
    table2 = Table("request_not_found_log", metadata, autoload_with=engine)  # Авто-считывание структуры таблицы

    message_cap = message.text.capitalize()  #Преобразование слова к заглавной первой букве
    city = f" Погода в {message.text}:"
    #send_msg = bot.send_message(message.chat.id, city, parse_mode='html')

    if message_cap in cities:
        response3 = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={cities[message_cap]}&appid={weather_api_key}&units=metric&lang=ru").json()
        fin_msg = f" Погода в {message_cap}е: {response3['weather'][0]['description']}, температура {response3['main']['temp']} °C, ощущается как {response3['main']['feels_like']} °C, давление  {round((response3['main']['pressure'])/1.333,1)}, влажность {response3['main']['humidity']}%."
        bot.send_message(message.chat.id,  fin_msg  , parse_mode='html')
            # Вставка данных в БД для Логирования
        log_data = {
            message.text: response3['weather'][0]['description'],
            'температура': response3['main']['temp'],
            'ощущается как': response3['main']['feels_like'],
            'давление': round((response3['main']['pressure']) / 1.333, 1),
            'влажность': response3['main']['humidity']
            }                                                            # Json для БД
        with engine.begin() as conn:
            # Собираем запрос
            stmt = insert(table).values(user_id = message.from_user.id, username= message.from_user.username, data= log_data)
            # Выполняем
            conn.execute(stmt)
    else:
        bot.send_message(message.chat.id, 'Город не найден')
        log_data = {
            'Некорректные данные': message.text }  # Json для БД
        with engine.begin() as conn2:
            # Собираем запрос
            stmt2 = insert(table2).values(user_id=message.from_user.id, username=message.from_user.username,
                                        data=log_data)
            # Выполняем
            conn2.execute(stmt2)

    user_id = message.from_user.id
    username = message.from_user.username

# Скрипт для БД: (Добавить обработку в ELSE текста не подходящего под город, добавить новую таблицу пример: request_not_found_log)

'''DATABASE_URL = "postgresql://admin:12345@localhost:5432/test_db"
engine = create_engine(DATABASE_URL)
try:
    with engine.connect() as connection:
        # Просим базу просто посчитать 1+1
        result = connection.execute(text("SELECT 1 + 1"))
        print(f"✅ Связь с Postgres установлена! Результат теста: {result.scalar()}")
except Exception as e:
    print(f"❌ Ошибка подключения! Проверь пароль или имя базы.\nТекст ошибки: {e}")#'''

DATABASE_URL = "postgresql://admin:12345@localhost:5432/test_db"
engine = create_engine(DATABASE_URL)
#connection = engine.connect()
'''
# 2. Выполняем запрос (если тут будет ошибка, программа просто упадет)
result = connection.execute(text("SELECT 1 + 1"))
# 3. Достаем и выводим результат
print(f"✅ Результат теста: {result.all()}")    #{result.scalar()}
# 4. ОБЯЗАТЕЛЬНО закрываем соединение сами
connection.close()
'''

bot.polling(none_stop=True)