import pandas as pd
import clean_data as clean


class DataTable:
    def __init__(self, file_name):
        self.table = pd.read_csv(file_name, index_col=0)


def show_menu():
    print("Menu\n0: Exit\n1: Enter a table\n2: Select data")
    result = input("Enter your selection: ")
    return result


response = ""
table = None

while response != "0":
    response = show_menu()
    print(response)
    if response == "1":
        name = input("Enter the path to the file")
        table = DataTable(name)





