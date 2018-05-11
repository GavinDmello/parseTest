import unittest
from utils import Utils

utilInstance = Utils()

class Test(unittest.TestCase):

    def test1(self):
        date = utilInstance.parseDate("2018-01-10T22:29Z")
        self.assertEqual(date, "10/01/2018")

if __name__ == "__main__":
    unittest.main()