# Environment setup

## Database Connection Setup
1. Setup SQL server and load [AdventureWorks database](../AdventureWorks2021.bak)

2. Open file ```connections.py``` and update variables values.


## Create virtual environment for tests execution
1. Run PyCharm and open terminal window.

2. Run following commands for setup required libraries.
```bash
pip install pypyodbc
pip install pytest
pip install pytest-html-reporter
```

## Deploy and configure Data Quality solution

# First launch type
1. Open in the PyCharm project M4_PyTest_DB_testing.
2. Navigate to the ```File->Settings->Project:DataBase_testing->Project Interpreter```. Check libraries. If libraries ```pypyodbc, pytest, pytest-html-report``` are not available, please add them.


# Run tests 1
In the PyCharm Terminal please run following command.
```bash
pytest tests/ --html-report=./report --title='PYTEST REPORT'
```

# Test Cases Run Result

To see Test Cases Run results please open ```report/pytest_html_report.html``` file in any available browser.

# Run tests 2
Open file ```tests/test_dqchecks_methods.py``` and press Ctrl+Shift+F10.

Open file ```tests/test_dqchecks_sqlscripts.py``` and press Ctrl+Shift+F10.

# Test Cases Run Result

Test run results are available in the pycharm console.
