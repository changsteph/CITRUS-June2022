import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np


def save_info():
    wind_median = wind_speed_table.iloc[:, 5:].median(axis=1, numeric_only=True)
    wm = wind_median.to_frame()
    file1 = open("WindSpeedData.txt", "w")
    file1.write("Mean of Wind Speeds\n")
    for row1 in wm.iterrows():
        file1.write(str(row1[0]) + " : " + str(row1[1].values) + "\n")

    file1.close()


def plot_info():
    wind_median = wind_speed_table.iloc[:, 5:].median(axis=1, numeric_only=True)
    lat = wind_speed_table['LAT'].tolist()
    lon = wind_speed_table['LON'].tolist()
    wind_data = wind_median.tolist()
    ax = plt.subplot()
    ax.scatter(x=lon[:51], y=lat[:51], s=wind_data[:51], c='blue', label='BI')
    ax.scatter(x=lon[51:73], y=lat[51:73], s=wind_data[51:73], c='magenta', label='MA')
    ax.scatter(x=lon[73:78], y=lat[73:78], s=wind_data[73:78], c='green', label='KO')
    ax.scatter(x=lon[78:84], y=lat[78:84], s=wind_data[78:84], c='purple', label='MO')
    ax.scatter(x=lon[84:87], y=lat[84:87], s=wind_data[84:87], c='orange', label='LA')
    ax.scatter(x=lon[87:120], y=lat[87:120], s=wind_data[87:120], c='red', label='OA')
    ax.scatter(x=lon[120:132], y=lat[120:132], s=wind_data[120:132], c='black', label='KA')
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("Mean Wind Speeds from 1990 - 2021")
    plt.legend(loc='lower left', title='Islands')
    ax.grid(True)
    ax.set_xlim(min(lon) - 0.5, max(lon) + 0.5)
    ax.set_ylim(min(lat) - 0.5, max(lat) + 0.5)
    plt.show()


def check_last_day(curr_year, curr_month, curr_day) -> bool:
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_years = [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
    if curr_month == 2:
        if (curr_year in leap_years and curr_day == 29) or (curr_year not in leap_years and curr_day == 28):
            return True
    elif curr_day == days_in_month[curr_month]:
        return True

    return False


wind_file = "Hawaii_Winds_Speed_1990_2021.csv"

wind_speed_table = pd.read_csv(wind_file, index_col=0)
column_names = list(wind_speed_table.columns)
column_names = column_names[5:]
wind_skn = list(wind_speed_table.index)

count = 0
month = 0
year = 0
null_count = 0
num_count = 0
month_sum = 0
data = []
all_data = {}

for index, row in wind_speed_table.iterrows():
    data = []
    for i in range(len(column_names)):
        if month != int(column_names[i][6:8]):
            count = 0
            null_count = 0
            num_count = 0
            month_sum = 0
            month = int(column_names[i][6:8])
            year = int(column_names[i][1:5])
        count += 1
        if pd.isnull(row[column_names[i]]):
            null_count += 1
        else:
            num_count += 1
            month_sum += row[column_names[i]]

        # If last day in month
        if check_last_day(year, month, count):
            data_available = num_count / count
            if data_available >= 0.75:
                wind_mean = month_sum / num_count
                data.append((year, month, round(wind_mean, 5), round(data_available, 4), null_count + num_count))

    all_data[str(index)] = data


file2 = open("MonthlyWindSpeed.txt", "w")
file2.write("Monthly Mean of Wind Speeds\n")
file2.write("Mean rounded to 5 decimal places\n")
file2.write("(Year, Month, Mean Wind Speed (m/s), Percentage of Data Available, Days in Month) \n\n")
for i in range(len(wind_skn)):
    file2.write(str(wind_skn[i]) + " : " + wind_speed_table.iloc[i]["Island"] +
                " : Valid Months (75+% data available): " + str(len(all_data[str(wind_skn[i])])) + "\n")
    file2.write(str(all_data[str(wind_skn[i])]) + "\n\n")

file2.close()

# print(total_months)
# np.nan
# df = {}
# df.to_csv(r"MonthlyWindSpeed.csv", index=True, header=True)
# Write the info to a text file called MonthlyWindSpeed
# file2 = open("MonthlyWindSpeed.txt", "w")
# file2.write("Monthly Mean of Wind Speeds\n")
# file2.write("Mean rounded to 5 decimal places\n")
# file2.write("(Year, Month, Mean Wind Speed (m/s), Percentage of Data Available, Days in Month) \n\n")
# for i in range(len(wind_skn)):
#     file2.write(str(wind_skn[i]) + " : " + wind_speed_table.iloc[i]["Island"] +
#                 " : Valid Months (75+% data available): " + str(len(all_data[str(wind_skn[i])])) + "\n")
#     file2.write(str(all_data[str(wind_skn[i])]) + "\n\n")
#
# file2.close()