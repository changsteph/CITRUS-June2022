import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu

wind_file1 = "703-HONOLULU INTERNATIONAL AIRPORT.csv"
wind_file2 = "840-KANEOHE BAY MCAS.csv"
wind_file3 = "842.8-MAKUA RANGE.csv"
wind_file4 = "911.1-KII.csv"

temp_file1 = "703-MonthAverageTemp.csv"
temp_file2 = "840-MonthAverageTemp.csv"
temp_file3 = "841.16-MonthAverageTemp.csv"
temp_file4 = "901.2-MonthAverageTemp.csv"

wind_table1 = pd.read_csv(wind_file1, index_col=0)
wind_table2 = pd.read_csv(wind_file2, index_col=0)
wind_table3 = pd.read_csv(wind_file3, index_col=0)
wind_table4 = pd.read_csv(wind_file4, index_col=0)

temp_table1 = pd.read_csv(temp_file1, index_col=0)
temp_table2 = pd.read_csv(temp_file2, index_col=0)
temp_table3 = pd.read_csv(temp_file3, index_col=0)
temp_table4 = pd.read_csv(temp_file4, index_col=0)

all_wind_tables = [
    wind_table1, wind_table2, wind_table3, wind_table4
]
all_temp_tables = [
    temp_table1, temp_table2, temp_table3, temp_table4
]
wind_station_names = [
    "703 HONOLULU INTERNATIONAL AIRPORT Wind Speeds",
    "840 KANEOHE BAY MCAS Wind Speeds",
    "842.8 MAKUA RANGE Wind Speeds",
    "911.1 KII Wind Speeds"
]

temp_station_names = [
    "703 HONOLULU INTERNATIONAL AIRPORT Temperatures",
    "840 KANEOHE BAY MCAS Temperatures",
    "841.16 CAMP ERDMAN Temperatures",
    "901.2 KII KAHUKU Temperatures"
]

months_names = ["January", "February", "March", "April", "May", "June", "July", "August",
                "September", "October", "November", "December"]

wind_mean_703 = [np.nan, 3.8439, 4.0899, 4.3602, 4.8278, 4.5749, 5.1531, 5.3453, 5.2483, 4.5631, 4.2667, 4.2173, 4.1329]
wind_mean_840 = [np.nan, 3.423, 3.7533, 3.934, 4.0726, 3.7081, 4.071, 4.231, 4.0671, 3.647, 3.4908, 3.6486, 3.5187]
wind_mean_842 = [np.nan, 3.1212, 3.3063, 3.5251, 3.4585, 3.1568, 3.2718, 3.3542, 3.2869, 3.1155, 3.1137, 3.1975, 3.1639]
wind_mean_911 = [np.nan, 4.8031, 5.0326, 5.2612, 6.2176, 6.0012, 6.6993, 6.5318, 6.3407, 5.8794, 5.3824, 5.7731, 5.1664]
wind_mean_list = [
    wind_mean_703,
    wind_mean_840,
    wind_mean_842,
    wind_mean_911,
]

temp_mean_703 = [np.nan, 23.071603633667042, 23.203731930321894, 23.665739710789765, 24.75887237415775, 25.58917050691244,
                 26.777777777777782, 27.44141705069124, 27.81094470046083, 27.53845238095238, 26.84793010752688,
                 25.46172619047619, 24.051958525345622]
temp_mean_840 = [np.nan, 22.9523334530335, 22.89845849766315, 23.200545104908805, 24.040703712071934, 24.74102554796334,
                 25.643042514637333, 26.097872513116197, 26.59960561584234, 26.727184488563797, 26.183349053748298,
                 24.898165001027074, 23.75592570144694]
temp_mean_841 = [np.nan, 22.25235413460803, 21.972517384802988, 22.506109680159334, 22.972154317186646, 23.80750870754812,
                 25.24433477348862, 25.440510486825, 25.762196823508585, 25.821351314310395, 25.392489154678245,
                 23.938920685668563, 23.119360799574782]
temp_mean_901 = [np.nan, 22.08718574546558, 22.032484204543497, 22.358555792838317, 23.13284042700872, 23.787254934581547,
                 24.863170005282072, 25.38120821812596, 25.76415072530752, 25.916493352349793, 25.348307758176908,
                 24.16226573786887, 23.0219198510064]

temp_mean_list = [
    temp_mean_703,
    temp_mean_840,
    temp_mean_841,
    temp_mean_901
]
# all_wind_dicts = []
# for table in all_wind_tables:
#     wind_dict = {}
#     for i in range(12):
#         month_list = list(table.iloc[:, i])
#         values = []
#         for j in range(len(month_list)):
#             if not np.isnan(month_list[j]):
#                 values.append(month_list[j])
#
#         wind_dict[months_names[i]] = values
#     all_wind_dicts.append(wind_dict)

all_temp_dicts = []
for table in all_temp_tables:
    temp_dict = {}
    for i in range(12):
        month_list = list(table.iloc[:, i])
        values = []
        for j in range(len(month_list)):
            if not np.isnan(month_list[j]):
                values.append(month_list[j])

        temp_dict[months_names[i]] = values
    all_temp_dicts.append(temp_dict)

# all_wind_dicts = []
# for table in all_wind_tables:
#     wind_dict = {}
#     for i in range(12):
#         month_list = list(table.iloc[:, i])
#         values = []
#         for j in range(len(month_list)):
#             if not np.isnan(month_list[j]):
#                 values.append(month_list[j])
#
#         wind_dict[months_names[i]] = values
#     all_wind_dicts.append(wind_dict)

# for i in range(len(all_temp_dicts)):
#     temp_mean = []
#     for j in range(12):
#         t_mean = np.mean(all_temp_dicts[i][months_names[j]])
#         temp_mean.append(t_mean)
#     print(temp_mean)
# file1 = open("TemperatureBoxPlotData.txt", "w")
# for j in range(len(all_temp_dicts)):
#     file1.write(temp_station_names[j] + " Box Plot Data\n")
#     for m in range(len(months_names)):
#         file1.write(months_names[m] + ":\n")
#         bp = plt.boxplot(all_temp_dicts[j][months_names[m]])
#         file1.write("Whiskers:\n")
#         for i in range(len(bp['whiskers'])):
#             median = bp["whiskers"][i].get_ydata()
#             file1.writelines(str(median) + "\n")
#
#         file1.write("Caps:\n")
#         for i in range(len(bp['caps'])):
#             median = bp["caps"][i].get_ydata()
#             file1.writelines(str(median) + "\n")
#
#         file1.write("Median:\n")
#         for i in range(len(bp['medians'])):
#             median = bp["medians"][i].get_ydata()
#             file1.writelines(str(median) + "\n")
#
#         file1.write("Fliers:\n")
#         for i in range(len(bp['fliers'])):
#             median = bp["fliers"][i].get_ydata()
#             file1.writelines(str(median) + "\n\n")
#     file1.write("\n\n")
#     plt.clf()
#
# file1.close()

# file1 = open("WindSpeedShapiro.txt", "w")
#
# for i in range(len(all_wind_dicts)):
#     file1.write("\n" + wind_station_names[i] + " Shapiro-Wilk test results\n")
#     for j in range(len(months_names)):
#         results = shapiro(all_wind_dicts[i][months_names[j]])
#         file1.write(months_names[j] + " " + str(results) + "\n")
#
# file1.close()

# file1 = open("TemperatureMannWhitney.txt", "w")
# file1.write(temp_station_names[2] + " + " + temp_station_names[3] + "\n")
# for j in range(len(months_names)):
#     results = mannwhitneyu(all_temp_dicts[2][months_names[j]], all_temp_dicts[3][months_names[j]])
#     file1.write(months_names[j] + " : " + str(results) + "\n")
#
# file1.close()
#

colors = ['magenta', 'green', 'blue', 'purple']
for i, w_value in enumerate(all_temp_dicts):
    fig, ax = plt.subplots()
    bp = ax.boxplot(w_value.values(), patch_artist=True)

    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color='black')

    for patch in bp['boxes']:
        patch.set(facecolor=colors[i], alpha=0.5)

    ax.set_ylim(top=18, bottom=30)
    # ax.set_xlabel("Months")
    ax.set_ylabel("Temperature (C)")
    ax.set_xticklabels(w_value.keys(), rotation=45)
    ax.set_title(temp_station_names[i])

    plt.plot(temp_mean_list[i], color='black', marker="o",
             linestyle="dashed", markersize=3, alpha=0.5)
    # for j, value in enumerate(temp_mean_list[i]):
    #     plt.annotate(str(round(value, 3)), (j, value + 0.05))

    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.ylim(bottom=18, top=30)
    plt.xlabel("Months", fontsize=15)
    # plt.ylabel("Temperature (C)", fontsize=15)
    # plt.title("Mean Oahu Temperatures", fontsize=25)
    # plt.legend(["703 HNL", "840 Kaneohe Bay", "841.16 Camp Erdman", "901.1 Kii"], title="Stations", loc='upper left')

    plt.savefig(temp_station_names[i] + "LinePlot.png", bbox_inches="tight")
    plt.clf()

# median_values = []
# for w_dict in all_temp_dicts:
#     location_list = []
#     for i in range(12):
#         location_list.append(np.median(w_dict[months_names[i]]))
#     median_values.append(location_list)
#
# plt.plot(median_values[0], color="magenta", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(median_values[0]):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(median_values[1], color="green", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(median_values[1]):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(median_values[2], color="blue", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(median_values[2]):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(median_values[3], color="purple", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(median_values[3]):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], months_names)
# # plt.ylim(bottom=20, top=30)
# plt.xlabel("Months", fontsize=20)
# plt.ylabel("Temperature (C)", fontsize=20)
# plt.title("Median Oahu Temperatures", fontsize=30)
# plt.legend(["703 HNL", "840 Kaneohe Bay", "841.16 Camp Erdman", "901.2 Kii"], title="Stations")
# plt.grid(True)
# plt.show()

# plt.plot(temp_mean_703, color="magenta", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(temp_mean_703):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(temp_mean_840, color="green", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(temp_mean_840):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(temp_mean_841, color="blue", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(temp_mean_841):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.plot(temp_mean_901, color="purple", marker="o", linestyle="dashed", markersize=10)
# for i, value in enumerate(temp_mean_901):
#     plt.annotate(str(round(value, 3)), (i, value + 0.05))
# plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], months_names)
# plt.ylim(bottom=21, top=29)
# plt.xlabel("Months", fontsize=15)
# plt.ylabel("Temperature (C)", fontsize=15)
# plt.title("Mean Oahu Temperatures", fontsize=25)
# plt.legend(["703 HNL", "840 Kaneohe Bay", "841.16 Camp Erdman", "901.1 Kii"], title="Stations", loc='upper left')
# plt.grid(True)
# plt.savefig("MeanWindSpeeds.png")
# plt.show()