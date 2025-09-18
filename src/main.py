from collections import namedtuple

from arg_parsing import parsing_arguments
from constants import FIELD_NAMES_AVG_PERFORMANCE
from data_rw import terminal_output
from logic import data_generation, sorted_avg_performance

Report = namedtuple('Report', ['function', 'field_names'])


REPORT_MODE = {
    'student-performance': Report(
        sorted_avg_performance, FIELD_NAMES_AVG_PERFORMANCE),
}


def main() -> None:
    """Основная функция."""
    # Парсинг принятых аргументов
    arg_parser = parsing_arguments()
    args = arg_parser.parse_args()

    # Получение полного списка учащихся со всех файлов
    try:
        full_data = data_generation(args.files)
    except FileNotFoundError as e:
        print(f"Файл {e.filename} не найден.")
        return

    # Вызов функции для создания нужного отчета
    try:
        result = REPORT_MODE[args.report].function(full_data)
    except KeyError:
        print('Неизвестный тип отчета.')
    else:
        terminal_output(result, REPORT_MODE[args.report].field_names)


if __name__ == '__main__':
    main()
