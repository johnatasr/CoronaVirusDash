import requests
import json


class Api:

    def __init__(self):
        self.url = 'https://api.covid19api.com/'

    def getSumary(self):
        response = requests.get(self.url + 'summary')
        global_response = response.json()

        return global_response

    def dayOne(self, country, status):
        response = requests.get(self.url + f'dayone/country/{country}/status/{status}')
        global_response = response.json()

        return global_response

    def dayOneAll(self, country):
        response = requests.get(self.url + f'dayone/country/{country}')
        global_response = response.json()

        return global_response


    def byCountry(self, country, status, init, end):
        #  Datetimeformat  2020-04-01T00:00:00Z
        response = requests.get(self.url + f'country/{country}/status/{status}?from={init}&to={end}')
        global_response = response.json()

        return global_response

    def getCountries(self):
        response = requests.get(self.url + 'countries')
        global_response = response.json()

        return global_response


if __name__ == "__main__":
    api = Api()
    api.getSumary()