from src.models.rule import Rule
from src.models.term import Term
from src.modules.fuzzy.fuzzy_number import FuzzyNumber
from test.mocks.calc_dist import CalculateDistance

expensive_hotel = [
    Rule(FuzzyNumber('near', (0, 0, 400), 'X'), []),
    Rule(FuzzyNumber('popular', (200, 500, 500), 'X'), []),
    Rule(FuzzyNumber('cheap', (0, 0, 100), 'X'), []),
    Rule(Term('hotel', ['sheraton', 354, 744, 4.2, 5]), []),
    Rule(Term('landmark', ['st_nedelia', 5, 330, 4.7, 5]), []),
    Rule(Term('landmark', ['nevski', 10, 1104, 4.7, 5]), []),
    Rule(Term('expensive', ['X', '_', '_', '_', '_']),
         [Term('landmark', ['Y', '_', 'P', '_', '_']),
          CalculateDistance('X', 'Y', 'D'),
          FuzzyNumber('near', (0, 0, 400), 'D'),
          FuzzyNumber('popular', (20, 500, 500), 'P')])
]