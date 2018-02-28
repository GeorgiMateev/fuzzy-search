from typing import Dict


class Solution:
    def __init__(self, truthfulness: float, variables: Dict):
        self.truthfulness = truthfulness
        self.variables = variables

    def __str__(self):
        format_str = ''

        for var_name, var_value in self.variables.items():
            if var_name != var_value:
                format_str += ' {}={}'.format(var_name, var_value)
        return ('Truth:{}' + format_str).format(self.truthfulness)
