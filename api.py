from requests import get, post
from json import dumps


TOKEN = 'ppo_9_30000'
HEADERS = {'X-Auth-Token': TOKEN}


# ['25-01-23', '14-02-23', '18-02-23', '04-03-23', '14-03-23', '18-04-23', '13-09-23', '30-09-23', '30-10-23']
def get_date():
    req = get('https://olimp.miet.ru/ppo_it_final/date', headers=HEADERS)
    date_list = req.json()['message']

    return date_list


def get_date_info(day, month, year):
    req = get(f'https://olimp.miet.ru/ppo_it_final?day={day}&month={month}&year={year}', headers=HEADERS)
    data = req.json()['message']

    rooms_count = data['flats_count']['data']
    windows_for_room_list = data['windows_for_flat']['data']
    windows_dict = data['windows']['data']

    return_data = {
        'rooms_count': rooms_count,
        'windows_for_room_list': windows_for_room_list,
        'windows_dict': windows_dict
    }

    return return_data


def post_answer(rooms: list[int], date: str):
    count = len(rooms)
    data = {
        "data": {
            "count": count,
            "rooms": rooms
        },
        "date": date
        }
    print(data)
    req = post(f'https://olimp.miet.ru/ppo_it_final', headers=HEADERS, data=data)

    answer = req.json()['message']

    return answer
