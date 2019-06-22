import os, sys
import shutil
from datetime import date

def parse_terminal_args():

    if "backup" in sys.argv:
        create_backup()
    else:
        price, item, category = sys.argv[1:]
        today = date.today().strftime("%d/%m/%Y") # dd/mm/YY
        data = "{}, {}, {}, {}".format(price, item, category, today)
        write_to_file(data)


def write_to_file(data):
    check_if_file_exists_helper()
    print(data)
    file = open("./data.csv", "a")
    file.write("\n{}\n".format(data))
    file.close()


def get_last_update_date():
    os.path.getmtime("./data.csv")


def create_backup():
    shutil.copy2("./data.csv", "./dataBackup.csv")


def check_if_file_exists_helper():
    if not os.path.isfile("./data.csv"):
        file = open("data.csv", "w")
        file.write("Price, Item, Category, Date")
        file.close()


if __name__ == '__main__':
    parse_terminal_args()
