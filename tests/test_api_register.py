import json
import logging
import random

import requests

from app_constants import API_TEST_URL, PASSWORD


def test_api_register(asserts):
    'Проверяю позитивный сценарий регистрации пользователя через API.'

    headers = {'Content-Type': "application/json; charset=utf-8", 'Accept': "application/json"}
    test_data = {'email': f'holy_test_ui_login{random.randint(1000, 10000)}@ddd.ru',
                 'password': PASSWORD,
                 'confirm_password': PASSWORD}

    r = requests.post(url=API_TEST_URL, data=json.dumps(test_data), headers=headers)
    asserts.accumulate(r.json(), f'Ответ в формате json, получил {r.text}')
    asserts.accumulate(list(r.json().keys()) ==
                       ['token', 'email', 'id'], f"Ожидаю список ключей - ['token', 'email', 'id'], "
                                                 f"получил - {list(r.json().keys())}")
    asserts.accumulate(r.json()['email'] == test_data['email'], f'Ожидаю email - {test_data["email"]}, '
                                                                f'получил - {r.json()["email"]}')
    asserts.accumulate(r.status_code == 200, f'Ожидаю код ответа - 200, получил - {r.status_code}')

    asserts.release()
