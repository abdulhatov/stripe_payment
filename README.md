## Главная информация ##
Этот проект представляет собой простой онлайн платеж.

## Технологии ##
python == 3.10
Django == 4.1
postgres == 14.1
stripe

## Установка ##

1.  git clone https://github.com/abdulhatov/agricultural.git
2. cd agricultural

3. Создать .env
    ### DJANGO SECRET KEY ###
    SECRET_KEY=<django secret key>
4. 
    ### DB POSTGRES ###
    DB_NAME=<Имя БД>
    DB_USER=<Юзер БД>
    DB_PASSWORD=<Пароль БД>
    DB_HOST=<Xост БД>
    DB_PORT=<Порт БД> #поумолчанию 5432

5. создать файл init.sql
   CREATE DATABASE <Имя БД>;
   CREATE USER <Юзер БД> WITH PASSWORD '<пароль>';
   GRANT ALL PRIVILEGES ON DATABASE <Имя БД> TO <Юзер БД>;

6. docker-compose build

7. docker-compose up

8. Для того чтобы создать админ:
   1. docker-compose up -d
   2. docker exec -it web python3 manage.py createsuperuser


    