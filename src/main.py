from src.config.config import Config
from src.models.rule import Rule
from src.models.term import Term
from src.modules.fuzzy.fuzzy_number import FuzzyNumber
from src.modules.geolocation.calc_dist import CalculateDistance
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

    CalculateDistance.create_api(Config.get_secrets()['gmaps']['key'])

    knowledge_base3 = [
        # Distance
        Rule(FuzzyNumber('near', (0, 0, 400), 'X'), []),
        Rule(FuzzyNumber('distant', (300, 1400, 2000), 'X'), []),
        Rule(FuzzyNumber('away', (1500, 2000, 3000), 'X'), []),

        # Cost
        Rule(FuzzyNumber('cheapRoom', (0, 0, 100), 'X'), []),
        Rule(FuzzyNumber('regularRoom', (80, 100, 150), 'X'), []),
        Rule(FuzzyNumber('expensiveRoom', (120, 500, 500), 'X'), []),

        Rule(FuzzyNumber('cheapDinner', (0, 0, 20), 'X'), []),
        Rule(FuzzyNumber('regularDinner', (15, 25, 40), 'X'), []),
        Rule(FuzzyNumber('expensiveDinner', (30, 60, 60), 'X'), []),

        Rule(FuzzyNumber('cheapCoffee', (0, 0, 2), 'X'), []),
        Rule(FuzzyNumber('regularCoffee', (1, 5, 8), 'X'), []),
        Rule(FuzzyNumber('expensiveCoffee', (6, 10, 10), 'X'), []),

        Rule(FuzzyNumber('cheapVisit', (0, 0, 5), 'X'), []),
        Rule(FuzzyNumber('regularVisit', (4, 7, 10), 'X'), []),
        Rule(FuzzyNumber('expensiveVisit', (9, 15, 15), 'X'), []),

        # Popularity
        Rule(FuzzyNumber('unknown', (0, 70, 100), 'X'), []),
        Rule(FuzzyNumber('common', (80, 200, 500), 'X'), []),
        Rule(FuzzyNumber('popular', (400, 1500, 1500), 'X'), []),

        # Quality
        Rule(FuzzyNumber('poor', (0, 0, 4), 'X'), []),
        Rule(FuzzyNumber('good', (3, 4, 5), 'X'), []),
        Rule(FuzzyNumber('great', (4, 5, 5), 'X'), []),

        Rule(Term('hotel', ['sheraton', 'pl. "Sveta Nedelya" 5, 1000 Sofia Center, Sofia', 354, 744, 4.2]), []),
        Rule(Term('hotel', ['kapri', 'ul. "Han Omurtag" 76, 1124 g.k. Yavorov, Sofia', 109, 24, 4.2]), []),
        Rule(Term('hotel', ['sense', 'bul. "Tsar Osvoboditel" 16, 1000 Sofia Center, Sofia', 187, 651, 4.5]), []),
        Rule(Term('hotel', ['grand_hotel', 'ul. "General Yosif V. Gourko" 1, 1000 Sofia Center, Sofia', 170, 717, 4.6]), []),
        Rule(Term('hotel', ['les_fleurs', '21, Vitosha Blvd., 1000 Sofia', 274, 183, 4.3]), []),
        Rule(Term('hotel', ['hilton', 'Bulevard "Bulgaria" 1, 1421 g.k. Lozenets, Sofia', 230, 405, 4.5]), []),
        Rule(Term('hotel', ['hemus', 'бул. Черни Връх 31, 1421 g.k. Lozenets, Sofia', 77, 420, 3.4]), []),

        Rule(Term('dinner', ['happy', 'ulitsa „Georgi S. Rakovski“ 145A, 1000 Sofia Center, Sofia', 20, 1126, 4.2]), []),
        Rule(Term('dinner', ['social', 'bul. "Vitosha" 16, 1000 Sofia Center, Sofia', 20, 1024, 4.2]), []),
        Rule(Term('dinner', ['shtastlivetsa', 'bul. "Vitosha" 27, 1000 Sofia Center, Sofia', 30, 1354, 4.5]), []),
        Rule(Term('dinner', ['mrpizza', 'bulevard "Cherni vrah" 38, 1000 g.k. Lozenets, Sofia', 15, 534, 4.1]), []),
        Rule(Term('dinner', ['sasa', 'pl. "Narodno sabranie" 4, 1000 Sofia Center, Sofia', 35, 268, 4.3]), []),
        Rule(Term('dinner', ['skaptobara', 'ul. "Iskar" 11А, 1000 Sofia Center, Sofia', 10, 494, 4.5]), []),

        Rule(Term('landmark', ['st_nedelia', 'площад Света Неделя 20, 1000 Sofia Center, Sofia', 0, 330, 4.7]), []),
        Rule(Term('landmark', ['nevski', 'pl. "Sveti Aleksandar Nevski", 1000 Sofia Center, Sofia', 0, 1104, 4.7]), []),
        Rule(Term('landmark', ['orlov_most', 'бул. „Цар Освободител“ 33, 1504 Sofia Center, Sofia', 0, 1671, 4.2]), []),
        Rule(Term('landmark', ['national_palace_culture', 'National Culture Palace, Bulevard "Bulgaria", 1463 Ndk, Sofia', 10, 1096, 4.2]), []),
        Rule(Term('landmark', ['vitosha', 'ul. "Detski mir", Sofia', 0, 2584, 4.7]), []),

        Rule(Term('coffee', ['costa', 'ploshtad "Knyaz Aleksandar I" 4, 1000 Sofia Center, Sofia', 5, 336, 4.2]), []),
        Rule(Term('coffee', ['starbucks', 'бул. Васил Левски, 1А, 1042 Sofia Center, Sofia', 5, 534, 4.1]), []),
        Rule(Term('coffee', ['memento', 'ulitsa „Georgi S. Rakovski“ 106, 1000 Sofia Center, Sofia', 6, 508, 4.3]), []),
        Rule(Term('coffee', ['modera', 'София, ул. Йордан Йосифов 8а, 1700 Studentski Kompleks, Sofia', 4, 389, 4.1]), []),
        Rule(Term('coffee', ['tu', 'bulevard "Cherni vrah" 96, 1407 Hladilnika, Sofia', 3, 11, 2.2]), []),

        Rule(Term('expensive', ['X', 'XA', '_', '_', '_']),
             [Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('popular', (400, 1500, 1500), 'P')]),

        Rule(Term('regular', ['X', 'XA', '_', '_', '_']),
             [Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('common', (80, 200, 500), 'P')]),

        Rule(Term('cheap', ['X', 'XA', '_', '_', '_']),
             [Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('unknown', (0, 70, 100), 'P')]),

        Rule(Term('great', ['X', 'XA', '_', '_', '_']),
             [Term('dinner', ['X', '_', '_', '_', '_']),
              Term('hotel', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('popular', (400, 1500, 1500), 'P')]),

        Rule(Term('good', ['X', 'XA', '_', '_', '_']),
             [Term('dinner', ['X', '_', '_', '_', '_']),
              Term('hotel', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('common', (80, 200, 500), 'P')]),

        Rule(Term('poor', ['X', 'XA', '_', '_', '_']),
             [Term('dinner', ['X', '_', '_', '_', '_']),
              Term('hotel', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('unknown', (0, 70, 100), 'P')]),

        Rule(Term('great', ['X', 'XA', '_', '_', '_']),
             [Term('hotel', ['X', '_', '_', '_', '_']),
              Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('away', (1500, 2000, 3000), 'D'),
              FuzzyNumber('popular', (400, 1500, 1500), 'P')]),

        Rule(Term('good', ['X', 'XA', '_', '_', '_']),
             [Term('hotel', ['X', '_', '_', '_', '_']),
              Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('distant', (300, 1400, 2000), 'D'),
              FuzzyNumber('popular', (400, 1500, 1500), 'P')]),

        Rule(Term('poor', ['X', 'XA', '_', '_', '_']),
             [Term('hotel', ['X', '_', '_', '_', '_']),
              Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('popular', (400, 1500, 1500), 'P')]),

        Rule(Term('great', ['X', 'XA', '_', '_', '_']),
             [Term('coffee', ['X', '_', '_', '_', '_']),
              Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('popular', (400, 1500, 1500), 'P')]),

        Rule(Term('good', ['X', 'XA', '_', '_', '_']),
             [Term('coffee', ['X', '_', '_', '_', '_']),
              Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('common', (80, 200, 500), 'P')]),

        Rule(Term('poor', ['X', 'XA', '_', '_', '_']),
             [Term('coffee', ['X', '_', '_', '_', '_']),
              Term('landmark', ['Y', 'YA', '_', 'P', '_']),
              CalculateDistance('XA', 'YA', 'D'),
              FuzzyNumber('near', (0, 0, 400), 'D'),
              FuzzyNumber('unknown', (0, 70, 100), 'P')]),
    ]

    reasoner = Reasoner(knowledge_base3)

    query_results = reasoner.complex_query([Term('expensive', ['sheraton', 'pl. "Sveta Nedelya" 5, 1000 Sofia Center, Sofia', 354, 744, 4.2])])
    print('Query result:')

    for result in query_results:
        print(result)

    print()

    search_result = reasoner.complex_query( [Term('landmark', ['X', '_', 'C', 'P', '_']),
                                             FuzzyNumber('popular', (20, 500, 500), 'P'),
                                             FuzzyNumber('cheap', (0, 0, 5), 'C')])

    print('Search result:')
    for result in search_result:
        print(result)


if __name__ == "__main__":
    main()


