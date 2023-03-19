from requests import get
from json import loads
import numpy as np
import sqlite3 as sql


# <------------------ Создание простой Базы данных --------------->
db = sql.connect("information.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS info(
    number_id INTEGER,
    count_day INTEGER,
    remain_resources INTEGER,
    now_resource INTEGER,
    power_reactor FLOAT,
    len_population INTEGER,
    autoclava TEXT
)
""")
db.commit()

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


def len_new_population_G(g1, g2, K):
    return g1 + g2 * K


def coeficent_K(T, Oxi):
    p = 3.14
    print(not p)
    d = np.sin((-p / 2) + (p * (T + 0.5 * Oxi) / 40))
    return d


# <------------ Основной алгоритм программы -------------->

flight_assigment = get_new_flight_assigment()

