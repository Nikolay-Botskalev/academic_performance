import argparse


def parsing_arguments() -> argparse.ArgumentParser:
    """Функция для установки аргументов для парсинга командной строки."""
    parser = argparse.ArgumentParser(description='Анализ успеваемости.')
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Имя файла',
    )
    parser.add_argument(
        '--report',
        nargs='?',
        const='student-performance',
        default='student-performance',
        help='Название отчета',
    )
    return parser
