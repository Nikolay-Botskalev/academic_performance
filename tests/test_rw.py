import pytest

from src.data_rw import read_file, terminal_output
from src.constants import FIELD_NAMES_AVG_PERFORMANCE
from .conftest import STUDENTS


def test_read_file(first_file):
    """Тестирование функции чтения данных из файла."""
    data = read_file(first_file)
    assert len(data) == 2, "Неполный набор данных"
    assert tuple(data[0].values()) == STUDENTS[0], "Неверные данные"
    assert tuple(data[1].values()) == STUDENTS[1], "Неверные данные"


def test_read_nonexistent_file():
    """Тест для проверки попытки чтения несуществующего файла."""
    with pytest.raises(FileNotFoundError):
        _ = read_file('nonexistent.csv')


def test_terminal_output(capsys):
    """Тестирование вывода данных в консоль."""
    test_data = [('Елена', 4.5), ('Владислав', 4.0), ('Мария', 3.0)]
    field_names = FIELD_NAMES_AVG_PERFORMANCE
    terminal_output(test_data, field_names)
    captured = capsys.readouterr()
    output = captured.out
    for data in [x for line in test_data for x in line]:
        assert str(data) in output, "Неполные данные в выводе"
