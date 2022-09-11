import numpy as np
import pandas as pd
import re


def get_date_columns(file):
    # wind_file = "Hawaii_Winds_Speed_1990_2021.csv"
    table = pd.read_csv(file, index_col=0)

    # Create a list of all the columns names that contain dates
    date_list = []
    for name in list(table.columns):
        if re.findall('\d+', name):
            date_list.append(name)


def remove_extreme_values(column_list, table, max_value, min_value, new_name):
    # TODO: Find way to document extreme values (in text file?)
    for column in column_list:
        table.loc[(table[column] < min_value) | (table[column] > max_value), column] = np.NaN

    # Write the new table (without extreme values to a new csv file)
    table.to_csv(r"{}.csv".format(new_name), na_rep='NA')


def clean_selected_wind_data():
    clean_file = 'CleanedSelectedWind.csv'
    clean_table = pd.read_csv(clean_file, index_col=0)
    # selected_file = "SelectedMonthlySpeeds.csv"
    # selected_table = pd.read_csv(selected_file, index_col=0)
    # selected_table = selected_table.dropna(how='all', axis=1)
    # selected_table.to_csv(r"CleanedSelectedWind.csv", na_rep='NA')
    rearrange_data(clean_table)


def rearrange_data(table):
    bi_table = table[table['Island'] == 'BI']
    ma_table = table[table['Island'] == 'MA']
    ko_table = table[table['Island'] == 'KO']
    mo_table = table[table['Island'] == 'MO']
    oa_table = table[table['Island'] == 'OA']
    ka_table = table[table['Island'] == 'KA']

    # consolidate_months(bi_table)
    # consolidate_months(ma_table)
    # consolidate_months(ko_table)
    # consolidate_months(mo_table)
    consolidate_months(oa_table)
    # consolidate_months(ka_table)


def consolidate_months(table):
    column_names = table.columns
    column_names = column_names[5:]
    month_columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months = [[], [], [], [], [], [], [], [], [], [], [], []]
    table_skn = list(table.index)
    data_dict = {}
    bi_dataframes = []

    # Go through each row in the table
    for index, row in table.iterrows():
        months = [[], [], [], [], [], [], [], [], [], [], [], []]
        # Go through each wind speed column in the row
        for i in range(len(column_names)):
            if not pd.isnull(row[column_names[i]]):
                num = int(column_names[i][5:])
                months[num - 1].append(row[column_names[i]])

        max_num = 0
        for k in range(len(months)):
            max_num = max(len(months[k]), max_num)
        for m in range(len(months)):
            while len(months[m]) < max_num:
                months[m].append(np.nan)
        for j in range(len(month_columns)):
            data_dict[month_columns[j]] = months[j]
        save_data = pd.DataFrame(data_dict)
        bi_dataframes.append(save_data)

    print(len(bi_dataframes))
    # bi_dataframes[0].to_csv(r"701.01-Kalaeloa.csv", na_rep='NA')
    # bi_dataframes[1].to_csv(r"702.7-Kapolei-Kalaeloa AP.csv", na_rep='NA')
    # bi_dataframes[2].to_csv(r"703-HONOLULU INTERNATIONAL AIRPORT.csv", na_rep='NA')
    # bi_dataframes[3].to_csv(r"742.4-HONOULIULI PHB.csv", na_rep='NA')
    # bi_dataframes[4].to_csv(r"752.6-WAIAWA PHB.csv", na_rep='NA')
    # bi_dataframes[5].to_csv(r"757-Hickam Field.csv", na_rep='NA')
    # bi_dataframes[6].to_csv(r"781.31-Kaneohe HI US D9459-DW9459.csv", na_rep='NA')
    # bi_dataframes[7].to_csv(r"793.2-BELLOWS AFS AT WAIMANALO.csv", na_rep='NA')
    # bi_dataframes[8].to_csv(r"801.2-WAIANAE BOAT HARBOR.csv", na_rep='NA')
    # bi_dataframes[9].to_csv(r"837.8-Heeia NERR.csv", na_rep='NA')
    # bi_dataframes[10].to_csv(r"840-KANEOHE BAY MCAS.csv", na_rep='NA')
    # bi_dataframes[11].to_csv(r"842.8-MAKUA RANGE.csv", na_rep='NA')
    # bi_dataframes[12].to_csv(r"843.7-DILLIINGHAM.csv", na_rep='NA')
    # bi_dataframes[13].to_csv(r"886.8-Hakipuu Mauka.csv", na_rep='NA')
    # bi_dataframes[14].to_csv(r"903.4-Laie HI US C5306-CW5306.csv", na_rep='NA')
    # bi_dataframes[15].to_csv(r"911.1-KII.csv", na_rep='NA')
    # bi_dataframes[16].to_csv(r"912-KAUHUKU.csv", na_rep='NA')



# clean_selected_wind_data()
