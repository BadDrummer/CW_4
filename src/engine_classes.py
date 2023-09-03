import requests

from abc import ABC, abstractmethod
SJ_token = 'v3.r.137783818.e3545af96c738f8122b6ee5746a30d3c81d0b2a6.6eb35ada079989ab14c658d5f099b682f137ed92'


class BaseEngine(ABC):
    """Base abstract class"""
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHEngine(BaseEngine):
    """Class which gets information of vacancies from HeadHunter API"""
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        params = {
            'text': keyword
        }
        response = requests.get(self.url, params=params)
        response_data = response.json()['items']
        return response_data


class SJEngine(BaseEngine):
    """Class which gets information of vacancies from SuperJob API"""
    def __init__(self):
        self.url = 'https://api.superjob.ru/2.0/vacancies'

    def get_vacancies(self, keyword):
        headers = {
            'X-Api-App-Id': SJ_token
        }

        params = {
            'keyword': keyword,
        }

        response = requests.get(self.url, params=params, headers=headers)
        return response.json()['objects']
