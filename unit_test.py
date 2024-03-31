import unittest

from api import get_date, get_date_info, post_answer
from main import get_all_dates, get_info


class TestApp(unittest.TestCase):
    def test_get_date(self):
        self.assertEqual(get_date(), ['25-01-23', '14-02-23', '18-02-23', '04-03-23', '14-03-23', '18-04-23', '13-09-23', '30-09-23', '30-10-23']) 

    def test_get_date_info(self):
        self.assertEqual(get_date_info(25, 1, 23), {'rooms_count': 3, 'windows_for_room_list': [3, 2, 1], 'windows_dict': {'floor_1': [False, True, False, True, False, False], 'floor_2': [True, False, True, False, False, True], 'floor_3': [False, False, True, False, True, False], 'floor_4': [False, False, False, True, False, True]}}) 

    def test_post_answer(self):
        self.assertEqual(post_answer([1, 2, 4, 6, 7, 8, 11, 12], '25-01-23'), 'Wrong data')

    def test_get_all_dates(self):
        self.assertAlmostEqual(get_all_dates(), ['25-01-23', '14-02-23', '18-02-23', '04-03-23', '14-03-23', '18-04-23', '13-09-23', '30-09-23', '30-10-23'])

    def test_get_info(self):
        self.assertAlmostEqual(get_info('25-01-23'), {'window_list': [[1, 1, 1, 2, 2, 3], [4, 4, 4, 5, 5, 6], [7, 7, 7, 8, 8, 9], [10, 10, 10, 11, 11, 12]], 'true_rooms': [1, 2, 4, 6, 7, 8, 11, 12], 'true_rooms_count': 8, 'rooms_count': 3, 'windows': [3, 2, 1], 'server_answer': 'Wrong data', 'date': '25-01-23'})

unittest.main()
