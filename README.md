# csv-dev-report

This project is for generating reports from CSV files.
It's currently supports average-gdp report, though new reports can be added by creating BaseReport child class and register it in ReportRegistry with ReportRegistry.register_report.

## Usage

```bash
poetry install
poetry shell
python main.py --files <paths_to_csv_files> --report <report_name>
```

## Examples

```bash
python main.py --files csv/economic1.csv csv/economic2.csv --report average-gdp
```

## Testing

```bash
python -m pytest
```

## Screenshots

### Basic usage
![alt](https://files.catbox.moe/kqdi7w.png)


### Some error handling
![alt](https://files.catbox.moe/4uanvm.png)


### Tests & flake8
![alt](https://files.catbox.moe/ueva1d.png)


### Logs
![alt](https://files.catbox.moe/8kvv51.png)
