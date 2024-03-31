from requests import get, post


TOKEN = 'ppo_9_30000'
HEADERS = {'X-Auth-Token': TOKEN}


def get_date():
    req = get('https://olimp.miet.ru/ppo_it_final/date', headers=HEADERS)
    date_list = req.json()['message']

    return date_list


def get_date_info(day, month, year):
    req = get(f'https://olimp.miet.ru/ppo_it_final?day={day}&month={month}&year={year}', headers=HEADERS)
    data = req.json()['message']

    flats_count = data['flats_count']['data']
    windows_for_flat = data['windows_for_flat']['data']
    windows_dict = data['windows']['data']

    return_data = {
        'flats_count': flats_count,
        'windows_for_flat': windows_for_flat,
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

    req = post(f'https://olimp.miet.ru/ppo_it_final', headers=HEADERS, data=data)

    answer = req.json()['message']

    return answer
