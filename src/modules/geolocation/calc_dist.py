from src.models.self_solvable_term import SelfSolvableTerm
from src.modules.geolocation.google_maps_api import GoogleMapsApi


class CalculateDistance(SelfSolvableTerm):
    distances = {}
    api = None

    def __init__(self, *args):
        new_args = list(('calculateDistance', *args))
        super(CalculateDistance, self).__init__(*new_args)
        self.is_self_solvable = True

    def get_new_term(self, params):
        return CalculateDistance(*params[1:])

    def self_solve(self):
        source = self.get_param(0)
        dest = self.get_param(1)
        result = self.get_param(2)

        if source + dest in CalculateDistance.distances:
            return CalculateDistance.distances[source + dest]

        result_val = CalculateDistance.api.get_distance(source, dest)

        CalculateDistance.distances[source + dest] = result_val

        return 1, {result: result_val}

    @staticmethod
    def create_api(key: str):
        CalculateDistance.api = GoogleMapsApi(key)
