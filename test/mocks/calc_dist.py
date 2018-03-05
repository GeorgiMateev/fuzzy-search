from src.models.self_solvable_term import SelfSolvableTerm


class CalculateDistance(SelfSolvableTerm):
    def __init__(self, *args):
        new_args = list(('calculateDistance', *args))
        super(CalculateDistance, self).__init__(*new_args)
        self.is_self_solvable = True

    def get_new_term(self, params):
        return CalculateDistance(*params[1:])

    def self_solve(self):
        # TODO: Calculate based on real map.
        source = self.get_param(0)
        dest = self.get_param(1)
        result = self.get_param(2)

        if dest == 'st_nedelia' and source == 'sheraton':
            return 1, {result: 290}

        if source == 'sheraton' and dest == 'nevski':
            return 1, {result: 1000}

        return 1, {result, 500}
