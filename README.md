# Django_tutorial

# Клонувати репозиторій
git clone https://github.com/igorkulish09/Django_tutorial.git

# Перейти до директорії проекту
cd \Users\Kulish_Family\PycharmProjects\Django_tutorial

# Створити та активувати віртуальне середовище
python -m venv venv
source venv/bin/activate

# Встановити залежності
pip install -r requirements.txt

# Застосувати міграції
python manage.py migrate

# Запустити сервер розробки
python manage.py runserver

# Доступ до адмін-панелі
http://localhost:8000/admin/

