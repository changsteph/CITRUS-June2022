import numpy as np
import pandas as pd
import re


def clean_table(file_name, max_value, min_value, new_name):
    table = pd.read_csv(file_name, index_col=0)

    index_names = list(table.index)
    # Create a list of all the columns names that contain dates
    column_list = []
    for name in list(table.columns):
        item = re.findall('\d+', name)
        if item:
            column_list.append(name)

    table_info = {}
    for index, row in table.iterrows():
        extreme_values = 0
        null_values = 0
        valid_points = 0
        for num, column in enumerate(column_list):
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

    file1 = open("{}_Info.txt".format(new_name), "w")
    file1.write("Table Data Information\n")
    for index in index_names:
        file1.write(str(index) + ":\n")
        file1.write(str(table_info.get(index, "No info found")) + "\n\n")

    file1.close()

    # Write the new table (without extreme values to a new csv file)
    table.to_csv(r"{}.csv".format(new_name), na_rep='NA')


def split_table(table, column_name: str):
    categories = table[column_name].tolist()
    categories = set(categories)
    new_tables = []
    for category in categories:
        new_tables.append(table[table[column_name]] == category)


wind_file = "/TestFiles/Hawaii_Winds_Speed_1990_2021.csv"
clean_table(wind_file, 49, 0, "CleanedWindSpeed1990_2021")
