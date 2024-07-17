from weather.nominatim.api import get_geolocation_data

def get_coordinates_from_zipcode(zipcode: int):
    raw_data = get_geolocation_data()
    #TODO: Return only long, lat pair
    return raw_data



