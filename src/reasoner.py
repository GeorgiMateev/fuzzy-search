from typing import List, Tuple, Dict

from src.models.rule import Rule
from src.models.term import Term


class Reasoner:
    def __init__(self, knowledge_base: List[Rule[Term, List[Term]]]):
        self.knowledge_base = knowledge_base

    def query(self, term: Term):
        for truthfulness, variables in self.solve(term):
            yield truthfulness, variables

    def query(self, query: List[Term]):
        results = map(lambda term: self.solve(term), query)
        self.mamdani(results)

    def solve(self, query_term: Term):
        if query_term.is_self_solvable:
            truthfulness, variables = query_term.self_solve()
            yield [truthfulness], variables

        for rule in self.knowledge_base:
            rule_variables = rule.get_variables()
            unified, query_variables_map = self.try_unify(query_term, rule.get_head())
            if unified:
                for body_truthfulness, solved_variables in self.solve_rule_body(rule.get_body(), rule_variables):
                    updated_query_variables = self.update_variables(query_variables_map, solved_variables)
                    yield self.mamdani(body_truthfulness), updated_query_variables

    def solve_rule_body(self, rule_body: List[Term], rule_variables: List):
        transformed_term = rule_body[0].assign_variables(rule_variables)
        for truthfulness, variables in self.solve(transformed_term):
            updated_rule_variables = self.update_variables(rule_variables, variables)
            for terms_truthfulness, solved_variables in self.solve_rule_body(rule_body[1:], updated_rule_variables):
                yield [truthfulness].append(terms_truthfulness), solved_variables

    def mamdani(self, truths: List):
        return min(truths)

    def try_unify(self, query_term: List, term: List) -> (bool, Dict):
        if len(query_term) == len(term.get_arity()):
            unified_variables = {}
            for i in range(len(query_term)):
                query_param = query_term[i]
                term_param = term[i]
                unified, param_variables = self.try_unify_param(query_param, term_param)
                if unified:
                    # Merge unified variables
                    unified_variables = {**unified_variables, **param_variables}
                else:
                    return False
            return True, unified_variables
        else:
            return False

    def try_unify_param(self, query_param, term_param) -> (bool, Dict):
        if isinstance(query_param, str):
            if query_param[0].isupper():
                return True, {query_param: term_param}
            elif query_param == '_':
                return True
            else:
                return query_param == term_param

        if isinstance(query_param, float) or isinstance(query_param, int):
            return query_param == term_param

        if isinstance(query_param, List) and isinstance(term_param, List):
            return self.try_unify(query_param, term_param)
        else:
            return False

    def update_variables(self, query_variables: Dict, solved_variables: Dict):
        updated_variables = {}
        for q_variable, q_value in query_variables.items():
            if q_value in solved_variables:
                updated_variables[q_variable] = solved_variables[q_value]
            else:
                updated_variables[q_variable] = query_variables[q_variable]
        return updated_variables


