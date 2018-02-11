from typing import Tuple

from src.models.term import Term


class FuzzyNumber(Term):
    def __init__(self, fuzzy_number: Tuple[int, int, int]):
        super(self)
        self.fuzzy_number = fuzzy_number
        self.is_self_solvable = True

    def get_fuzzy_number(self):
        return self.fuzzy_number

    def get_new_term(self, params):
        return FuzzyNumber(*params)

    def assign_variables(self, variables):
        new_term = super(variables)
        new_term.fuzzy_number = self.get_fuzzy_number()

    def self_solve(self):
        param = self.get_param(0)
        if param < self.fuzzy_number[0]:
            return 0
        elif self.fuzzy_number[0] <= param <= self.fuzzy_number[1]:
            return (param - self.fuzzy_number[0]) / (
            self.fuzzy_number[1] - self.fuzzy_number[0])
        elif self.fuzzy_number[1] <= param <= self.fuzzy_number[2]:
            return (self.fuzzy_number[2] - param) / (
            self.fuzzy_number[2] - self.fuzzy_number[1])
        elif param > self.fuzzy_number[2]:
            return 0
        else:
            return 0
