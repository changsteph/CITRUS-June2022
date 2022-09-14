import matplotlib.pyplot as plt


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


