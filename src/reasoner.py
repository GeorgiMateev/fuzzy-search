from typing import List, Dict

from src.models.rule import Rule
from src.models.term import Term
from src.tracer import Tracer
from src.unifier import Unifier


class Reasoner:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def complex_query(self, query: List[Term]):
        """
        Query the database with complex query - several terms in AND logical ralation.
        :param query: List of terms in AND relation.
        :return: Generates solutions - each with truthfulness and unified variables.
        """
        rule = Rule(Term('query'), query)
        variables = rule.get_variables()
        tracer = Tracer()
        tracer.trace_rule(rule.get_head(), {}, rule, variables)
        result = self.solve_rule_body(rule.get_body(), variables, tracer)
        for truthfulness, solved_vars in result:
            truthfulness_implication = self.mamdani(truthfulness)
            tracer.trace_solution(truthfulness_implication, solved_vars)
            yield [truthfulness_implication], solved_vars

        print(tracer)

    def solve(self, query_term: Term, tracer: Tracer):
        if query_term.is_self_solvable:
            truthfulness, variables = query_term.self_solve()
            tracer.trace_fact(query_term, truthfulness, variables)
            tracer.trace_back()
            yield [truthfulness], variables
        else:
            for rule in self.knowledge_base:
                rule_variables = rule.get_variables()
                unified, query_variables_map, head_variables_map = Unifier.try_unify(query_term, rule.get_head())
                if unified:
                    updated_rule_variables = self.update_variables(rule_variables, head_variables_map)

                    tracer.trace_rule(query_term, query_variables_map, rule, updated_rule_variables)

                    for body_truthfulness, solved_variables in self.solve_rule_body(rule.get_body(), updated_rule_variables, tracer):
                        updated_query_variables = self.update_variables(query_variables_map, solved_variables)
                        body_truthfulness_implication = self.mamdani(body_truthfulness)

                        tracer.trace_solution(body_truthfulness_implication, updated_query_variables)

                        yield [body_truthfulness_implication], updated_query_variables

                    tracer.trace_back()

    def solve_rule_body(self, rule_body: List[Term], rule_variables: Dict, tracer: Tracer) -> (List, Dict):
        if len(rule_body) == 0:
            yield [1], {}
        else:
            transformed_term = rule_body[0].assign_variables(rule_variables)
            # Here we are just updating the whole rule variables with every next term in the body
            # without checking for conflicts because we are solving from left to right:
            # each new term have less and less unsolved rule variables.
            for truthfulness, variables in self.solve(transformed_term, tracer):
                updated_rule_variables = self.update_variables(rule_variables, variables)
                for terms_truthfulness, solved_variables in self.solve_rule_body(rule_body[1:], updated_rule_variables, tracer):
                    updated_body_variables = self.update_variables(updated_rule_variables, solved_variables)
                    yield [*truthfulness, *terms_truthfulness], updated_body_variables

    def mamdani(self, truths: List):
        return min(truths)

    def update_variables(self, query_variables: Dict, solved_variables: Dict) -> Dict:
        """
        Updates the variables with the given variable values.
        :param query_variables: Variables that may not have values e.g. X=X
        :param solved_variables: Variables that have values e.g. X=5
        :return: Returns new dict with all query_variables updated or not.
        """
        updated_variables = {}
        for q_variable, q_value in query_variables.items():
            if q_value in solved_variables:
                updated_variables[q_variable] = solved_variables[q_value]
            else:
                updated_variables[q_variable] = query_variables[q_variable]
        return updated_variables

