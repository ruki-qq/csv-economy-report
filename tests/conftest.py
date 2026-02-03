import csv
import tempfile
from pathlib import Path
from typing import Iterator

import pytest


@pytest.fixture
def economic_data() -> list[dict[str, str]]:
    """Valid sample data for AverageGDPReport testing."""

    return [
        {
            "country": "United States",
            "year": "2021",
            "gdp": "22994",
            "gdp_growth": "2.4",
            "inflation": "3.2",
            "unemployment": "11.8",
            "population": "48",
            "continent": "North America",
        },
        {
            "country": "United States",
            "year": "2022",
            "gdp": "23315",
            "gdp_growth": "5.5",
            "inflation": "8.4",
            "unemployment": "13.0",
            "population": "48",
            "continent": "North America",
        },
        {
            "country": "United States",
            "year": "2023",
            "gdp": "25462",
            "gdp_growth": "6.4",
            "inflation": "3.0",
            "unemployment": "14.8",
            "population": "47",
            "continent": "North America",
        },
        {
            "country": "China",
            "year": "2021",
            "gdp": "17734",
            "gdp_growth": "2.4",
            "inflation": "3.2",
            "unemployment": "11.8",
            "population": "48",
            "continent": "Asia",
        },
        {
            "country": "China",
            "year": "2022",
            "gdp": "17734",
            "gdp_growth": "5.5",
            "inflation": "8.4",
            "unemployment": "13.0",
            "population": "48",
            "continent": "Asia",
        },
        {
            "country": "China",
            "year": "2023",
            "gdp": "17963",
            "gdp_growth": "6.4",
            "inflation": "3.0",
            "unemployment": "14.8",
            "population": "47",
            "continent": "Asia",
        },
        {
            "country": "Germany",
            "year": "2021",
            "gdp": "4257",
            "gdp_growth": "2.4",
            "inflation": "3.2",
            "unemployment": "11.8",
            "population": "48",
            "continent": "Europe",
        },
    ]


@pytest.fixture
def economic_data_with_invalid() -> list[dict[str, str]]:
    """Data with some invalid and missing values."""

    return [
        {"country": "United States", "gdp": "25462"},
        {"country": "InvalidCountry", "gdp": "not_a_number"},
        {"country": "MissingGDP", "year": "2023"},
        {"country": "United States", "gdp": "20000"},
    ]


@pytest.fixture
def economic_data_rounding() -> list[dict[str, str]]:
    """Data to test rounding to 2 decimal places."""

    return [
        {"country": "TestCountry", "gdp": "10000"},
        {"country": "TestCountry", "gdp": "10001"},
    ]


@pytest.fixture
def valid_csv_file(economic_data: list[dict[str, str]]) -> Iterator[Path]:
    """Creating a temporary CSV file for testing csv_tools."""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "country",
                "year",
                "gdp",
                "gdp_growth",
                "inflation",
                "unemployment",
                "population",
                "continent",
            ],
        )
        writer.writeheader()
        writer.writerows(economic_data)
        temp_path = Path(f.name)

    yield temp_path

    temp_path.unlink()


@pytest.fixture
def invalid_csv_file() -> Iterator[Path]:
    """Creating a temporary invalid CSV file for testing csv_tools."""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("invalid,csv,content\nwith no proper structure")
        temp_path = Path(f.name)

    yield temp_path

    temp_path.unlink()


@pytest.fixture
def empty_csv_file() -> Iterator[Path]:
    """Creating a temporary empty CSV file for testing csv_tools."""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("empty,csv,file")
        temp_path = Path(f.name)

    yield temp_path

    temp_path.unlink()


@pytest.fixture
def empty_value_csv_file() -> Iterator[Path]:
    """Creating a temporary CSV file with empty value in row for testing csv_tools."""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(
            "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        )
        f.write("United States,2023,25462,2.1,3.4,3.7,339,\n")
        temp_path = Path(f.name)

    yield temp_path

    temp_path.unlink()


@pytest.fixture
def non_csv_file() -> Iterator[Path]:
    """Creating a temporary non-CSV file for testing csv_tools."""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("This is not a CSV file")
        temp_path = Path(f.name)

    yield temp_path

    temp_path.unlink()


@pytest.fixture
def nonexistent_file() -> Path:
    """Path to a non-existent file."""
    return Path("nonexistent_file.csv")


@pytest.fixture
def semicolon_csv_file() -> Iterator[Path]:
    """Creating a temporary semicolon CSV file for testing csv_tools."""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(
            "country;year;gdp;gdp_growth;inflation;unemployment;population;continent\n"
        )
        f.write("United States;2023;25462;2.1;3.4;3.7;339;North America\n")
        f.write("China;2022;17734;5.5;8.4;13.0;48;Asia\n")
        temp_path = Path(f.name)

    yield temp_path

    temp_path.unlink()


@pytest.fixture
def quotes_csv_file() -> Iterator[Path]:
    """Creating a temporary CSV file with quotes for testing csv_tools."""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write(
            "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        )
        f.write('United "States",2023,25462,2.1,3.4,3.7,339,North America\n')
        temp_path = Path(f.name)

    yield temp_path
    temp_path.unlink()


@pytest.fixture
def valid_args() -> list[str]:
    """Valid arguments for testing arg_parser."""

    return ["--files", "file.csv", "--report", "average-gdp"]


@pytest.fixture
def valid_multiple_files_args() -> list[str]:
    """Valid multi-files arguments for testing arg_parser."""

    return ["--files", "file1.csv", "file2.csv", "file3.csv", "--report", "average-gdp"]


@pytest.fixture
def no_files_args() -> list[str]:
    """Invalid arguments without --files for testing arg_parser."""

    return ["--report", "average-gdp"]


@pytest.fixture
def no_report_args() -> list[str]:
    """Invalid arguments without --report for testing arg_parser."""

    return ["--files", "file.csv"]


@pytest.fixture
def abbreviated_args() -> list[str]:
    """Abbreviated arguments for testing arg_parser."""

    return ["--f", "file.csv", "--report", "average-gdp"]


@pytest.fixture
def duplicate_args() -> list[str]:
    """Duplicate arguments for testing arg_parser."""

    return ["--files", "file1.csv", "--files", "file2.csv", "--report", "average-gdp"]


@pytest.fixture
def help_arg() -> list[str]:
    """Help argument for testing arg_parser."""

    return ["--help"]


@pytest.fixture
def unknown_args() -> list[str]:
    """Unknown arguments for testing arg_parser."""

    return ["--files", "file.csv", "--report", "average-gdp", "--unknown", "value"]


@pytest.fixture
def zero_files_args() -> list[str]:
    """Zero-files arguments for testing arg_parser."""

    return ["--files", "--report", "average-gdp"]
