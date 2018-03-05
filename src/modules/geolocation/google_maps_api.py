import googlemaps


class GoogleMapsApi:
    def __init__(self, client_id):
        self.gmaps = googlemaps.Client(key=client_id)

    def get_distance(self, x: str, y: str):
        result = self.gmaps.distance_matrix(x, y, mode="walking")

        if result['rows'][0]['elements'][0]['status'] == 'NOT_FOUND':
            raise ValueError(
                'The addresses must be wrong because no distance was found.')

        distance = result['rows'][0]['elements'][0]['distance']['value']
        return distance
