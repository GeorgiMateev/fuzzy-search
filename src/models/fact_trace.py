from typing import List

from src.models.solution import Solution
from src.models.term import Term


class FactTrace:

    def __init__(self, term: Term, solution: Solution):
        self.term = term
        self.parent = None
        self.solutions: List[Solution] = []

        self.add_solution(solution)

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add_solution(self, solution: Solution):
        self.solutions.append(solution)
