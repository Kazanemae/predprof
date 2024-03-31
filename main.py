from api import get_date, get_date_info, post_answer
from calcul import formula


def get_all_dates():
    date_list = get_date()

    return date_list


def get_info(date: str): #dd-mm-yy
    day = date.split('-')[0]
    month = date.split('-')[1]
    year = date.split('-')[2]

    data = get_date_info(day, month, year)
    rooms = formula(data['rooms_count'], data['windows_for_room_list'],{
        "floor_1": data['windows_dict']['floor_1'],
        "floor_2": data['windows_dict']['floor_2'],
        "floor_3": data['windows_dict']['floor_3'],
        "floor_4": data['windows_dict']['floor_4']
    })
    server_answer = post_answer(rooms, date)

    window_list = []
    room = 0
    for floor in range(1, 5):
        room_list = []
        for windows_for_room in data['windows_for_room_list']:
            room += 1
            for __ in range(windows_for_room):
                room_list.append(room)
        window_list.append(room_list)

    return window_list
    # data_to_return = {
    #     'true_rooms': rooms,
    #     'true_rooms_count': rooms,
    #     'window_list': window_list,


    # }


print(get_info('25-01-23'))
# [[1, 1, 1, 2, 2, 3], [4, 4, 4, 5, 5, 6], [7, 7, 7, 8, 8, 9], [10, 10, 10, 11, 11, 12]]