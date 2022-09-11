import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

wild_file = "SelectedWindCount.csv"
island_file = "Coastline.shp"
temp_file = "Max_Temperatures.csv"

# Selected stations (can remove)
skn_used = [703, 840, 841.16, 901.2]
wind_skn = [703, 840, 842.8, 911.1]
skn_used.sort()

# Get data frame from csv files
wind_table = pd.read_csv(wild_file, index_col=0)
temp_table = pd.read_csv(temp_file, index_col=0)
# latitude = list(wind_table["LAT"].loc[wind_table["ELEV.m."] <= 50])
# longitude = list(wind_table["LON"].loc[wind_table["ELEV.m."] <= 50])
# latitude = list(wind_table.loc[wind_skn]["LAT"])
# longitude = list(wind_table.loc[wind_skn]["LON"])
# t_latitude = list(temp_table.loc[skn_used]["LAT"])
# t_longitude = list(temp_table.loc[skn_used]["LON"])

skn_used = [39, 47, 324.6, 328.4, 339.4]
lat = [19.5362, 19.47555556, 20.75788889, 20.75763889, 20.75980556]
lon = [-155.5763, -155.3627778, -156.3200278, -156.2775, -156.2481667]
# skn_list = list(temp_table.loc[temp_table['ELEV.m.'] <= 50].index)
# print(t_latitude)
# print(t_longitude)

hawaiian_islands = gpd.read_file(island_file)
graph = hawaiian_islands.plot(color="Magenta")
plt.scatter(x=lon, y=lat, color='Blue', s=4, label='Wind Stations')
# for i in range(len(skn_used)):
#     plt.annotate(str(skn_used[i]), xy=(lon[i] + 0.02, lat[i] + 0.02), textcoords='data')
#
# plt.scatter(x=t_longitude, y=t_latitude, color='Magenta', s=20, alpha=0.5, label='Temperature Stations')
# for i in range(len(skn_used)):
#     plt.annotate(str(skn_used[i]), xy=(t_longitude[i] + 0.01, t_latitude[i] - 0.01), textcoords='data')


# for xy in zip(t_longitude, t_latitude):
#     plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
# for i in range(len(skn_list)):
#     plt.annotate('%s' % skn_list[i], xy=(t_longitude[i], t_latitude[i]), textcoords='data')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
# plt.legend(loc='lower left', title='Islands')
plt.title("Map of Wind Speed Stations Used for Analysis", fontsize=12)
plt.show()


