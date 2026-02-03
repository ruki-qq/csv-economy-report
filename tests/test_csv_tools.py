from csv import Error as csv_Error

from pytest import raises as pt_raises

from core import CsvReader


class TestCsvReader:
    """Tests for CsvReader."""

    def test_check_csv_file_valid(self, valid_csv_file):
        """Test validation of a valid CSV file."""

        reader = CsvReader(valid_csv_file)
        result = reader.check_csv_file_valid

        assert "is valid" in result
        assert "7 rows" in result

    def test_check_csv_file_not_found(self, nonexistent_file):
        """Test that non-existent file raises FileNotFoundError."""

        reader = CsvReader(nonexistent_file)

        with pt_raises(FileNotFoundError, match="does not exist"):
            _ = reader.check_csv_file_valid

    def test_check_non_csv_file(self, non_csv_file):
        """Test that non-CSV file raises ValueError."""

        reader = CsvReader(non_csv_file)

        with pt_raises(ValueError, match="is not a CSV file"):
            _ = reader.check_csv_file_valid

    def test_check_empty_csv_file(self, empty_csv_file):
        """Test that empty CSV file raises csv.Error."""

        reader = CsvReader(empty_csv_file)

        with pt_raises(csv_Error, match="is empty"):
            _ = reader.check_csv_file_valid

    def test_check_invalid_csv_structure(self, invalid_csv_file):
        """Test that CSV with inconsistent columns raises csv.Error."""

        reader = CsvReader(invalid_csv_file)

        with pt_raises(csv_Error, match="More or less columns"):
            _ = reader.check_csv_file_valid

    def test_check_empty_value_in_row(self, empty_value_csv_file):
        """Test that empty value in CSV file row raises csv.Error."""

        reader = CsvReader(empty_value_csv_file)

        with pt_raises(csv_Error, match="Empty value in row"):
            _ = reader.check_csv_file_valid

    def test_load_csv_returns_list_of_dicts(self, valid_csv_file):
        reader = CsvReader(valid_csv_file)
        data = reader.load_csv

        assert isinstance(data, list)
        assert len(data) == 7
        assert all(isinstance(row, dict) for row in data)

    def test_load_csv_correct_data(self, valid_csv_file):
        reader = CsvReader(valid_csv_file)
        data = reader.load_csv

        assert data[0]["country"] == "United States"
        assert data[0]["year"] == "2021"
        assert data[0]["gdp"] == "22994"
        assert data[0]["gdp_growth"] == "2.4"
        assert data[0]["inflation"] == "3.2"
        assert data[0]["unemployment"] == "11.8"
        assert data[0]["population"] == "48"
        assert data[0]["continent"] == "North America"
        assert data[1]["country"] == "United States"
        assert data[1]["year"] == "2022"
        assert data[1]["gdp"] == "23315"
        assert data[1]["gdp_growth"] == "5.5"
        assert data[1]["inflation"] == "8.4"
        assert data[1]["unemployment"] == "13.0"
        assert data[1]["population"] == "48"
        assert data[1]["continent"] == "North America"

    def test_load_csv_with_custom_delimiter(self, semicolon_csv_file):
        reader = CsvReader(semicolon_csv_file, delimiter=";")
        data = reader.load_csv

        assert len(data) == 2
        assert data[0]["country"] == "United States"
        assert data[0]["year"] == "2023"

    def test_csv_reader_with_quotes(self, quotes_csv_file):
        """Test CSV reader handles quoted fields."""

        reader = CsvReader(quotes_csv_file)
        data = reader.load_csv

        assert len(data) == 1
        assert data[0]["country"] == 'United "States"'

    def test_check_csv_file_valid_called_multiple_times(self, valid_csv_file):
        reader = CsvReader(valid_csv_file)

        result1 = reader.check_csv_file_valid
        result2 = reader.check_csv_file_valid

        assert result1 == result2

    def test_load_csv_called_multiple_times(self, valid_csv_file):
        reader = CsvReader(valid_csv_file)

        data1 = reader.load_csv
        data2 = reader.load_csv

        assert data1 == data2
        assert len(data1) == 7
