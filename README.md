# Пульт охраны банка

Сайт с информацией о владельцах пропусков в хранилище банка и историей их визитов.

Для запуска скрипта нужен установленный Python3 и веб-фреймворк Django.

Для запуска проекта нужно:

 1. Скачать и распаковать архив с проектом

 2. Создать и активировать Django-окружение, если его нет :
 
  - в командной строке Anaconda создаем окружение:
    
   ```
       conda create -n djangoenv python=3.6 anaconda 
   ```
 - активируем его: 
   
  ```
    conda activate djangoenv
  ```
 
 Если всё сделано правильно, то к названию оболочки добавится ещё djangoenv
 
 ![Создали и активировали окружение](https://github.com/atskayasatana/Images/blob/20dde0a58f69e6d5643b004ccf2d15d388d401c4/%D0%BF%D0%B5%D1%80%D0%B5%D1%85%D0%BE%D0%B4%20%D0%B2%20%D0%BF%D0%B0%D0%BF%D0%BA%D1%83%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0.png "Активировали окружение")
 
 
3. Для работы с сайтом нужны настройки базы данных, которые нужно внести в .env файл.
   Настройки:
   
   ```Python3
      DB_ENGINE= django.db.backends.postgresql_psycopg2 
      '''
      Настройки БД вносятся по шаблону ниже, postgres - менять не нужно, нужно прописать свои данные:
      
      USER - имя пользователя
      PASSWORD - пароль
      HOST - адрес хоста
      PORT - номер порта
      NAME - название таблицы
      '''
      DB_URL = postgres://USER:PASSWORD@HOST:PORT/NAME 
   
      DEBUG = FALSE # или TRUE
      
      X_FRAME_OPTIONS = '*'

      ALLOWED_HOSTS = # здесь нужно указать через запятую разрешенные сервера 
   ```
 

4. Переходим в папку проекта и загружаем необходимые библиотеки из файла requirements.txt 
   ```
      pip install -r requirements.txt
   ```
5. Для работы нужен SECRET_KEY. Его нужно сгенерировать самостоятельно с помощью команды:
   ```
   python generate_secret_key.py
   ```
   В файле .env появится секретный ключ. Если ключ не будет создан, то проект работать не будет.
   
   
 6. Пишем в командной строке: 
    ```
     python manage.py runserver 0.0.0.0:8000
    ```

Мы должны получить сообщение следующего вида:

 ![Сервер](https://github.com/atskayasatana/Images/blob/5745c6f4324c145b102c3835d034253ba60b2467/managepy.png)

Переходим на http://127.0.0.1:8000/

Сервер выполнил запросы и вернул информацию:
1. Все активные пропуска/Главная страница

 ![Главная](https://github.com/atskayasatana/Images/blob/main/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0.png)

2. Информацию о проходам в хранилище по каждому владельцу/открывается при нажатии на имя. Подозрительным считается визит дольше 25 минут. Контрольное время можно изменить, присвоив переменной MAX_VISIT_DURATION в файле functions.py новое значение.

![Владелец](https://github.com/atskayasatana/Images/blob/97f1cf121b643d7a9c438441de2e3ca891573b33/%D0%92%D0%B8%D0%B7%D0%B8%D1%82%D1%8B%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F.png)

3. Информацию по людям, которые на данный момент времени находятся в хранилище/ по ссылке 
![В хранилище](https://github.com/atskayasatana/Images/blob/97f1cf121b643d7a9c438441de2e3ca891573b33/%D0%A1%D0%B5%D0%B9%D1%87%D0%B0%D1%81%20%D0%B2%20%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D0%BB%D0%B8%D1%89%D0%B5.png)
