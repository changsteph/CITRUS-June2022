import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

wind_file = "SelectedMonthlySpeeds.csv"
wind_speed_table = pd.read_csv(wind_file, index_col=0)

months = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
column_names = list(wind_speed_table.columns)
column_names = column_names[5:]
max_station_value = []
min_station_value = []

for index, row in wind_speed_table.iterrows():
    max_value = 0
    min_value = 100
    for j in range(len(column_names)):
        if row[column_names[j]] > max_value:
            max_value = row[column_names[j]]
        if row[column_names[j]] < min_value:
            min_value = row[column_names[j]]

    max_station_value.append(max_value)
    min_station_value.append(min_value)


count = 0
for index, row in wind_speed_table.iterrows():
    for i in range(12):
        value_list = []
        year_list = []
        for j in range(len(column_names)):
            if int(column_names[j][5:]) == i + 1 and not pd.isnull(row[column_names[j]]):
                value_list.append(row[column_names[j]])
                year_list.append(int(column_names[j][:4]))

        max_value = int(max_station_value[count]) + 1.5
        min_value = max(int(min_station_value[count]) - 0.5, 0)
        plot_title = str(index) + " " + months[i] + " Average Wind Speeds"
        plt.xticks(range(min(year_list),  max(year_list) + 1), rotation=45)
        plt.yticks(np.arange(0, max_value, 0.25))
        plt.ylim(min_value, max_value)
        plt.plot(year_list, value_list, ls='dashed', marker='.', markersize=10)
        plt.title(plot_title)
        plt.grid(True)
        plt.ylabel("Wind Speed m/s")
        figure_name = plot_title + ".png"
        plt.savefig(figure_name)
        plt.clf()

    count += 1
