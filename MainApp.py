from requests import get
from json import loads



# <------------ Обьявление функций -------------->

def get_new_flight_assigment(url="https://dt.miet.ru/ppo_it_final"):
    token = "46u76vrf"
    sait = get(url, headers={'X-Auth-Token': token})
    return dict(loads(sait.text))["message"]




# <------------ ОСновной алгоритм программы -------------->

flight_assigment = get_new_flight_assigment()

