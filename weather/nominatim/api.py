from weather.singleton import Singleton
from geopy.geocoders import Nominatim


_USER_AGENT = 'weather-tool'

#TODO: Assess if this package is needed?
class NominatimClient(Nominatim, metaclass=Singleton):
    def __new__(cls) -> Nominatim:
        return Nominatim(user_agent=_USER_AGENT)


def get_nominatim_client() -> NominatimClient:

    return NominatimClient(_USER_AGENT)



def get_geolocation_data(location):
    """Get the geoloction data for a given location"""
    app = get_nominatim_client()
    return app.geocode(location)