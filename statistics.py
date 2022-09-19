from scipy.stats import shapiro
from scipy.stats import mannwhitneyu


def shapiro_test(data):
    print(shapiro(month_list))

    file1 = open("WindSpeedShapiro.txt", "w")

    for i in range(len(all_wind_dicts)):
        file1.write("\n" + wind_station_names[i] + " Shapiro-Wilk test results\n")
        for j in range(len(months_names)):
            results = shapiro(all_wind_dicts[i][months_names[j]])
            file1.write(months_names[j] + " " + str(results) + "\n")

    file1.close()


def mannwhitneyu_test(data):
    file1 = open("TemperatureMannWhitney.txt", "w")
    file1.write(temp_station_names[2] + " + " + temp_station_names[3] + "\n")
    for j in range(len(months_names)):
        results = mannwhitneyu(all_temp_dicts[2][months_names[j]], all_temp_dicts[3][months_names[j]])
        file1.write(months_names[j] + " : " + str(results) + "\n")

    file1.close()
