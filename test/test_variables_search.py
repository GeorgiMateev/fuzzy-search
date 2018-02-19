import unittest

from src.reasoner import Reasoner
from test.common_knowledge_bases import *


class VariablesSearchTestCase(unittest.TestCase):
    def test_search_popular_cheap_landmark(self):
        reasoner = Reasoner(expensive_hotel)

        result = reasoner.complex_query([Term('landmark', ['X', 'C', 'P', '_', '_']),
                                        FuzzyNumber('popular', (20, 500, 500), 'P'),
                                        FuzzyNumber('cheap', (0, 0, 100), 'C')])

        i = 0
        for r in result:
            if i == 0:
                self.assertEqual(r, ([0.6458333333333334], {'X': 'st_nedelia', 'C': 5, 'P': 330}))
            elif i == 1:
                self.assertEqual(r, ([0.9], {'X': 'nevski', 'C': 10, 'P': 1104}))
            else:
                self.fail("Only two answers expected.")

            i += 1


if __name__ == '__main__':
    unittest.main()
