from unittest import TestCase

from idrw.utils import int_list_to_hex

class UtilsTestCase(TestCase):

    def test_int_list_to_hex(self):
        int_lists = [([7, 7], 1799),
                     ([23, 45], 5933),
                     ([7], 7),
                     ([73, 150, 2, 210], 1234567890)]
        for list_test in int_lists:

            self.assertEqual(int_list_to_hex(list_test[0]), list_test[1])
