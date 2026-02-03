from pytest import raises as pt_raises

from core import ReportRegistry
from core.defined_reports import AverageGDPReport


class TestReportRegistry:
    """Tests for ReportRegistry."""

    def test_register_report(self):
        ReportRegistry.register_report("test_report", AverageGDPReport)

        assert "test_report" in ReportRegistry.available_reports

    def test_get_registered_report(self):
        ReportRegistry.register_report("average-gdp", AverageGDPReport)
        report = ReportRegistry.get_report("average-gdp")

        assert isinstance(report, AverageGDPReport)

    def test_get_nonexistent_report_raises_error(self):
        """Test that getting non-existent report raises ValueError."""

        with pt_raises(ValueError, match="isn't found"):
            ReportRegistry.get_report("nonexistent_report")


class TestAverageGDPReport:
    """Tests for AverageGDPReport class."""

    def test_generate_report_valid_data(self, economic_data):
        report = AverageGDPReport()
        result = report.generate(economic_data)

        assert len(result) == 3
        assert result[0] == {"country": "United States", "average_gdp": 23923.67}
        assert result[1] == {"country": "China", "average_gdp": 17810.33}
        assert result[2] == {"country": "Germany", "average_gdp": 4257.0}

    def test_generate_report_invalid_data_skipped(self, economic_data_with_invalid):
        report = AverageGDPReport()
        result = report.generate(economic_data_with_invalid)

        assert len(result) == 1
        assert result[0] == {"country": "United States", "average_gdp": 22731.0}

    def test_generate_report_rounding(self, economic_data_rounding):
        report = AverageGDPReport()
        result = report.generate(economic_data_rounding)

        assert len(result) == 1
        assert result[0]["average_gdp"] == 10000.5

    def test_generate_report_empty_data(self):
        report = AverageGDPReport()
        result = report.generate([])

        assert result == []

    def test_registry_average_gdp(self):
        ReportRegistry.register_report("average-gdp", AverageGDPReport)
        report = ReportRegistry.get_report("average-gdp")

        assert isinstance(report, AverageGDPReport)
