from datetime import date
from exceptions import NegativeTitlesError
from exceptions import InvalidYearCupError
from exceptions import ImpossibleTitlesError


def data_processing(self):
    year_now = date.today().year
    cups_data = []
    var_first_cup = self["first_cup"]
    var_titles = self["titles"]
    total_titles = int((year_now - int(var_first_cup[:4])) / 4)

    for cups in range(1930, year_now, 4):
        cups_data.append(cups)

    if var_titles < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if int(var_first_cup[:4]) not in cups_data:
        raise InvalidYearCupError("there was no world cup this year")

    if var_titles > total_titles:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
