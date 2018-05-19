import json
import pytest
import requests


URL = 'http://127.0.0.1:5000/get_form'

TESTS = [
    ({'first_name': 'Ivan',
      'last_name': 'Ivanov',
       'email': 'test@gmail.com',
       'password': 'qwerty',
       'phone_number': '+7 915 123 45 67',
       'birthdate': '01.03.2000'
     }, ['UserInfo']),

    ({'first_name': 'Ivan',
      'last_name': 'Ivanov',
      'email': 'test@gmail.com',
      'password': 'qwerty',
      'phone_number': '+7 915 123 45 67',
      'birthdate': '2000-03-01'
      }, ['UserInfo']),

    ({
      "first_name": "Ivan",
      "last_name": "Ivanov",
      "email": "test@gmail.com",
      "password": "qwerty",
      "phone_number": "+7 915 123 45 67",
      "birthdate": "01.03.2000",
      "reg_date": "01.05.2018"
    }, ['UserInfo']),

    ({
      "first_name": "Ivan",
      "last_name": "Ivanov",
      "email": "test@gmail.com",
      "password": "qwerty"
    }, ['LoginInfo']),

    ({
      "email": "1@ya.ru",
      "order_id": "12345",
      "order_date": "05.12.2018",
      "delivery_date": "2018-12-05"
    }, ['OrderInfo']),

    ({
      "email": "gmail@mail.ru",
      "date1": "2018-11-2",
      "date2": "2.11.2018",
      "not_date": "2018-13-01"
    },
    [{
      "date1": "date",
      "date2": "date",
      "email": "email",
      "not_date": "text"
    }]),

    ({
      "notmail1": "1@ru",
      "notmail2": "1@@1.ru",
      "mail": "1@1.ru"
    },
    [{
      "mail": "email",
      "notmail1": "text",
      "notmail2": "text"
    }]),

    ({
      "phone": "+7 999 999 88 88",
      "not_phone": "+7123456789"
    },
    [{
      "not_phone": "text",
      "phone": "phone"
    }]),

    ({
      "email": "test@gmail.com",
      "password": "qwerty"
    }, ['LoginInfo']),

    ({
      "mail": "1@1.ru"
    },
    [{
      "mail": "email"
    }]),

    ({
      "email": "test@gmail.com",
      "password": "qwerty",
      "reg_date": "18.04.2008"
    }, ['LoginInfo', 'UserInfo'])]


@pytest.mark.parametrize('input,answer', TESTS)
def test_query(input, answer):
    response = requests.post(URL, data=input)
    try:
        out = response.json()
    except json.decoder.JSONDecodeError:
        out = response.text
    assert out in answer
