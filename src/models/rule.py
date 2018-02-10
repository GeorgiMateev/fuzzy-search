from typing import Tuple, List

from src.models.term import Term


class Rule(Tuple):
    def get_head(self) -> Term:
        return self[0]

    def get_body(self) -> List[Term]:
        return self[1]

    def get_variables(self):
        variables = []
        variables.extend(
            self.__get_term_variables(self.get_head())
        )

        for term in self.get_body():
            variables.extend(
                self.__get_term_variables(term)
            )
        return variables

    def __get_term_variables(self, term: Term):
        return [param for param in term.get_params()
                if isinstance(param, str) and param[0].isupper()]

