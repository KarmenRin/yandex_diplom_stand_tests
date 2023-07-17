import requests

from configuration import *
from data import *


def post_new_order(body):
    """Функция создания нового заказа"""
    return requests.post(URL_SERVICE + CREATE_ORDER_PATH,
                         json=body,
                         headers=headers)


def get_order(track):
    """Функция получения заказа по его номеру"""
    return requests.get(URL_SERVICE + GET_ORDER_PATH + str(track))


def test_positive_assert():
    """Тестирование создания нового заказа"""
    track = post_new_order(order_body).json()['track']
    assert get_order(track).status_code == 200