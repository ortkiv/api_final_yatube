# api_final
API для проекта YATUBE
Позволяет делать запросы к базе данных YATUBE:
    - получать, создавать, изменять и удалять записи при наличии соответствующих прав доступа
    - создавать подписки на авторов
Позволяет расширять функциональность проекта YATUBE и связывать его с другими.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ortkiv/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
## Примеры запросов

Получить список постов:
```
GET api/v1/posts/
```
Ответ:
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "author": "Foma",
        "text": "First post",
        "pub_date": "2022-06-26T07:21:33.502337Z",
        "image": null,
        "group": 2
    },
    {
        "id": 2,
        "author": "Sasha",
        "text": "second post",
        "pub_date": "2022-06-26T07:37:50.269787Z",
        "image": null,
        "group": 1
    }
]
```
Получить одну конкретную запись:
```
GET /api/v1/posts/1/
```
Ответ:
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "author": "Foma",
    "text": "First post",
    "pub_date": "2022-06-26T07:21:33.502337Z",
    "image": null,
    "group": 2
}
```
Создать подписку неавторизованным пользователем:
```
GET /api/v1/follow/
```
Ответ:
```
HTTP 401 Unauthorized
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
WWW-Authenticate: Bearer realm="api"

{
    "detail": "Учетные данные не были предоставлены."
}
```

## Авторы

### Виктор Антонов
## О себе:
Начинающий разработчик, студент ЯндексПрактикума -  курс Python-разработчик, в серьёзных проектах пока замечен не был)

[git_hub](https://github.com/ortkiv)

