# Practice_2021
После просмотра лекций был создан телеграм-бот, который по запросу выдает информацию о распространении Covid-19 на территории Брянской области (статистику заболеваемости, динамику заболевших и выздоровевших, количество вакцинированных и данные о вакцине Ковивак в регионе).
Для создания бота были реализованы функции: 
1) get_url(); 
2) statistics(url);
3) dynamics(url);
4) vaccine(url);
5) kovivak(url);
6) get_text_messages(message)

#### Функция get_url():
Функция содержит переменные: access_token (в котором лежит вк токен), owner_id (id сообщества), count (количество постов, которые будут просматриваться) и v (отвечает за версию VK API). Для того, чтобы получить нужную информаци, был выбрам метод wall.get(), который возвращает список записей со стены сообщества. В переменной mainpage лежит та часть ссылки, которая не будет меняться при изменении параметров. В переменной parameters лежит та часть ссылки, которая отвечает за параметры, которые при желании можно изменить: id сообщества, со стены которого нужно получить записи, количество постов, которые вернет wall.get(), токен пользователя и версия API. Функция возвращает необходимую нам для запроса ссылку.

#### Функция statistics(url):
Функция принимает на вход ссылку, полученную в результате выполнения функции get_url(). Заводим счетчик counter = 0. В переменной response храним результаты requests.get(). Далее вытаскием нужную нам информацию, т.е. посты и сохраняем их в переменной posts. Далее проходимся по всем постам и ищем превый, в котором нет текста. Берем его post['attachments'], где лежит список с ссылками на одну и ту же картинку, но с разными размерами и выбирам из них самый большой (post['attachments'][0]['photo']['sizes'][-1]['url']), чтобы удобнее было смотреть. Cчетчик увеличиваем на один и прерываем цикл. Если после выполнения всех итераций цикла, счетчик больше нуля, то возвращаем ссылку на найденную картинку. Иначе возвращаем строку "Нет свежих данных по этому запросу", т.к. в рассматриваемых постах не содержится нужной нам информации.

#### Функция dynamics(url):
Функция принимает на вход ссылку, полученную в результате выполнения функции get_url(). Заводим счетчик counter = 0. В переменной response храним результаты requests.get(). Далее вытаскием нужную нам информацию, т.е. посты и сохраняем их в переменной posts. Заводим переменную, в которой храним подстроку "Динамика заболевших, выздоровевших в Брянской области по состоянию на". Далее проходимся по всем постам и ищем превый, в который входит наша подстрока. Берем его post['attachments'], где лежит список с ссылками на одну и ту же картинку, но с разными размерами и выбирам из них самый большой (post['attachments'][0]['photo']['sizes'][-1]['url']), чтобы удобнее было смотреть. Cчетчик увеличиваем на один и прерываем цикл. Если после выполнения всех итераций цикла, счетчик больше нуля, то возвращаем ссылку на найденную картинку. Иначе возвращаем строку "Нет свежих данных по этому запросу", т.к. в рассматриваемых постах не содержится нужной нам информации.

#### Функция vaccine(url):
Функция принимает на вход ссылку, полученную в результате выполнения функции get_url(). Заводим счетчик counter = 0. В переменной response храним результаты requests.get(). Далее вытаскием нужную нам информацию, т.е. посты и сохраняем их в переменной posts. Заводим переменную, в которой храним подстроку "прививку от коронавирусной инфекции. Таковы данные оперштаба". Далее проходимся по всем постам и ищем превый, в который входит наша подстрока. Берем его post['text']. Cчетчик увеличиваем на один и прерываем цикл. Если после выполнения всех итераций цикла, счетчик больше нуля, то возвращаем текст поста. Иначе возвращаем строку "Нет свежих данных по этому запросу", т.к. в рассматриваемых постах не содержится нужной нам информации.

#### Функция kovivak(utl):
Функция принимает на вход ссылку, полученную в результате выполнения функции get_url().Заводим счетчик counter = 0. В переменной response храним результаты requests.get(). Далее вытаскием нужную нам информацию, т.е. посты и сохраняем их в переменной posts. Заводим переменную, в которой храним подстроку "КовиВак". Далее проходимся по всем постам и ищем превый, в который входит наша подстрока. Берем его post['text']. Cчетчик увеличиваем на один и прерываем цикл. Если после выполнения всех итераций цикла, счетчик больше нуля, то возвращаем текст поста. Иначе возвращаем строку "К сожалению, нет новых данных про вакцину", т.к. в рассматриваемых постах не содержится нужной нам информации.

#### Функция get_text_messages(message):
Функция приминает на вход текствовое сообщение от пользователя и в зависимости от текста выводит нужное сообщение и/или рельзьтат выполнения какой-то из вышепредставленных функций.
