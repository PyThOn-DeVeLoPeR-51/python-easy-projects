import unittest
from functions_tests import fullname

# class NumTest(unittest.TestCase):
#     def num_max_test(self):
#         x = maxNum(3, 6, 8)
#         self.assertEqual(maxNum(x, 10))
        
# unittest.main()

# class EvenNumTest(unittest.TestCase):
#     def even_num_test(self):
#         self.assertEqual(evenNum, 'Bu juft son')
        
# unittest.main()


class FullNameTest(unittest.TestCase):
    def fullName(self):
        name = fullname('botir', 'qodirov')
        self.assertEqual(name, 'Botir Qodirov')
        
unittest.main()