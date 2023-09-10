from src.vacancies import Vacancy


def sort_vacancies(vacancies):
    """Function for sorting vacancies by salary"""
    return list(sorted(vacancies))


def get_top_vacancies(vacancies, count):
    """Function for getting a list of chosen number of top vacancies sorted by salary"""
    return list(sorted(vacancies, reverse=True))[:count]


def get_hh_vacancies(worker):
    """Function gets a list of HH vacancies"""
    data = worker.get_all()
    vacancies = []

    for vac_data in data:
        pk = vac_data['id']
        name = vac_data['name']
        url = vac_data['alternate_url']
        if vac_data['salary']:
            salary = vac_data['salary']
        else:
            salary = None
        vacancy = Vacancy(pk, name, url, salary)
        vacancies.append(vacancy)
    return vacancies


def get_sj_vacancies(worker):
    """Function gets a list of SJ vacancies"""
    data = worker.get_all()
    vacancies = []

    for vac_data in data:
        pk = vac_data['id']
        name = vac_data['profession']
        url = vac_data['link']
        if vac_data['payment_from']:
            salary = vac_data['payment_from']
        else:
            salary = None
        vacancy = Vacancy(pk, name, url, salary)
        vacancies.append(vacancy)
    return vacancies
