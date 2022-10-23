import pandas as pd
import clean_data as clean


class DataTable:
    def __init__(self, file_name):
        self.table = pd.read_csv(file_name, index_col=0)


def get_input(menu: str):
    print(menu)
    result = input("Enter your selection: ")
    return result


def checked_input(menu: str, approved: list[str], name_key: str, values: dict):
    result = get_input(menu)
    if result in approved:
        values[name_key] = result
        print(f"New value for {name_key} set to {values[name_key]}")
    else:
        print(f"Invalid response for {name_key}, current value set to {values[name_key]}")


def line_plot_data():
    values = {
        "x_values": [],
        "y_values": [],
        "x_label": "",
        "y_label": "",
        "title": "",
        "marker_color": "black",
        "line_color": "blue",
        "marker_shape": "o",
        "line_style": "solid",
        "marker_size": 5
    }
    options = "Change:\n0: Go back\n1: x values\n2: y values\n3: Marker color\n4: Line color\n5: Marker shape" \
              "\n6: Line style\n7: Point size\n8: Plot title\n9: x-axis label\n10: y-axis label\n11: Plot data"
    line_style_text = "Line Styles: solid (-), dashed (--), dashdot (-.), dotted (:), none"
    line_style_options = ["solid", "dashed", "dashdot", "dotted", "none", "None", "-", "--", "-.", ":"]
    marker_style_text = "Marker Styles: point, pixel, circle, square, diamond, x, none, verts, star, triangle_up"
    marker_style_options = ["point", ".", "pixel", ",", "circle", "o", "square", "s", "x", "diamond", "D", "none",
                            "None", "verts", "star", "*", "triangle_up", "^"]
    colors_text = "Colors: black, gray, red, pink, orange, yellow, green, blue, purple"
    color_options = ["black", "gray", "red", "orange", "yellow", "green", "blue", "purple", "pink"]

    print(options)
    result = input("Enter your selection: ")
    while result != "0":
        if result == "3":
            checked_input(colors_text, color_options, "marker_color", values)
        elif result == "4":
            checked_input(colors_text, color_options, "line_color", values)
        elif result == "5":
            checked_input(marker_style_text, marker_style_options, "marker_shape", values)
        elif result == "6":
            checked_input(line_style_text, line_style_options, "line_style", values)
        elif result == "7":
            values["marker_size"] = float(input("Enter a new marker size: "))
            print(f"The new marker size is: {values['marker_size']}")
        elif result == "8":
            values["title"] = input("Enter a new plot title: ")
            print(f"The new plot title is: {values['title']}")
        elif result == "9":
            values["x_label"] = input("Enter a new x-axis label: ")
            print(f"The new x-axis label is {values['x_label']}")
        elif result == "10":
            values["y_label"] = input("Enter a new y-axis label: ")
            print(f"The new y-axis label is {values['y_label']}")
    return values


response = ""
table = None

while response != "0":
    response = get_input("Menu\n0: Exit\n1: Enter a table\n2: Select data\n3: Plot data\n4: Analyze data")
    print(response)
    if response == "1":
        name = input("Enter the path to the file")
        table = DataTable(name)
    elif response == "2":
        pass
    # Plot Data
    elif response == "3":
        response = get_input("Plot Data:\n0: Exit\n1: Line Plot\n2: Box Plot\n3: Scatter Plot\n4: Histogram")
    elif response == "4":
        pass
    else:
        print("Invalid Selection")

