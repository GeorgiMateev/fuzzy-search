from typing import List, Dict


class Term(list):
    def __init__(self, *args):
        super(Term, self).__init__(list(args))

        self.is_self_solvable = False

    def get_functor(self):
        return self[0]

    def get_arity(self):
        return len(self) - 1

    def get_params(self):
        return self[1:]

    def get_param(self, index: int):
        return self.get_params()[index]

    def get_new_term(self, params):
        return Term(*params)

    def assign_variables(self, variables):
        new_params = Term.__assign_variables(self, variables)
        return self.get_new_term(new_params)

    def get_variables(self) -> Dict:
        return Term.__get_variables(self)

    @staticmethod
    def __get_variables(params) -> Dict:
        variables = {}
        for param in params:
            if isinstance(param, str) and param[0].isupper():
                variables[param] = param
            elif isinstance(param, List):
                param_variables = Term.__get_variables(param)
                for t_var, t_var_value in param_variables.items():
                    variables[t_var] = t_var_value

        return variables

    @staticmethod
    def __assign_variables(term_params: List, variables: List) -> List:
        transformed = []
        for param in term_params:
            if isinstance(param, List):
                transformed_list = Term.__assign_variables(param, variables)
                transformed.append(transformed_list)
            elif param in variables:
                transformed.append(variables[param])
            else:
                transformed.append(param)
        return transformed
