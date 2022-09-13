import numpy as np
import pandas as pd
import re


def check_last_day(curr_year: int, curr_month: int, curr_day: int) -> bool:
    """
    Checks if the specified day is the last day in the specified month.
    Checks for 29 days during leap year (only years 1992 - 2020), otherwise 28 days for Feb.
    :param curr_year: year being checked
    :param curr_month: month being checked
    :param curr_day: day being checked
    :return: True if last day of month, otherwise false
    """
    # Total number of days in each month (not including Feb-leap year)
    # First value is 0 since index starts at 0, want to use indices 1 - 12
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check Feb separately (since it depends on if leap year)
    if curr_month == 2:
        # Check for 29 days if leap year, otherwise 28 days
        if (check_leap_year(curr_year) and curr_day == 29) or (not check_leap_year(curr_year) and curr_day == 28):
            return True
    # Check rest of months
    elif curr_day == days_in_month[curr_month]:
        return True

    return False


def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True

    return False


def aggregate_table(file_name, new_name, valid_percentage):
    table = pd.read_csv(file_name, index_col=0)
    index_names = list(table.index)
    # Create a list of all the columns names that contain dates
    date_columns = []
    date_names = []
    info_columns = []
    for name in list(table.columns):
        item = re.findall('\d+', name)
        if item:
            date_columns.append(name)
            date_names.append(item)
        else:
            info_columns.append(name)

    new_table = []
    # Combine data from days to months
    for index, row in table.iterrows():
        count = 0
        valid_count = 0
        data_sum = 0
        avg_row = []
        for num, column in enumerate(date_columns):
            year = int(date_names[num][0])
            month = int(date_names[num][1])
            count += 1
            value = row[column]
            if not pd.isnull(value):
                valid_count += 1
                data_sum += value

            if check_last_day(year, month, count):
                if valid_count / count >= valid_percentage:
                    avg_row.append(data_sum / valid_count)
                else:
                    avg_row.append(np.NaN)
                count = 0
                valid_count = 0
                data_sum = 0
        new_table.append(avg_row)

    column_names = []
    for date in date_names:
        name = str(date[0]) + '-' + str(date[1])
        if name not in column_names:
            column_names.append(name)

    if len(index_names) != len(column_names) and len(index_names) != len(new_table):
        return

    new_frame = pd.DataFrame(np.array(new_table), columns=column_names, index=index_names)
    info_table = table.filter(items=info_columns)
    average_table = pd.concat([info_table, new_frame], axis=1)
    # Write the new table (without extreme values to a new csv file)
    average_table.to_csv(r"{}.csv".format(new_name), na_rep='NA')


aggregate_table("CleanedWindSpeed1990_2021.csv", "AverageWindSpeeds", 0.75)
