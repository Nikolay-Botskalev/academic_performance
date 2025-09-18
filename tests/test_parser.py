import pytest


@pytest.mark.parametrize("test_input, expected_files", [
    (['--files', 'file1.csv'], ['file1.csv']),
    (['--files', 'file1.csv', 'file2.csv'], ['file1.csv', 'file2.csv']),
])
def test_parser_with_various_files(parser, test_input, expected_files):
    """Тестирование парсинга различного числа входных файлов."""
    args = parser.parse_args(test_input)
    assert args.files == expected_files


@pytest.mark.parametrize("test_input, expected_report", [
    (['--files', 'file1.csv', '--report'], 'student-performance'),
    (['--files', 'file1.csv'], 'student-performance'),
    (['--files', 'file1.csv', '--report', 'report_name'], 'report_name'),
])
def test_parser_with_various_report(parser, test_input, expected_report):
    """Тестирование парсинга отчета."""
    args = parser.parse_args(test_input)
    assert args.report == expected_report


@pytest.mark.parametrize("test_input", [
    (['--files']),
    ([]),
    ([['--files', 'file1.csv', '--report', 'report1', 'report2']]),
])
def test_parser_without_files(parser, test_input):
    """Тестирование некорректного количества параметров."""
    with pytest.raises(SystemExit):
        _ = parser.parse_args(test_input)
