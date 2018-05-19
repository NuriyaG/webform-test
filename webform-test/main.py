from flask import Flask, request, jsonify
from tinydb import TinyDB
import datetime
import re
from collections import namedtuple

FormStats = namedtuple('FormStats', ['name', 'size'])


app = Flask(__name__)


DATE_FORMATS = ['%Y-%m-%d', '%d.%m.%Y']
LENGTH_MOBILE = 16  #format:+7 xxx xxx xx xx
FORMS_PATH = 'webform-test/forms.json'


def validate_date(date_text, date_format):
    is_date = True
    try:
        datetime.datetime.strptime(date_text, date_format)
    except ValueError:
        is_date = False
    return is_date


def validate_phone(text):

    if len(text) != LENGTH_MOBILE:
        return False
    else:
        rule = re.compile(r'\+7( \d{3}){2}( \d{2}){2}')
        return bool(rule.match(text))


def validate_email(text):
    rule = re.compile(r'[^@]+@[^@]+\.[^@]+')
    return bool(rule.match(text))


def determine_field_type(text):
    if any(validate_date(text, date_format) for date_format in DATE_FORMATS):
        return 'date'
    elif validate_phone(text):
        return 'phone'
    elif validate_email(text):
        return 'email'
    else:
        return 'text'


def determine_type(data):
    types = {}
    for field, value in data.items():
        types[field] = determine_field_type(value)
    return types


db = TinyDB(FORMS_PATH)


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form

    input_data = determine_type(data)
    res = []
    for form in db.all():
        contains_input_data = all(True if input_data.get(x) == form[x] else False for x in form if x != 'name')
        if contains_input_data:
            res.append(FormStats(form['name'], len(form)))

    res.sort(key=lambda x: x.size, reverse=True)

    if res:
        return res[0].name
    else:
        return jsonify(input_data)


if __name__ == "__main__":
    app.run(debug=True)