def tuple_country(obj):
    """
    This function takes an object as input and constructs a tuple containing the country's common name, capital, location,
    currencies, and area.
    Returns: Tuples 
    """
    each_country = ()
    coin = ""
    each_country += (obj['name']['common'],)
    each_country += (obj['capital'][0],)
    each_country += (obj['maps']['googleMaps'],)
    for key, value in obj['currencies'].items():
        coin += value['name']
        coin += " "
    each_country += (coin,)
    each_country += (obj['area'],)
    return each_country        


def info_list_country(obj_country):
    """
    A function that generates a list of tuples from a given country object.
    
    Parameters:
    obj_country (object): The country object to convert
    into a list of tuples.
    
    Returns:
    list: A list of tuples representing the country object.
    """
    list_tuple_country = list(map(tuple_country, obj_country))
    return list_tuple_country
