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
