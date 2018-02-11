from typing import Tuple, List, Dict

from src.models.term import Term


class Rule(tuple):
    def __new__(cls, *args):
        return super(Rule, cls).__new__(cls, args)

    def get_head(self) -> Term:
        return self[0]

    def get_body(self) -> List[Term]:
        return self[1]

    def get_variables(self) -> Dict:
        variables = self.__get_term_variables(self.get_head())

        term_variables = self.__get_term_variables(self.get_body())

        for t_var, t_var_value in term_variables.items():
            variables[t_var] = t_var_value

        return variables

    def __get_term_variables(self, term: List) -> Dict:
        variables = {}
        for param in term:
            if isinstance(param, str) and param[0].isupper():
                variables[param] = param
            elif isinstance(param, List):
                param_variables = self.__get_term_variables(param)
                for t_var, t_var_value in param_variables.items():
                    variables[t_var] = t_var_value

        return variables

