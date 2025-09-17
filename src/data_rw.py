import csv

from prettytable import PrettyTable


def read_file(file_name: str) -> list:
    """Считывание данных из файла."""
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def terminal_output(
    data: list | tuple,
    field_names: list | tuple,
) -> None:
    """Вывод отчета в терминал.

    Входные данные:
    data - Список с данными, которые выводятся в терминал
    field_names - Список с заголовками для таблицы
    """
    result = PrettyTable()
    result.field_names = field_names
    result.align = 'l'
    for idx, row in enumerate(data, start=1):
        result.add_row([idx, *row])
    print(result)
