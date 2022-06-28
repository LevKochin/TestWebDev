# TestWebDev

Предполагается, что все необходимые стандартные инсталяции, вроде pip, python или django, были проведены
После клонирования репозитория, выполните следующие команды из корневой папки проекта, где распологается manage.py:

 ```
manage.py makemigrations
manage.py migrate
manage.py loaddata userinitdata.json
manage.py loaddata devicesinitdata.json
manage.py loaddata vpninitdata.json
```

Создаем superuser-а 
```
manage.py createsuperuser
```
 
Далее, запуская сервер через окружение или IDE.Чтобы заполнить некоторые дополнительные связи между данными и протестировать приложение на работоспособность,
необходимо зайти по адресу:
```
URL - http://127.0.0.1:8000/admin
```
Вводим созданные данные суперпользователя. Далее - VPN's, предоставьте пользователю лицензию для использования VPN-а.
Далее в Profile, укажите устройство пользователя.
>> По логике вещей, необходимо реализовать считывание устройства через приходящий запрос и сохранять эти данные
>> в базе, и туда - же уходит время захода пользователя на VPN. 

Далее, обязательно, к сформированному URL добавляем дополнительный path
```
URL - http://127.0.0.1:8000/vpndashboard/1
```

Тестируем
