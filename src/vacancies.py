class Vacancy:

    def __init__(self, pk, name, url, salary):
        self._pk = pk
        self._name = name
        self._url = url
        self._salary = salary

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()

        if other._salary is None:
            return False

        if self._salary is None:
            return True

        return self._salary < other._salary

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()

        if other._salary is None:
            return True

        if self._salary is None:
            return False

        return self._salary > other._salary

    def __str__(self):
        return f'(id вакансии: {self._pk}\
        название вакансии: {self._name}\
        URL вакансии: {self._url}\
        зарплата: {self._salary})'


if __name__ == '__main__':

    a = Vacancy(100, 'PD', '323254', 1000)
    b = Vacancy(145, 'PHD', '32345254', 1800)
    c = Vacancy(21100, 'JD', '35713254', 1500)
    my_list = [a, b, c]
    sorted_list = sorted(my_list, reverse=True)
    for item in sorted_list:
        print(item)
