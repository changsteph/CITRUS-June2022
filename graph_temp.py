import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

min_file = "68.13-MonthMinTemp.csv"
max_file = "68.13-MonthMaxTemp.csv"

min_table = pd.read_csv(min_file, index_col=0)
max_table = pd.read_csv(max_file, index_col=0)

# bin_width = 1
# bin_min = 15
# bin_max = 35

min_column_values = list(min_table["January"])
max_column_values = list(max_table["January"])
# min_values = []
# for i in range(len(min_column_values)):
#     if not np.isnan(min_column_values[i]):
#         min_values.append(min_column_values[i])
# plt.boxplot(min_values, vert=False)

max_value = int(max_station_value[count]) + 1.5
min_value = max(int(min_station_value[count]) - 0.5, 0)
plot_title = str(index) + " " + months[i] + " Average Wind Speeds"
plt.xticks(range(min(year_list), max(year_list) + 1), rotation=45)
plt.yticks(np.arange(0, max_value, 0.25))
plt.ylim(min_value, max_value)
plt.plot(year_list, value_list, ls='dashed', marker='.', markersize=10)
plt.title(plot_title)
plt.grid(True)
plt.ylabel("Wind Speed m/s")
figure_name = plot_title + ".png"
plt.savefig(figure_name)
# plt.clf()

plt.show()
