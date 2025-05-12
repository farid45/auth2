
#### Создать venv и установить зависимости
```
python3 -m venv library_django
source library_django/bin/activate
pip3 install -r requirements.txt
```

---------------------------------------------------------------------------------------------------------------

### Windows

#### Установить python + git
- Установите Python и git.
- Если вы устанавливаете Python из магазина Microsoft Store, «установка python setup.py» завершится неудачно, но этот шаг не требуется.
- WIN+R ```cmd```

#### Grab файлы и установка
```
git clone https://github.com/bkerler/mtkclient
cd mtkclient
pip3 install -r requirements.txt
```

### Запуск приложения:

#### Запускаем миграцию:
```
python manage.py migrate   
```

### Запускаем сервер
```
python manage.py runserver
```
### Запускаем браузер и вставляем следующую ссылку:
```
http://127.0.0.1:8000/
```