from src.engine_classes import HHEngine, SJEngine
from src.utils import get_top_vacancies, sort_vacancies, get_hh_vacancies, get_sj_vacancies
from src.json_worker import JSONWorker

if __name__ == '__main__':
    hh_engine = HHEngine()
    sj_engine = SJEngine()

    user_word = input(f'Введите ключевое слово для поиска по вакансиям:\n').lower()

    """Creation of JSON files with raw vacancies data"""
    hh_vacancies = hh_engine.get_vacancies(user_word)
    sj_vacancies = sj_engine.get_vacancies(user_word)

    hh_json_worker = JSONWorker('hh.json')
    sj_json_worker = JSONWorker('sj.json')

    for vacancy_data in hh_vacancies:
        hh_json_worker.insert(vacancy_data)

    for vacancy_data in sj_vacancies:
        sj_json_worker.insert(vacancy_data)

    """Making a list of HH and SJ vacancies separately"""
    hh_instances = get_hh_vacancies(hh_json_worker)
    sj_instances = get_sj_vacancies(sj_json_worker)

    """Making unified list of HH and SJ vacancies"""
    all_instances = hh_instances + sj_instances

    while True:
        user_answer_mix = input(f'Если хотите посмотреть вакансии из HH, нажмите "1":\n'
                                f'Если хотите посмотреть вакансии из SJ, нажмите "2":\n'
                                f'Если хотите посмотреть вакансии из HH и SJ, нажмите "3":\n')

        if user_answer_mix.isdigit():
            if int(user_answer_mix) == 1:
                sorted_vacancies = sort_vacancies(hh_instances)
            elif int(user_answer_mix) == 2:
                sorted_vacancies = sort_vacancies(sj_instances)
            elif int(user_answer_mix) == 3:
                sorted_vacancies = sort_vacancies(all_instances)
            else:
                print('Ошибка ввода, значение должно быть 1, 2 или 3')
                continue
        else:
            print('Ошибка ввода, значение должно быть 1, 2 или 3')
            continue

        user_answer_top = input(f'Если хотите посмотреть топ выбранных вакансий по зарплате, нажмите "1":\n'
                                f'Если хотите посмотреть вакансии целиком, нажмите "2":\n')

        if user_answer_top.isdigit():
            if int(user_answer_top) == 1:
                """Making top vacancies list by salary"""
                count = int(input('Введите желаемое число топ вакансий\n'))
                sorted_vacancies = get_top_vacancies(sorted_vacancies, count)
            elif int(user_answer_mix) == 2:
                continue
            else:
                print('Ошибка ввода, значение должно быть 1 или 2 ')
                continue
        else:
            print('Ошибка ввода, значение должно быть 1 или 2')
            continue

        user_answer_delete = input(f'Если хотите удалить вакансию по критерию, нажмите "1":\n'
                                   f'Если нет, нажмите "2":\n')

        if user_answer_delete.isdigit():
            if int(user_answer_delete) == 1:
                """Removing a vacancy from the list by user's parameters"""
                removing_key = input('Введите ключ для удаления\n')
                removing_value = input('Введите значение для удаления\n')
                print('Удаленная вакансия:')
                print(hh_json_worker.delete({removing_key: removing_value}))
            elif int(user_answer_mix) == 2:
                continue
            else:
                print('Ошибка ввода, значение должно быть 1 или 2 ')
                continue
        else:
            print('Ошибка ввода, значение должно быть 1 или 2')
            continue

        print('Список ваших вакансий:')
        for vacancy in sorted_vacancies:
            print(vacancy)
        break
