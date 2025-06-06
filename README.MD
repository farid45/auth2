
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
# Для проекта необходимо создать приложение на GITHUB

# Создание OAuth приложения в GitHub

## 1. Авторизация и переход в настройки
1. Войдите в свой GitHub аккаунт
2. Кликните на аватар профиля → "Settings"
3. В боковом меню выберите "Developer settings"
4. Перейдите в раздел "OAuth Apps"

## 2. Создание нового приложения
Нажмите кнопку "Register a new application" и заполните:

| Поле                  | Описание                                                                 |
|-----------------------|--------------------------------------------------------------------------|
| **Application name**  | Уникальное название вашего приложения (видимое пользователям)           |
| **Homepage URL**      | Основной URL вашего приложения (например, http://localhost:8000)        |
| **Callback URL**      | URL для перенаправления после авторизации  http://localhost:8000/custom-callback/github/|

## 3. Получение учетных данных
После регистрации вы получите:
- 🔑 **Client ID** - публичный идентификатор приложения
- 🔒 **Client Secret** - конфиденциальный ключ 

## 4. Clien_id и Client_secret необходимо прописать в .env в корневой папке проекта.
```bash
# Пример .env конфигурации
NEXTAUTH_URL= "http://localhost:8000"
OAUTH_PROVIDERS="github"
OAUTH_GITHUB_KEY="Ваш id"
OAUTH_GITHUB_SECRET="Ваш секретный ключ"

### Запуск приложения:

#### Запускаем миграцию:
```
python manage.py migrations accounts
python manage.py migrate   
```

### Запускаем сервер
```
python manage.py runserver
```
### Запускаем браузер и вставляем следующую ссылку:
```
http://localhost:8000/s
```