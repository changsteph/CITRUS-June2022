import pandas as pd

wind_file = "CleanedSelectedWind.csv"

wind_speed_table = pd.read_csv(wind_file, index_col=0)

column_names = list(wind_speed_table.columns)
column_names = column_names[5:]
wind_skn = list(wind_speed_table.index)
month_columns = ['Island', 'LAT', 'LON', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
                 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data_list = []
skn_list = []


for index, row in wind_speed_table.iterrows():
    months = [0] * 12
    island_list = []
    latitude = []
    longitude = []
    # Go through each wind speed column in the row
    for i in range(len(column_names)):
        if not pd.isnull(row[column_names[i]]):
            num = int(column_names[i][5:])
            months[num - 1] += 1
    if min(months) > 10:
        skn_list.append(index)
        island_list.append(wind_speed_table.loc[index]['Island'])
        latitude.append(wind_speed_table.loc[index]['LAT'])
        longitude.append(wind_speed_table.loc[index]['LON'])
        data_list.append(island_list + latitude + longitude + months)

save_data = pd.DataFrame(data_list, columns=month_columns, index=skn_list)
save_data.to_csv(r"SelectedWindCount.csv", na_rep='NA')
