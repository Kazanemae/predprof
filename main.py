from api import get_date, get_date_info, post_answer
from calcul import formula
from flask import Flask, render_template, jsonify
from sqlite3 import connect

import connection as connection
from requests import get, post

TOKEN = 'ppo_9_30000'
HEADERS = {'X-Auth-Token': TOKEN}

app = Flask(__name__)


def get_all_dates():
    date_list = get_date()

    return date_list


def get_info(date: str):  # dd-mm-yy
    day = date.split('-')[0]
    month = date.split('-')[1]
    year = date.split('-')[2]

    data = get_date_info(day, month, year)
    rooms = formula(data['flats_count'], data['windows_for_flat'], {
        "floor_1": data['windows_dict']['floor_1'],
        "floor_2": data['windows_dict']['floor_2'],
        "floor_3": data['windows_dict']['floor_3'],
        "floor_4": data['windows_dict']['floor_4']
    })
    server_answer = post_answer(rooms, date)

    window_list = []
    room = 0
    for _ in range(1, 5):
        room_list = []
        for windows_for_room in data['windows_for_flat']:
            room += 1
            for __ in range(windows_for_room):
                room_list.append(room)
        window_list.append(room_list)

    data_to_return = {
        'window_list': window_list,
        'true_rooms': rooms,
        'true_rooms_count': len(rooms),
        'rooms_count': data['flats_count'],
        'windows': data['windows_for_flat'],
        'server_answer': server_answer,
        'date': date
    }
    print(data_to_return)
    return data_to_return


def getTT(day, month, year):
    req = get(f'https://olimp.miet.ru/ppo_it_final?day={day}&month={month}&year={year}', headers=HEADERS)
    data = req.json()['message']
    return data


stroka = '25-01-23'
day = stroka.split('-')[0]
month = stroka.split('-')[1]
year = stroka.split('-')[2]
data = getTT(day, month, year)
s = get_info(stroka)["window_list"]
s1 = get_info(stroka)["true_rooms"]
comnaty = get_info(stroka)["true_rooms_count"]
result = get_info(stroka)["server_answer"]


def insertINtoBD(ans):
    n = len(ans["windows"]["data"])
    # print('|'.join(ans["windows"]["data"]))
    dataForWindows = []
    for i in range(n):
        dataForWindows.append('|'.join(ans["windows"]["data"]["floor_" + str(i + 1)]))
    s1 = '!'.join(dataForWindows)
    s2 = list(map(str, ans["windows_for_room"]["data"]))
    windows_for_rooms = '|'.join(s2)
    cursor = connection.cursor()
    id = len(cursor.execute("SELECT * FROM res").fetchall())
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO res (id, data, roomscount, zapolnenieRooms, dataForWindows)
            VALUES  (?, ?, ?, ?, ?)""",
            (id, ans["date"]["data"], ans["rooms_count"]["data"], windows_for_rooms, s1))
        connection.commit()
    print(cursor.execute("SELECT * FROM res").fetchall())


data = getTT(day, month, year)
insertINtoBD(data)
print(data)


@app.route('/')
def index():
    wList = s
    nomera = s1
    return render_template('index2.html', rooms_count=data['flats_count']['data'],
                           windows_for_room=data['windows_for_flat']['data'],
                           windows=data['windows']['data'], n=len(data["windows"]["data"]), mas=wList,
                           lenMas=len(wList), kolvo=len(wList[0]), comnaty=comnaty, nomera=nomera, result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

# print(get_info('25-01-23'))
