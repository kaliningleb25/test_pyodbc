import connections


# function to find max length value
def max_len(records: list) -> int:
    max_len_value = len(str(records[0][0]))
    for i in range(len(records)):
        for j in range(len(records[i])):
            if len(str(records[i][j])) > max_len_value:
                max_len_value = len(str(records[i][j]))
    return max_len_value


# Declare percentage function
# Exception was added
def get_result_by_percentage(corrupted_records_amount: int, overall_records_amount: int, description: str) -> bool:
    try:
        print(description, ' ', (corrupted_records_amount / overall_records_amount), ' %')
    except:
        print('The table being checked is empty (has zero rows).')
    pass


# function to find records with null or empty values
def verify_completeness(records: list) -> bool:
    records_amount_with_empty_values = 0
    for row in records:
        if row == '' or None:
            records_amount_with_empty_values += 1
    return get_result_by_percentage(records_amount_with_empty_values, len(records), "Percentage of completed records")


# function to find records with value length more than expected
def verify_max_length(records: list, max_length: int):
    records_amount_with_values_more_than_max_length = 0
    for i in range(len(records)):
        for j in range(len(records[i])):
            if len(str(records[i][j])) < max_length:
                records_amount_with_values_more_than_max_length += 1
    return get_result_by_percentage(records_amount_with_values_more_than_max_length, len(records),
                                    f"Percentage of records with length less than {max_length}")


# function to find records with not allowed values
def verify_allowed_values(records: list, column_number, allowed_values: list):
    records_amount_with_not_allowed_values = 0
    for i in range(len(records)):
        if records[i][column_number] not in allowed_values:
            records_amount_with_not_allowed_values += 1
    return records_amount_with_not_allowed_values
    # get_result_by_percentage(records_amount_with_not_allowed_values, len(records),f"Percentage of records with
    # allowed values ({allowed_values})")


# functions to find duplicates in the table
def duplicates(full_table_name: str, table_name: str):
    cursor = connections.conn.cursor()
    columns = connections.table_columns(table_name)
    cursor.execute(f'select {columns} , COUNT(*) FROM {full_table_name} group by {columns} having count(*) > 1')
    for row in cursor:
        return row[0]


# functions to find dates in the future
def date_in_future(records: str, column_number):
    import datetime
    now = datetime.datetime.now()
    records_amount_date_in_future = 0
    for i in range(len(records)):
        for j in range(len(records[i])):
            if str(records[i][column_number]) > str(now):
                records_amount_date_in_future += 1
    return records_amount_date_in_future
    # get_result_by_percentage(records_amount_date_in_future, len(records),f"Percentage of records with dates in the
    # future ")


# functions to find columns count
def columns_count(records: str):
    table_columns_count = 0
    for i in range(len(records)):
        table_columns_count = len(records[i])
    return table_columns_count
