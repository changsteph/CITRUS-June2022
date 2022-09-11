import numpy as np
import pandas as pd

file_max = "Max_Temperatures.csv"
file_min = "Min_Temperatures.csv"

min_temp_table = pd.read_csv(file_min, index_col=0)
max_temp_table = pd.read_csv(file_max, index_col=0)

years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006,
         2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
months_names = ["January", "February", "March", "April", "May", "June", "July", "August",
                "September", "October", "November", "December"]
month_columns = list(max_temp_table.columns)
month_columns = month_columns[12:]
skn_list = list(max_temp_table.index)
print(skn_list)
all_data = []

for index, row in max_temp_table.iterrows():
    months = []
    data_dict = {}
    for j in range(12):
        values = []
        for i in range(len(month_columns)):
            if int(month_columns[i][6:]) == j + 1:
                values.append(row[month_columns[i]])
        months.append(values)

    for j in range(len(months_names)):
        data_dict[months_names[j]] = months[j]
    all_data.append(data_dict)

print(len(all_data))

for i in range(len(all_data)):
    result = pd.DataFrame(all_data[i], columns=months_names, index=years)
    result.to_csv(r"{}-MonthMaxTemp.csv".format(skn_list[i]), na_rep='NA')
