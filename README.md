# hq_test
hq_test

## Стек
 - python 3.11
 - django 3.2
 - djangorestframework 3.14.0

## Локальная установка без БД
## Настройка окружения
```bash
git clone https://github.com/ksunik/hq_test.git

# Backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd hq_project
python3 manage.py migrate
python3 manage.py createsuperuser
```

### Запуск проекта
# Запуск backend
```
cd hq_project
python manage.py runserver
```

# API запросы по заданию
- API для выведения списка всех уроков по всем продуктам к которым пользователь имеет доступ, с выведением информации о статусе и времени просмотра
http://127.0.0.1:8000/api/lessons/

- API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ, с выведением информации о статусе и времени просмотра, а также датой последнего просмотра ролика
http://127.0.0.1:8000/api/user-lessons/?product_id=<id>

- API для отображения статистики по продуктам. Необходимо отобразить список всех продуктов на платформе, к каждому продукту приложить информацию:
    a. Количество просмотренных уроков от всех учеников.
    b. Сколько в сумме все ученики потратили времени на просмотр роликов.
    c. Количество учеников занимающихся на продукте.
    d. Процент приобретения продукта (рассчитывается исходя из количества полученных доступов к продукту деленное на общее количество пользователей на платформе)
http://127.0.0.1:8000/api/product_stats/