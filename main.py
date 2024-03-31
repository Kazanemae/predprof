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