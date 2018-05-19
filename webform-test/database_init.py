from tinydb import TinyDB
db = TinyDB('forms.json')




db.insert({'name': 'UserInfo', 'first_name': 'text',
           'last_name': 'text', 'email': 'email',
           'password': 'text', 'phone_number': 'phone',
           'birthdate': 'date'})


db.insert({'name':'OrderInfo', 'order_id': 'text',
           'email': 'email', 'order_date': 'date',
           'delivery_date': 'date'})


db.insert({'name': 'LoginInfo', 'email': 'email',
           'password': 'text'})


db.insert({'name': 'RegInfo', 'email': 'email',
           'reg_date': 'date'})