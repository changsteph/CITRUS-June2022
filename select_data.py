import numpy as np
import pandas as pd
import re


def select_by_category(table, column_name: str, category_name: str):
    new_table = table.loc[table[column_name] == category_name]
    return new_table


def select_by_index(table, index):
    """
    Creates a new table with all the average values from row with the specified index. The new columns are the months
    of the year and the new rows are the years. The rows with all null values at the beginning and the end of the
    dataset will be removed.
    :param table: table to get values from
    :param index: index of row to get values from table
    """

    # Get the name of all the date columns
    date_columns = []
    year_list = []
    for column in list(table.columns):
        name = re.findall("\d+", column)
        if name:
            date_columns.append(column)
            if name[0] not in year_list:
                year_list.append(name[0])

    # Split values into new arrays based on year
    table_values = []
    month_values = []
    for column in date_columns:
        month = int(column[5:])
        value = table.loc[index, column]
        if np.isnan(value):
            month_values.append(None)
        else:
            month_values.append(value)
        if month == 12:
            table_values.append(month_values)
            month_values = []

    # Remove rows with all null values at beginning and end of rows
    print(table_values[-1])
    while len(table_values) > 0:
        if table_values[0].count(None) == 12:
            table_values.pop(0)
            year_list.pop(0)
        elif table_values[-1].count(None) == 12:
            table_values.pop()
            year_list.pop()
        else:
            break

    # Create new table with months as columns and years as indices
    months_names = ["01-January", "02-February", "03-March", "04-April", "05-May", "06-June", "07-July", "08-August",
                    "09-September", "10-October", "11-November", "12-December"]
    new_table = pd.DataFrame(np.array(table_values), columns=months_names, index=year_list)
    new_name = str(index) + "-Monthly Averages"
    new_table.to_csv(r"{}.csv".format(new_name), na_rep='NA')


wind_table = pd.read_csv("AverageWindSpeeds.csv", index_col=0)
select_by_index(wind_table, 39)
