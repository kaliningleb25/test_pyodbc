import pypyodbc

conn = pypyodbc.connect(
    "Driver={SQL Server};"
    "Server=EPBYGROW00BD\\SQLEXPRESS;"
    "Database=AdventureWorks2012;"
    "Trusted_Connection=yes;"
)


def connect_db():
    conn_db = pypyodbc.connect(
        "Driver={SQL Server};"
        "Server=EPBYGROW00BD\\SQLEXPRESS;"
        "Database=AdventureWorks2012;"
        "Trusted_Connection=yes;"
    )
    return conn_db.cursor()


def connection_table_rows(table_name: str):
    cursor = connect_db()
    cursor.execute(f'select * from {table_name}')
    rows = []
    for row in cursor:
        rows.append(row)
    return rows


def table_columns(table_name: str):
    columns = ''
    columns_list = []
    cursor = connect_db()
    cursor.execute(f'select column_name FROM INFORMATION_SCHEMA.COLUMNS where table_name =\'{table_name}\'')
    for row in cursor:
        columns_list.append(row[0])
    return ', '.join(columns_list)






