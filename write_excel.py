from typing import List, Tuple
import openpyxl


def save_to_excel(countries: List[Tuple[str, str, str, float]]):
    """
    A function that saves a list of tuples to an Excel file.
    """

    # wb is a instance of Workbook
    wb = openpyxl.Workbook()
    # create sheet
    sheet = wb.active
    # create field names
    #if sheet.cell(row=1, column=1).value != 'Country':
    sheet.append(['Country', 'Capital', 'Location',
                      'currencies', 'population'])
    # add data
    for country in countries:
        sheet.append(country)
    path = 'excels/data_country.xlsx'
    wb.save(path)
