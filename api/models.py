class Country:
    """
    Representation of the country with parameters predefined by API
    """
    def __init__(self, **data_dict):
        self.__dict__.update(data_dict)


class City:
    """
    Representation of the city with parameters predefined by API
    """
    def __init__(self, **data_dict):
        self.__dict__.update(data_dict)
        self.country = Country(**data_dict['country'])
