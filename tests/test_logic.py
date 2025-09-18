from src.logic import data_generation, sorted_avg_performance

from .conftest import STUDENTS


def test_data_generation(first_file, second_file):
    """Тестирование функции объединения данных нескольких файлов."""
    data = data_generation([first_file, second_file])
    assert len(data) == 4, "Неверное колличество строк данных"
    for line in data:
        assert tuple(line.values()) in STUDENTS, "Неверные данные"


def test_sorted_avg_performance(student_data):
    """Тестирование функции расчета средней оценки и сортировки результата."""
    data = sorted_avg_performance(student_data)
    assert isinstance(data, (tuple, list))
    assert len(data) == 3, "Неверное количество полученных записей"
    for current, expected in zip(
        data, [('Елена', 4.5), ('Владислав', 4.0), ('Мария', 3.0)],
    ):
        assert current == expected, "Неверная оценка или порядок сортировки"
