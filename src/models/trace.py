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

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)

    def add_solution(self, solution: Solution):
        self.solutions.append(solution)

    def __str__(self):
        trace_str = str(self.term) \
                    + ((' -> ' + str(self.rule)) if self.rule else '')

        if len(self.solutions) > 0:
            trace_str += '    |'

        for s in self.solutions:
            trace_str += (' ' + str(s))

        for child in self.get_children():
            new_line = '        '.join(('\n' + str(child)).splitlines(True))
            trace_str += new_line

        return trace_str
