from src.models.rule import Rule
from src.models.term import Term
from src.reasoner import Reasoner


def main():

    knowledge_base = [
        (['expensive', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['popular', 'P']]),
        (['regular', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['common', 'P']]),
        (['cheap', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['popular', 'P']]),
    ]

    knowledge_base1 = [
        Rule(Term('expensive', ['X', '|', 'T']), [
                    Term('landmark', ['Y', '_', 'P', '_', '|', '_']),
                    Term('calcDist', 'X', 'Y', 'D'),
                    Term('near', 'D'),
                    Term('popular', 'P')]),
        (['regular', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['common', 'P']]),
        (['cheap', ['X', '|', 'T']], [['landmark', ['Y', '_', 'P', '_', '|', '_']], ['calcDist', 'X', 'Y', 'D'], ['near', 'D'], ['popular', 'P']]),
    ]

    reasoner = Reasoner({})


if __name__ == "__main__":
    main()


