from requests import get
from json import loads



# <------------ Обьявление функций -------------->

def get_new_flight_assigment(url="https://dt.miet.ru/ppo_it_final"):
    token = "46u76vrf"
    sait = get(url, headers={'X-Auth-Token': token})
    return dict(loads(sait.text))["message"]

def speeds(V, w, m):
    return V * (w/80) * (200/m)

def energy(T):
    t = 0
    for i in range(0, T + 1):
        t += i
    return t



# <------------ ОСновной алгоритм программы -------------->

flight_assigment = get_new_flight_assigment()

