from typing import List

from src.models.calc_dist import CalculateDistance
from src.models.fuzzy_number import FuzzyNumber
from src.models.rule import Rule
from src.models.term import Term
from src.reasoner import Reasoner


def main():
    knowledge_base2 = [
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
              FuzzyNumber('popular', (20, 500, 500), 'P')]),
        # Rule(Term('expensive', ['X', 'C', '_', '_', '_']),
        #      FuzzyNumber('expensive', (120, 500, 500), 'C'))
    ]

    reasoner = Reasoner(knowledge_base2)

    query_results = reasoner.query(Term('expensive', ['sheraton', 354, 744, 4.2, 5]))
    print('Query result:')

    for result in query_results:
        print(result)

    print()

    search_result = reasoner.complex_query( [Term('landmark', ['X', 'C', 'P', '_', '_']),
                                             FuzzyNumber('popular', (20, 500, 500), 'P'),
                                             FuzzyNumber('cheap', (0, 0, 100), 'C')])

    print('Search result:')
    for result in search_result:
        print(result)



if __name__ == "__main__":
    main()


