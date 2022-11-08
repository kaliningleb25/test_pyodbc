import pytest
import connections
import dqchecks

table_address = connections.connection_table_rows('[AdventureWorks2012].[Person].[Address]')
table_document = connections.connection_table_rows('[AdventureWorks2012].[Production].[Document]')
table_unitmeasure = connections.connection_table_rows('[AdventureWorks2012].[Production].[UnitMeasure]')


# Run tests for [Person].[Address] table
def test_dq_checks_table_address():
    assert dqchecks.verify_completeness(table_address) is None


def test_dq_checks_table_address_max():
    assert dqchecks.verify_max_length(table_address, dqchecks.max_len(table_address)) is None


def test_dq_checks_future_date_address():
    assert dqchecks.date_in_future(table_address, 8) == 0


def test_dq_checks_column_count_address():
    assert dqchecks.columns_count(table_address) == 9


# Run tests for [Production].[Document] table
def test_dq_checks_table_document():
    assert dqchecks.verify_completeness(table_document) is None


def test_dq_checks_table_document_max():
    assert dqchecks.verify_max_length(table_document, dqchecks.max_len(table_document)) is None


def test_duplicates_documents():
    assert dqchecks.duplicates('[AdventureWorks2012].[Production].[Document]', 'Document') is None


def test_dq_checks_table_document_status_column():
    assert dqchecks.verify_allowed_values(table_document, 9, [1, 2, 3]) == 0


def test_dq_checks_table_document_flag_column():
    assert dqchecks.verify_allowed_values(table_document, 4, [0, 1]) == 0


def test_dq_checks_future_date_documents():
    assert dqchecks.date_in_future(table_document, 13) == 0


def test_dq_checks_column_count_documents():
    assert dqchecks.columns_count(table_document) == 14


# Run tests for [Production].[UnitMeasure] table
def test_dq_checks_table_unitmeasure():
    assert dqchecks.verify_completeness(table_unitmeasure) is None


def test_dq_checks_table_unitmeasure_max():
    assert dqchecks.verify_max_length(table_unitmeasure, dqchecks.max_len(table_unitmeasure)) is None


def test_duplicates_unitmeasure():
    assert dqchecks.duplicates('[AdventureWorks2012].[Production].[UnitMeasure]', 'UnitMeasure') is None


def test_dq_checks_future_date_unitmeasure():
    assert dqchecks.date_in_future(table_unitmeasure, 2) == 0


def test_dq_checks_column_count_unitmeasure():
    assert dqchecks.columns_count(table_unitmeasure) == 3

