import unittest

from api import get_date, get_date_info, post_answer


class TestApp(unittest.TestCase):
    def test_get_date(self):
        self.assertEqual(get_date(), ['25-01-23', '14-02-23', '18-02-23', '04-03-23', '14-03-23', '18-04-23', '13-09-23', '30-09-23', '30-10-23']) 


unittest.main()


