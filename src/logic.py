from collections import defaultdict

from data_rw import read_file


def data_generation(files: list) -> list:
    """Функция для объединения данных всех файлов в 1 список."""
    full_data = []
    for file in files:
        full_data.extend(read_file(file))
    return full_data


def sorted_avg_performance(data: list[dict]) -> list[tuple]:
    """Функция для вычисления средней оценки студента и сортировки."""
    sudent_grades = defaultdict(list)
    for student in data:
        sudent_grades[student['student_name']].append(int(student['grade']))
    avg_score = dict()
    for key, values in sudent_grades.items():
        avg_score[key] = round(sum(values) / len(values), 2)
    return sorted(avg_score.items(), key=lambda x: x[-1], reverse=True)
