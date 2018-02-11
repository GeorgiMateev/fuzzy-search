from typing import List


class Term(List):
    def __init__(self):
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
