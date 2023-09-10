import os

import requests
import dotenv

from abc import ABC, abstractmethod

dotenv.load_dotenv()


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
            'X-Api-App-Id': os.environ.get('SJ_token')
        }

        params = {
            'keyword': keyword,
        }

        response = requests.get(self.url, params=params, headers=headers)
        return response.json()['objects']
