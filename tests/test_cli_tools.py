from core import print_table


class TestPrintTable:
    """Tests for print_table function."""

    def test_print_table_with_valid_data(self, capsys, economic_data):
        print_table(economic_data)
        captured = capsys.readouterr()

        assert "United States" in captured.out
        assert "China" in captured.out
        assert "country" in captured.out
        assert "year" in captured.out
        assert "gdp" in captured.out
        assert "22994" in captured.out

    def test_print_table_with_title(self, capsys, economic_data):
        title = "Test Results"
        print_table(economic_data, title=title)
        captured = capsys.readouterr()

        assert title in captured.out
        assert "=" * len(title) in captured.out
        assert "United States" in captured.out

    def test_print_table_empty_data(self, capsys):
        print_table([])
        captured = capsys.readouterr()

        assert "No data to display" in captured.out

    def test_print_table_single_row(self, capsys, economic_data):
        data = economic_data[:1]
        print_table(data)
        captured = capsys.readouterr()

        assert "North America" in captured.out
        assert "22994" in captured.out

    def test_print_table_grid_format(self, capsys, economic_data):
        """Test that table uses grid format."""

        print_table(economic_data)
        captured = capsys.readouterr()

        assert "+" in captured.out
        assert "|" in captured.out
