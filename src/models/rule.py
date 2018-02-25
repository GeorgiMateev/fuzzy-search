from typing import List, Dict

from src.models.term import Term


class Rule(tuple):
    def __new__(cls, *args):
        return super(Rule, cls).__new__(cls, args)

    def get_head(self) -> Term:
        return self[0]

    def get_body(self) -> List[Term]:
        return self[1]

    def get_variables(self) -> Dict:
        variables = self.get_head().get_variables()

        for term in self.get_body():
            term_variables = term.get_variables()

            for t_var, t_var_value in term_variables.items():
                variables[t_var] = t_var_value

        return variables

    def __str__(self):
        format_str = ''.join(['{}' if i == len(self.get_body()) - 1 else '{}, '
                              for i in range(len(self.get_body()))]) + '.'
        formatted = format_str.format(*self.get_body())

        return str(self.get_head()) + ':-' + formatted

