"""
Calculates the mean of monthly wind speeds if 75% or more of values for the month are available (not NaN).
Output results to a text file.
Assumes code is in the same folder as csv file (if it's not, change the wind_file string to the path)
"""
import pandas as pd
import numpy as np


def check_last_day(curr_year, curr_month, curr_day) -> bool:
    """
    Checks if the specified day is the last day in the specified month.
    Checks for 29 days during leap year (only years 1992 - 2020), otherwise 28 days for Feb.
    :param curr_year: year being checked
    :param curr_month: month being checked
    :param curr_day: day being checked
    :return: True if last day of month, otherwise false
    """
    # Total number of days in each month (not including Feb-leap year)
    # First value is 0 since index starts at 0, want to use indices 1 - 12
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # List of leap years
    leap_years = [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]

    # Check Feb separately (since it depends on if leap year)
    if curr_month == 2:
        # Check for 29 days if leap year, otherwise 28 days
        if (curr_year in leap_years and curr_day == 29) or (curr_year not in leap_years and curr_day == 28):
            return True
    # Check rest of months
    elif curr_day == days_in_month[curr_month]:
        return True

    return False


# Path to the wind file (my file is in the same folder as the python script & project)
wind_file = "CleanedWindSpeeds.csv"

# Read file and convert it to a DataFrame Object (first column(0), SKN,  is the index)
wind_speed_table = pd.read_csv(wind_file, index_col=0)
# List of column names from column 5 (start of dates & wind speed values) to the end
column_names = list(wind_speed_table.columns)
column_names = column_names[5:]
# List of the SKN from the table
wind_skn = list(wind_speed_table.index)


station_names = list(wind_speed_table["Station.Name"])
island_names = list(wind_speed_table["Island"])
elevations = list(wind_speed_table["ELEV.m."])
latitudes = list(wind_speed_table["LAT"])
longitudes = list(wind_speed_table["LON"])

new_column_names = []
month_names = 1

for i in range(1990, 2022):
    for j in range(1, 13):
        if j < 10:
            new_column_names.append(str(i) + "-0" + str(j))
        else:
            new_column_names.append(str(i) + "-" + str(j))

count = 0
month = 0
year = 0
null_count = 0
month_sum = 0
num_count = 0
data = []
all_data = []


# Go through each row in the table
for index, row in wind_speed_table.iterrows():
    data = []
    # Go through each wind speed column in the row
    for i in range(len(column_names)):
        # If it's a new month, reset values
        if month != int(column_names[i][6:8]):
            count = 0
            null_count = 0
            num_count = 0
            month_sum = 0
            month = int(column_names[i][6:8])
            year = int(column_names[i][1:5])
        # Add a day to the count
        count += 1
        # If the value is NaN
        if pd.isnull(row[column_names[i]]):
            null_count += 1
        else:
            num_count += 1
            month_sum += row[column_names[i]]

        # If last day in month
        if check_last_day(year, month, count):
            data_available = num_count / count
            # If 75+% of data was available for the month
            if data_available >= 0.75:
                # Calculate wind mean speed
                wind_mean = month_sum / num_count
                # Add to list of wind means
                data.append(round(wind_mean, 5))
            else:
                data.append(np.nan)
    # Add list to 2D array
    all_data.append(data)


avg_wind = pd.DataFrame(all_data, index=wind_skn, columns=new_column_names)
avg_wind.index.name = "SKN"
avg_wind.insert(0, "Station.Name", station_names, True)
avg_wind.insert(1, "Island", island_names, True)
avg_wind.insert(2, "ELEV.m.", elevations, True)
avg_wind.insert(3, "LAT", latitudes, True)
avg_wind.insert(4, "LON", longitudes, True)

selected_skn = [63, 68.21, 87, 398, 499.8, 553, 702.7, 703, 752.6, 840, 842.8, 911.1, 1020.1, 1023]

avg_wind.loc[(avg_wind["ELEV.m."] <= 50) & (avg_wind.index.isin(selected_skn))].to_csv(r"SelectedMonthlySpeeds.csv", na_rep='NA')



