from write_excel import save_to_excel
import requests
from typing import List, Tuple
from organize_info_api.organize_info import info_list_country


def get_countries() -> List[Tuple[str, str, str, float]]:

    try:
        response = requests.get('https://restcountries.com/v3.1/lang/spanish')
        if response.status_code == 200:
            obj_country = response.json()
            list_countries = info_list_country(obj_country)

    except:
        raise Exception('Error to get data from API')

    return list_countries


if __name__ == '__main__':

    list_countries = get_countries()
    save_to_excel(list_countries)
