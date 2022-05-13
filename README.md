Для запуска проекта установите python версии 3.9.6 и pip

После клонирования перейдите в склонированную папку и выполните следующие команды:
Создайте виртуальное окружение командой

python -m venv venv

Активируйте виртуальное окружение командой

source venv/bin/activate
или
venv\Scripts\activate

Установите зависимости командой

pip install -r requirements.txt

Примените миграции командой

./manage.py migrate

Загрузите фикстурные статьи командой

./manage.py loaddata fixtures/auth_dump.json
./manage.py loaddata fixtures/dump.json

Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin

login: admin

password: admin
