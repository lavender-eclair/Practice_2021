import telebot
import vk
import requests

bot = telebot.TeleBot('')


def get_url():
    with open('vk_api_token') as f:
        access_token = f.read()[:-1]
    owner_id = -193294595  # id сообщества
    count = 25  # количество постов, среди которых мы ищем
    v = 5.131  # версия API
    mainpage = 'https://api.vk.com/method/wall.get?'
    parameters = 'owner_id=' + str(owner_id) + '&' + 'count=' + str(count) + \
                 '&' + 'access_token=' + access_token + '&' + 'v=' + str(v)
    url = mainpage + parameters
    return url


def statistics(url):
    counter = 0
    response = requests.get(url)
    posts = response.json()['response']['items']
    for post in posts:  # ищем первый пост, который не содержит текста
        if post['text'] == "":
            ans = post['attachments'][0]['photo']['sizes'][-1]['url']
            counter += 1
            break
    if counter > 0:
        return ans
    else:
        return 'Нет свежих данных по этому запросу'


def dynamics(url):
    counter = 0
    response = requests.get(url)
    posts = response.json()['response']['items']
    s = "Динамика заболевших, выздоровевших в Брянской области по состоянию на"
    # подстрока, которая встечается во всех постах такого типа
    for post in posts:  # ищем первый пост, в который входит подстрока
        if s in post['text']:
            ans = post['attachments'][0]['photo']['sizes'][-1]['url']
            counter += 1
            break
    if counter > 0:
        return ans
    else:
        return 'Нет свежих данных по этому запросу'


def vaccine(url):
    counter = 0
    response = requests.get(url)
    posts = response.json()['response']['items']
    s = "прививку от коронавирусной инфекции. Таковы данные оперштаба"
    # подстрока, которая встечается во всех постах такого типа
    for post in posts:  # ищем первый пост в который входит подстрока
        if s in post['text']:
            ans = post['text']
            counter += 1
            break
    if counter > 0:
        return ans
    else:
        return 'Нет свежих данных по этому запросу'


def kovivak(url):
    counter = 0
    response = requests.get(url)
    posts = response.json()['response']['items']
    s = "КовиВак"  # подстрока, которая встечается во всех постах такого типа
    for post in posts:  # ищем первый пост, в который входит подстрока
        if s in post['text']:
            ans = post['text']
            counter += 1
            break
    if counter > 0:
        return ans
    else:
        return 'К сожалению, нет новых данных про вакцину'


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Привет! Напиши /help, чтобы посмотреть,"
                         "что я могу")
    elif message.text == "статистика":
        url = get_url()
        bot.send_message(message.from_user.id, statistics(url))
    elif message.text == "динамика":
        url = get_url()
        bot.send_message(message.from_user.id, dynamics(url))
    elif message.text == "количество вакцинированных":
        url = get_url()
        bot.send_message(message.from_user.id, vaccine(url))
    elif message.text == "КовиВак":
        url = get_url()
        bot.send_message(message.from_user.id,
                         "О, а вот и новая иформация про "
                         "вакцину Ковивак:\n\n" + kovivak(url))
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "Напиши: статистика, динамика, КовиВак "
                         "или количество вакцинированных")
    else:
        bot.send_message(message.from_user.id,
                         "Упс, твоя моя не понимать. Напиши /help.")


bot.polling()
