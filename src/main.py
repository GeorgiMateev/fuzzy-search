from typing import List

from src.models.calc_dist import CalculateDistance
from src.models.fuzzy_number import FuzzyNumber
from src.models.rule import Rule
from src.models.term import Term
from src.reasoner import Reasoner


def main():

    # knowledge_base = [
    #     (['expensive', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['popular', 'P']]),
    #     (['regular', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['common', 'P']]),
    #     (['cheap', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['popular', 'P']]),
    # ]
    #
    # knowledge_base1 = [
    #     Rule(Term('expensive', ['X', '|', 'T']), [
    #                 Term('landmark', ['Y', '_', 'P', '_', '|', '_']),
    #                 Term('calcDist', 'X', 'Y', 'D'),
    #                 Term('near', 'D'),
    #                 Term('popular', 'P')]),
    #     (['regular', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['common', 'P']]),
    #     (['cheap', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['popular', 'P']]),
    # ]
    # List
    knowledge_base2 = [
        Rule(FuzzyNumber('near', (0, 0, 400), 'X'), []),
        Rule(FuzzyNumber('popular', (20, 500, 500), 'X'), []),
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

    reasoner = Reasoner(knowledge_base2)
    query_results = reasoner.query(Term('expensive', ['sheraton', 354, 744, 4.2, 5]))
    for result in query_results:
        print(result)


if __name__ == "__main__":
    main()


