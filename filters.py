import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
from api import Api

api = Api()

# Row 1 | Col 1
def data_slider():
    pass

def list_all_statuses():

    list_status = [
        {"label": "Todos ", "value": "all"},
        {"label": "Novos Confirmados ", "value": "NewConfirmed"},
        {"label": "Total Confirmados ", "value": "TotalConfirmed"},
        {"label": "Novas baixas ", "value": "NewDeaths"},
        {"label": "Total baixas ", "value": "TotalDeaths"},
        {"label": "Novos recuperados ", "value": "NewRecovered"},
        {"label": "Total recuperados ", "value": "TotalRecovered"},
    ]

    return list_status

def get_all_countries():

    response = api.getCountries()
    df = json_normalize(response)

    list_countries = []
    for country in df.values:
        data = {
            country[1]: country[0]
        }
        list_countries.append(data)

    return list_countries


# Row 1 | Col 2 | Sub-Row 1
def header_status():
    response = api.getSumary()
    df = json_normalize(response)

    list_status = []
    for key in df.keys()[2:]:
        name = key.split(".")
        data = {
            name[1]: df[key].values
        }
        list_status.append(data)

    return list_status
# Row 1 | Col 2 | Sub-Row 2
def total_time():
    response = api.getSumary()
    df = json_normalize(response)

    total = df['Global.TotalConfirmed']
    # range_date = ['', df['']]

    return total.key, total.value

# Row 2 | Col 1
def graph_satellite():
    pass
# Row 2 | Col 2
def scatter_unit():
    pass

# Row 3 | Co11
def rosca_chart():
    pass
# Row 3 | Col2

def global_scatter():
    pass


# Utils




if __name__ == "__main__":
    get_all_countries()

