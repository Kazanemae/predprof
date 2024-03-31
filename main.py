from api import get_date, get_date_info, post_answer
from calcul import formula


data = get_date_info(25, 1, 23)
rooms = formula(data['rooms_count'], data['windows_for_room_list'],{
    "floor_1": data['windows_dict']['floor_1'],
    "floor_2": data['windows_dict']['floor_2'],
    "floor_3": data['windows_dict']['floor_3'],
    "floor_4": data['windows_dict']['floor_4']
})
print(post_answer(rooms, '25-01-23'))

room_dict = {}
room = 0
for floor in range(1, 5):
    room_list = []
    for windows_for_room in data['windows_for_room_list']:
        room += 1
        for __ in range(windows_for_room):
            room_list.append(room)
    room_dict[f'floor_{floor}'] = room_list
