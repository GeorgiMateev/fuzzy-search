from typing import Dict

from src.models.fact_trace import FactTrace
from src.models.rule import Rule
from src.models.solution import Solution
from src.models.term import Term
from src.models.trace import Trace


class Tracer:

    def __init__(self):
        self.current: Trace = None

    def trace_fact(self, term: Term, truthfulness, variables: Dict):
        fact_trace = FactTrace(term, Solution(truthfulness, variables))
        fact_trace.set_parent(self.current)
        if not self.current:
            self.current = fact_trace
        else:
            self.current.add_child(fact_trace)

        self.current = fact_trace

    def trace_rule(self, term: Term, term_variables, rule: Rule, rule_variables: Dict):
        new_trace = Trace(term, term_variables, rule, rule_variables)
        new_trace.set_parent(self.current)
        if not self.current:
            self.current = new_trace
        else:
            self.current.add_child(new_trace)
        self.current = new_trace

    def trace_solution(self, truthfulness, term_variables: Dict):
        self.current.add_solution(Solution(truthfulness, term_variables))

    def trace_back(self):
        parent = self.current.get_parent()
        self.current = parent

    def __str__(self):
        return str(self.current)
