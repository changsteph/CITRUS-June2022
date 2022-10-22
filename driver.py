import pandas as pd
import clean_data as clean


class DataTable:
    def __init__(self, file_name):
        self.table = pd.read_csv(file_name, index_col=0)


def get_input(menu: str):
    print(menu)
    result = input("Enter your selection: ")
    return result


def line_plot_data():
    values = {
        "point_color": "black",
        "line_color": "blue",
        "point_shape": "o",
        "line_style": "solid",

    }
    options = "Change:\n0: Go back\n1: x values\n2: y values\n3: Point color\n4: Line color\n5: Point shape" \
              "\n6: Line style\n7: Point size\n8: Plot title\n9: y-axis name\n10: x-axis name\n11: Plot data"
    line_color_options = ""
    line_style_text = "solid (-), dashed (--), dashdot (-.), dotted (:), none"
    line_style_options = ["solid", "dashed", "dashdot", "dotted", "none", "None", "-", "--", "-.", ":"]
    print(options)
    result = input("Enter your selection: ")
    while result != "0":
        if result == "6":
            print("Select one of the line types: ", line_style_text)
            result = input("Enter your selection: ")
            if result in line_style_options:
                values["line_style"] = result
            else:
                print("Invalid option, line style currently set to: ", values["line_style"])
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

