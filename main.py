import re
import sqlite3
from typing import Any, List, Tuple
import sys
import pandas as pd

from constants import ALIAS_SQL_REGEX, COLS_SELECT_REGEX, QUERIES, SELECT_SQL_REGEX


def extract_columns(query: str) -> List[str]:
    """
    Extract all columns from a query SQL

    :query: The query SQL
    :return: List of columns
    """
    if select := re.match(SELECT_SQL_REGEX, query):
        cols = []
        for col in re.finditer(
            COLS_SELECT_REGEX,
            select.group(0),
        ):
            if match := re.match(ALIAS_SQL_REGEX, col.group(0)):
                cols.append(match.group(1))
            elif col.group(0) not in ["SELECT", "select"]:
                cols.append(col.group(0))
        return cols
    raise ValueError("Columns not found")


def read_file(filename: str) -> str:
    """
    Read a file and returns the text.

    :filename: The filename to read.
    :return: The text.
    """
    with open(filename, "r") as f:
        return f.read()


def execute_sql(filename_db: str, code_sql: str, long_query: bool = False) -> list:
    """
    Execute a SQL code.

    :filename_db: The name of DB.
    :code_sql: Code SQL to execute.
    :return: The result of code.
    """
    with sqlite3.connect(filename_db) as connection:
        cursor = connection.cursor()
        if long_query:
            cursor.executescript(code_sql)
        else:
            cursor.execute(code_sql)
        connection.commit()
        return cursor.fetchall()


def execute_query(db: str, *querys: Tuple[str, str]) -> None:
    """
    Execute all querys

    :db: Name of database.
    :querys: List of querys.
    """
    for i, (question, query) in enumerate(querys):
        print("~" * 90, f"{i+1}. {question}", "~" * 90, sep="\n")
        cols = extract_columns(query)
        print(pd.DataFrame(execute_sql(db, query), columns=cols))


def main(*args: Any) -> None:
    filename = args[0]
    content_file = read_file(filename)
    db = filename.replace(".sql", ".sqlite3")
    execute_sql(db, content_file, long_query=True)

    execute_query(db, *QUERIES)


if __name__ == "__main__":
    main(sys.argv)
