from scipy.stats import shapiro

# index = 2
skn = 1023
wind_file = "1023-BARKING SANDS PMRF.csv"
wind_speed_table = pd.read_csv(wind_file, index_col=0)
column_lists = list(wind_speed_table.columns)
bin_width = 0.25
bin_min = 1.5
bin_max = 5.5
months = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]

file2 = open("1023 MonthlyDistribution.txt", "w")

for j in range(12):
    month_list = list(wind_speed_table[column_lists[j]])
    nonnull_data = []
    for i in range(len(month_list)):
        if not pd.isnull(month_list[i]):
            nonnull_data.append(month_list[i])

    month_mean = round(np.mean(nonnull_data), 4)
    month_median = round(np.median(nonnull_data), 4)
    text_string = 'mean: {} m/s\nmedian: {} m/s\npoints: {}\nbin width: {}\n'.format(month_mean, month_median,
                                                                            len(nonnull_data), bin_width)
    # a histogram returns 3 objects : n (i.e. frequncies), bins, patches
    freq, bins, patches = plt.hist(nonnull_data, edgecolor='white', label='d',
                                   bins=np.arange(bin_min, bin_max, bin_width))

    plt.xticks(np.arange(bin_min, bin_max, bin_width * 2))

    # x coordinate for labels
    bin_centers = np.diff(bins)*0.5 + bins[:-1]

    height_list = []

    n = 0
    for fr, x, patch in zip(freq, bin_centers, patches):
      height = int(freq[n])
      height_list.append(height)
      if height > 0:
          plt.annotate("{}".format(height),
                       xy = (x, height),             # top left corner of the histogram bar
                       xytext = (0,0.2),             # offsetting label position above its bar
                       textcoords = "offset points", # Offset (in points) from the *xy* value
                       ha = 'center', va = 'bottom'
                       )
      n = n+1

    title_name = "{} - {} Wind Speed Distribution".format(skn, months[j])
    plt.yticks(range(max(height_list) + 1))
    plt.title(title_name)
    # plt.text(bin_min -0.1, max(height_list) - 1, text_string, fontsize=10, bbox=dict(facecolor='green', alpha=0.3),
    #          ha='left', va='bottom')
    plt.xlabel("Wind Speed m/s")

    figure_name = str(skn) + " " + months[j] + ".png"
    plt.savefig(figure_name)
    plt.clf()
    file2.write(months[j] + " Data\n")
    file2.write(text_string + "\n")


file2.close()
# print(shapiro(month_list))