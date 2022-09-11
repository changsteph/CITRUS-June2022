import pandas as pd

skn_used = [1020.1, 1023, 901.2, 841.16, 702.2, 703, 840, 398, 68.13, 87]
skn_used.sort()

file_names = ["temperature_min_1990.csv", "temperature_min_1991.csv", "temperature_min_1992.csv",
              "temperature_min_1993.csv", "temperature_min_1994.csv", "temperature_min_1995.csv",
              "temperature_min_1996.csv", "temperature_min_1997.csv", "temperature_min_1998.csv",
              "temperature_min_1999.csv", "temperature_min_2000.csv", "temperature_min_2001.csv",
              "temperature_min_2002.csv", "temperature_min_2003.csv", "temperature_min_2004.csv",
              "temperature_min_2005.csv", "temperature_min_2006.csv", "temperature_min_2007.csv",
              "temperature_min_2008.csv", "temperature_min_2009.csv", "temperature_min_2010.csv",
              "temperature_min_2011.csv", "temperature_min_2012.csv", "temperature_min_2013.csv",
              "temperature_min_2014.csv", "temperature_min_2015.csv", "temperature_min_2016.csv",
              "temperature_min_2017.csv", "temperature_min_2018.csv",
              ]
# file_names = ["temperature_max_1990.csv", "temperature_max_1991.csv", "temperature_max_1992.csv",
#               "temperature_max_1993.csv", "temperature_max_1994.csv", "temperature_max_1995.csv",
#               "temperature_max_1996.csv", "temperature_max_1997.csv", "temperature_max_1998.csv",
#               "temperature_max_1999.csv", "temperature_max_2000.csv", "temperature_max_2001.csv",
#               "temperature_max_2002.csv", "temperature_max_2003.csv", "temperature_max_2004.csv",
#               "temperature_max_2005.csv", "temperature_max_2006.csv", "temperature_max_2007.csv",
#               "temperature_max_2008.csv", "temperature_max_2009.csv", "temperature_max_2010.csv",
#               "temperature_max_2011.csv", "temperature_max_2012.csv", "temperature_max_2013.csv",
#               "temperature_max_2014.csv", "temperature_max_2015.csv", "temperature_max_2016.csv",
#               "temperature_max_2017.csv", "temperature_max_2018.csv",
#               ]

max_temp_table = []
for i in range(len(file_names)):
    temp_table = pd.read_csv(file_names[i], index_col=0)
    temp_table = temp_table[temp_table.index.isin(skn_used)]
    max_temp_table.append(temp_table)

print(len(max_temp_table))
result = max_temp_table[0]
for i in range(1, len(max_temp_table)):
    result = pd.concat([result, max_temp_table[i].iloc[:, 12:]], axis=1, join='outer')

result.to_csv(r"Min_Temperatures.csv", na_rep='NA')
