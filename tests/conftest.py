import csv

import pytest

from src.arg_parsing import parsing_arguments
from src.constants import FIELD_NAMES_INPUT_FILE

STUDENTS = [
    ('Елена', 'Английский язык', 'Ковалева Анна', '2023-10-10', '5'),
    ('Владислав', 'География', 'Орлов Сергей', '2023-10-12', '4'),
    ('Елена', 'Математика', 'Смирнова Татьяна', '2023-10-11', '4'),
    ('Мария', 'Химия', 'Иванов Олег', '2023-10-16', '3'),
]


@pytest.fixture()
def first_file(tmp_path):
    """Фикстура для создания первого тестового файла с данными."""
    file_path = tmp_path / "testfile1.csv"
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(FIELD_NAMES_INPUT_FILE)
        writer.writerow(STUDENTS[0])
        writer.writerow(STUDENTS[1])
    return file_path


@pytest.fixture()
def second_file(tmp_path):
    """Фикстура для создания второго тестового файла с данными."""
    file_path = tmp_path / "testfile2.csv"
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(FIELD_NAMES_INPUT_FILE)
        writer.writerow(STUDENTS[2])
        writer.writerow(STUDENTS[3])
    return file_path


@pytest.fixture()
def student_data():
    """Фикстура для создания списка словарей с информацией о студентах."""
    return [dict(zip(FIELD_NAMES_INPUT_FILE, student)) for student in STUDENTS]


@pytest.fixture
def parser():
    """Фикстура для возврата парсера."""
    return parsing_arguments()
