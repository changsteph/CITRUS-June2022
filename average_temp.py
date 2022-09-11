import pandas as pd

file1_max = "703.0-MonthMaxTemp.csv"
file1_min = "703.0-MonthMinTemp.csv"
file2_max = "840.0-MonthMaxTemp.csv"
file2_min = "840.0-MonthMinTemp.csv"
file3_max = "841.16-MonthMaxTemp.csv"
file3_min = "841.16-MonthMinTemp.csv"
file4_max = "901.2-MonthMaxTemp.csv"
file4_min = "901.2-MonthMinTemp.csv"

months_names = ["January", "February", "March", "April", "May", "June", "July", "August",
                "September", "October", "November", "December"]

skn_list = ["703", "840", "841.16", "901.2"]

temp1_max_table = pd.read_csv(file1_max, index_col=0)
temp1_min_table = pd.read_csv(file1_min, index_col=0)
temp2_max_table = pd.read_csv(file2_max, index_col=0)
temp2_min_table = pd.read_csv(file2_min, index_col=0)
temp3_max_table = pd.read_csv(file3_max, index_col=0)
temp3_min_table = pd.read_csv(file3_min, index_col=0)
temp4_max_table = pd.read_csv(file4_max, index_col=0)
temp4_min_table = pd.read_csv(file4_min, index_col=0)

average1_table = pd.DataFrame()
average2_table = pd.DataFrame()
average3_table = pd.DataFrame()
average4_table = pd.DataFrame()
for i in range(12):
    average1_table[months_names[i]] = (temp1_max_table[months_names[i]] + temp1_min_table[months_names[i]]) / 2
    average2_table[months_names[i]] = (temp2_max_table[months_names[i]] + temp2_min_table[months_names[i]]) / 2
    average3_table[months_names[i]] = (temp3_max_table[months_names[i]] + temp3_min_table[months_names[i]]) / 2
    average4_table[months_names[i]] = (temp4_max_table[months_names[i]] + temp4_min_table[months_names[i]]) / 2


average1_table.to_csv(r"{}-MonthAverageTemp.csv".format(skn_list[0]), na_rep='NA')
average2_table.to_csv(r"{}-MonthAverageTemp.csv".format(skn_list[1]), na_rep='NA')
average3_table.to_csv(r"{}-MonthAverageTemp.csv".format(skn_list[2]), na_rep='NA')
average4_table.to_csv(r"{}-MonthAverageTemp.csv".format(skn_list[3]), na_rep='NA')

