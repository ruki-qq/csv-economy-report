from collections import defaultdict
from typing import Any

from core import BaseReport, convert_to_number, is_numeric, log


class AverageGDPReport(BaseReport):
    """Report for average GDP by country."""

    @log
    def generate(self, data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """
        Generating report with average GDP by country.

        Args:
            data: Combined list of dictionaries from all CSV files.

        Returns:
            List of dictionaries with country and average_gdp,
            sorted by average_gdp desc.
        """
        country_gdps = defaultdict(list)

        for row in data:
            if "country" not in row or "gdp" not in row:
                continue

            country = row["country"].strip()
            gdp_str = row["gdp"].strip()

            if is_numeric(gdp_str):
                gdp = convert_to_number(gdp_str)
                country_gdps[country].append(gdp)
            else:
                continue

        report_data = []
        for country, gdps in country_gdps.items():
            if gdps:
                avg_gdp = sum(gdps) / len(gdps)
                report_data.append(
                    {
                        "country": country,
                        "average_gdp": round(avg_gdp, 2),
                    }
                )

        report_data.sort(key=lambda x: x["average_gdp"], reverse=True)

        return report_data
