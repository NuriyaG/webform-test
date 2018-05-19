Web-приложение для определения заполненных форм
python 3.6
1. установка необходимых пакетов:
pip install -r requirements.txt
2. запуск приложения:
python webform-test/main.py
3. запуск скрипта с тестовыми запросами:
pytest -v

Пример запроса:
curl 'http://127.0.0.1:5000/get_form' -d 'phone=%2B7 999 999 88 88&not_phone=%2B7123456789'

Примечания:
* формат телефона - '+7 xxx xxx xx xx' (16 знаков), при написании запроса через curl стоит заменить знак '+' на его код '%2B', иначе он заменяется пробелом
* формат даты - 'DD.MM.YYYY' или 'YYYY-MM-DD'
* формат email - 1 вхождение знака @, хотя бы один знак до него, хотя бы 2 после него, разделенные точкой
* файл database_init.py создает базу данных
* файл forms.json - база данных