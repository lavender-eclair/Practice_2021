## Practice_2021
После просмотра лекций был создан телеграм-бот, который по запросу выдает информацию о распространении Covid-19 на территории Брянской области (статистику заболеваемости, динамику заболевших и выздоровевших, количество вакцинированных и данные о вакцине Ковивак в регионе).
Для создания бота были реализованы функции get_url(), statistics(url), dynamics(url), vaccine(url) и kovivak(url).\\
#Функция get_url():
Функция содержит переменные: access_token (в котором лежит), owner_id (id сообщества), count (количество постов, которые будут просматриваться) и v (отвечает за версию VK API). Для того, чтобы получить нужную информаци, был выбрам метод wall.get(), который возвращает список записей со стены пользователя или сообщества.
