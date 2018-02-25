from typing import List, Tuple, Dict, Generator

from src.models.rule import Rule
from src.models.term import Term
from src.unifier import Unifier


class Reasoner:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def query(self, term: Term) -> Generator[Tuple[List, Dict]]:
        """
        Query the knowledge base with the given term.
        :param term: A query term.
        :return: Generates solutions - each with truthfulness and unified variables.
        """
        for truthfulness, variables in self.solve(term):
            yield truthfulness, variables

    def complex_query(self, query: List[Term]) -> Generator[Tuple[List, Dict]]:
        """
        Query the database with complex query - several terms in AND logical ralation.
        :param query: List of terms in AND relation.
        :return: Generates solutions - each with truthfulness and unified variables.
        """
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
                unified, query_variables_map, head_variables_map = Unifier.try_unify(query_term, rule.get_head())
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

