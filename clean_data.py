import numpy as np
import pandas as pd
import re


def clean_table(file_name: str, max_value: float, min_value: float, new_name: str):
    """
    Removes values outside the range given by turning them into NaN.
    Creates a text file with the count of valid values, null values and extreme values
    (outside the given range) for each row in the table.
    :param file_name: name of the file to open
    :param max_value: max value(inclusive) of the column values
    :param min_value: min value(inclusive) of the column values
    :param new_name: new name of the cleaned table
    """
    table = pd.read_csv(file_name, index_col=0)

    index_names = list(table.index)
    # Create a list of all the columns names that contain dates
    column_list = []
    for name in list(table.columns):
        item = re.match('\d+', name)
        if item:
            column_list.append(name)

    table_info = {}
    # Remove extreme values, count types of data points
    for index, row in table.iterrows():
        extreme_values = 0
        null_values = 0
        valid_points = 0
        for column in column_list:
            value = row[column]
            if pd.isnull(value):
                null_values += 1
            elif value > max_value or value < min_value:
                extreme_values += 1
                table.loc[index, column] = np.NaN
            else:
                valid_points += 1
            table_info[index] = {
                "valid points": valid_points,
                "extreme values": extreme_values,
                "null values": null_values
            }

    # Write table info to a text file
    file1 = open("{}_Info.txt".format(new_name), "w")
    file1.write("Table Data Information\n")
    for index in index_names:
        file1.write(str(index) + ":\n")
        file1.write(str(table_info.get(index, "No info found")) + "\n\n")

    file1.close()

    # Write the new table (without extreme values to a new csv file)
    table.to_csv(r"{}.csv".format(new_name), na_rep='NA')


wind_file = "/TestFiles/Hawaii_Winds_Speed_1990_2021.csv"
clean_table(wind_file, 49, 0, "CleanedWindSpeed1990_2021")
