from typing import Dict, List

from src.models.rule import Rule
from src.models.solution import Solution
from src.models.term import Term


class Trace:

    def __init__(self, term: Term, term_variables, rule: Rule, rule_variables: Dict):
        self.term = term
        self.term_variables = term_variables
        self.rule = rule
        self.rule_variables = rule_variables
        self.parent = None
        self.children = []
        self.solutions: List[Solution] = []

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add_child(self, child):
        self.children.append(child)

    def add_solution(self, solution: Solution):
        self.solutions.append(solution)
