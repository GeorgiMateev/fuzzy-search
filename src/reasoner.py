from typing import List, Tuple, Dict

from src.models.rule import Rule
from src.models.term import Term


class Reasoner:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def query(self, term: Term):
        for truthfulness, variables in self.solve(term):
            yield truthfulness, variables

    def complex_query(self, query: List[Term]):
        rule = Rule(Term(), query)
        variables = rule.get_variables()
        result = self.solve_rule_body(rule.get_body(), variables)
        for truthfulness, solved_vars in result:
            yield [self.mamdani(truthfulness)], solved_vars

    def solve(self, query_term: Term):
        if query_term.is_self_solvable:
            truthfulness, variables = query_term.self_solve()
            yield [truthfulness], variables
        else:
            for rule in self.knowledge_base:
                rule_variables = rule.get_variables()
                unified, query_variables_map, head_variables_map = self.try_unify(query_term, rule.get_head())
                if unified:
                    updated_rule_variables = self.update_variables(rule_variables, head_variables_map)
                    for body_truthfulness, solved_variables in self.solve_rule_body(rule.get_body(), updated_rule_variables):
                        updated_query_variables = self.update_variables(query_variables_map, solved_variables)
                        yield [self.mamdani(body_truthfulness)], updated_query_variables

    def solve_rule_body(self, rule_body: List[Term], rule_variables: Dict) -> (List, Dict):
        if len(rule_body) == 0:
            yield [1], {}
        else:
            transformed_term = rule_body[0].assign_variables(rule_variables)
            for truthfulness, variables in self.solve(transformed_term):
                updated_rule_variables = self.update_variables(rule_variables, variables)
                for terms_truthfulness, solved_variables in self.solve_rule_body(rule_body[1:], updated_rule_variables):
                    updated_body_variables = self.update_variables(updated_rule_variables, solved_variables)
                    yield [*truthfulness, *terms_truthfulness], updated_body_variables

    def mamdani(self, truths: List):
        return min(truths)

    def try_unify(self, query_term: List, term: List) -> (bool, Dict, Dict):
        if len(query_term) == len(term):
            unified_query_variables = {}
            unified_term_variables = {}
            for i in range(len(query_term)):
                query_param = query_term[i]
                term_param = term[i]
                unified, query_variables, term_variables = self.try_unify_param(query_param, term_param)
                if unified:
                    # Merge unified variables
                    compatible_query, unified_query_variables = self.merge_variables(unified_query_variables, query_variables)
                    if not compatible_query:
                        return False, {}, {}

                    compatible_term, unified_term_variables = self.merge_variables(unified_term_variables, term_variables)
                    if not compatible_term:
                        return False, {}, {}
                else:
                    return False, {}, {}
            return True, unified_query_variables, unified_term_variables
        else:
            return False, {}, {}

    def try_unify_param(self, query_param, term_param) -> (bool, Dict, Dict):
        if isinstance(query_param, str):
            if query_param[0].isupper():
                return True, {query_param: term_param}, {}
            elif query_param == '_':
                return True, {}, {}
            elif isinstance(term_param, str) and term_param[0].isupper():
                return True, {}, {term_param: query_param}
            elif term_param == '_':
                return True, {}, {}
            else:
                return query_param == term_param, {}, {}

        if isinstance(query_param, float) or isinstance(query_param, int):
            if isinstance(term_param, str) and term_param[0].isupper():
                return True, {}, {term_param: query_param}
            elif term_param == '_':
                return True, {}, {}
            else:
                return query_param == term_param, {}, {}

        if isinstance(query_param, List) and isinstance(term_param, List):
            return self.try_unify(query_param, term_param)
        elif isinstance(query_param, List) and isinstance(term_param, str) and term_param[0].isupper():
            return True, {}, {term_param, query_param}
        elif isinstance(term_param, List) and isinstance(query_param, str) and query_param[0].isupper():
            return True, {query_param: term_param}, {}
        else:
            return False, {}, {}

    def update_variables(self, query_variables: Dict, solved_variables: Dict):
        updated_variables = {}
        for q_variable, q_value in query_variables.items():
            if q_value in solved_variables:
                updated_variables[q_variable] = solved_variables[q_value]
            else:
                updated_variables[q_variable] = query_variables[q_variable]
        return updated_variables

    def merge_variables(self, all_variables: Dict, variables: Dict) -> (bool, Dict):
        new_vars = dict(all_variables)

        for variable, value in variables.items():
            if variable in new_vars and new_vars[variable] != value:
                return False, {}
            else:
                new_vars[variable] = value

        return True, new_vars
