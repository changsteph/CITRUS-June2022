import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd


def box_plot(data):
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


def line_plot(data, plot_name: str, x_axis: str, y_axis: str, line_color="black", point_type="o",
              line_style="dashed", size=10):
    months_names = ["January", "February", "March", "April", "May", "June", "July", "August",
                    "September", "October", "November", "December"]

    plt.plot(data, color=line_color, marker=point_type, linestyle=line_style, markersize=size)
    for i, value in enumerate(data):
        plt.annotate(str(round(value, 3)), (i, value + 0.05))

    min_val = min(data) - 2
    max_val = max(data) + 2
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], months_names)
    plt.ylim(bottom=min_val, top=max_val)
    plt.xlabel(x_axis, fontsize=15)
    plt.ylabel(y_axis, fontsize=15)
    plt.title(plot_name, fontsize=25)
    # plt.legend(["legend1", "legend2", "legend3", "legend4"], title="Stations", loc='upper left')
    plt.grid(True)
    # plt.savefig("MeanWindSpeeds.png")
    plt.show()


def histogram(table, data, title_name, bin_width, bin_min, bin_max):
    # a histogram returns 3 objects : n (i.e. frequencies), bins, patches
    freq, bins, patches = plt.hist(data, edgecolor='white', label='d',
                                   bins=np.arange(bin_min, bin_max, bin_width))

    plt.xticks(np.arange(bin_min, bin_max, bin_width * 2))

    # x coordinate for labels
    bin_centers = np.diff(bins) * 0.5 + bins[:-1]

    height_list = []
    n = 0
    for fr, x, patch in zip(freq, bin_centers, patches):
        height = int(freq[n])
        height_list.append(height)
        if height > 0:
            plt.annotate("{}".format(height),
                         xy=(x, height),  # top left corner of the histogram bar
                         xytext=(0, 0.2),  # offsetting label position above its bar
                         textcoords="offset points",  # Offset (in points) from the *xy* value
                         ha='center', va='bottom'
                         )
        n = n + 1

    plt.yticks(range(max(height_list) + 1))
    plt.title(title_name)
    # plt.text(bin_min -0.1, max(height_list) - 1, text_string, fontsize=10, bbox=dict(facecolor='green', alpha=0.3),
    #          ha='left', va='bottom')
    plt.xlabel("Wind Speed m/s")
    figure_name = title_name + ".png"
    plt.savefig(figure_name)


def scatter_with_image(x_column, y_column, annotation_column, shape_file, table_name, image_color="Orange",
                       scatter_color="Blue", scatter_size=5, scatter_alpha=1.0):
    image_file = gpd.read_file(shape_file)
    graph = image_file.plot(color=image_color)
    plt.scatter(x=x_column, y=y_column, color=scatter_color, s=scatter_size, alpha=scatter_alpha, label=table_name)
    for i in range(len(annotation_column)):
        plt.annotate(annotation_column[i], xy=(x_column[i] + 0.02, y_column[i] + 0.02), textcoords='data')
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    # plt.legend(loc='lower left', title='Islands')
    plt.title(table_name, fontsize=12)
    plt.show()
