from typing import Tuple

from src.models.term import Term


class FuzzyNumber(Term):
    def __init__(self, functor: str, fuzzy_number: Tuple[int, int, int], *args):
        new_args = list((functor, *args))
        super(FuzzyNumber, self).__init__(*new_args)
        self.fuzzy_number = fuzzy_number
        self.is_self_solvable = True

    def get_fuzzy_number(self):
        return self.fuzzy_number

    def get_new_term(self, params):
        return FuzzyNumber(params[0], self.fuzzy_number, *params[1:])

    def assign_variables(self, variables):
        new_term = super(FuzzyNumber, self).assign_variables(variables)
        new_term.fuzzy_number = self.get_fuzzy_number()
        return new_term

    def self_solve(self):
        param = self.get_param(0)
        if not isinstance(param, int) or isinstance(param, float):
            raise ValueError('Please provide int or float parameter to the term.')

        if self.fuzzy_number[0] == self.fuzzy_number[1] and param <= self.fuzzy_number[0]:
            return 1, {}
        elif self.fuzzy_number[1] == self.fuzzy_number[2] and param >= self.fuzzy_number[2]:
            return 1, {}
        elif param < self.fuzzy_number[0]:
            return 0, {}
        elif self.fuzzy_number[0] <= param <= self.fuzzy_number[1]:
            return (param - self.fuzzy_number[0]) / (
            self.fuzzy_number[1] - self.fuzzy_number[0]), {}
        elif self.fuzzy_number[1] <= param <= self.fuzzy_number[2]:
            return (self.fuzzy_number[2] - param) / (
            self.fuzzy_number[2] - self.fuzzy_number[1]), {}
        elif param > self.fuzzy_number[2]:
            return 0, {}
        else:
            return 0, {}
