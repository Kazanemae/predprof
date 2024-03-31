from requests import get, post


TOKEN = 'ppo_9_30000'
HEADERS = {'X-Auth-Token': TOKEN}


def get_date():
    req = get('https://olimp.miet.ru/ppo_it_final/date', headers=HEADERS)
    date_list = req.json()['message']

    return date_list


def get_date_info(day, month, year):
    req = get(f'https://olimp.miet.ru/ppo_it_final/?day=<{day}>&month=<{month}>&<{year}>')
    data = req.json()['message']

    rooms_count = data['rooms_count']['data']
    windows_for_room_list = data['windows_for_room']['data']
    windows_dict = data['windows']['data']

    return_data = {
        'rooms_count': rooms_count, 
        'windows_for_room_list': windows_for_room_list,
        'windows_dict': windows_dict
    }

    return  return_data


def post_answer(count: int, rooms: list[int], date: str):
    body = {
        "data": {
            "count": count,
            "rooms": rooms
        },
        "date": date
        }
    req = post(f'https://olimp.miet.ru/ppo_it_final/', body=body)

    answer = req.json()['message']

    return answer


