import unittest

from src.reasoner import Reasoner
from test.common_knowledge_bases import *


class FactsCheckingTestCase(unittest.TestCase):
    def test_expensive_hotel_if_popular_landscape(self):
        reasoner = Reasoner(expensive_hotel)

        query_results = reasoner.complex_query([Term('expensive', ['sheraton', 354, 744, 4.2, 5])])

        i = 0
        for r in query_results:
            if i == 0:
                self.assertEqual(r, ([0.275], {}))
            elif i == 1:
                self.assertEqual(r, ([0], {}))
            else:
                self.fail("Only two answers expected.")

            i += 1

if __name__ == '__main__':
    unittest.main()
