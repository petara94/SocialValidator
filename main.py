from src import SocialChecker
import json
import time
import csv


def LoadConfig():
    try:
        with open("config.json", "r") as f:
            global CONFIGS
            CONFIGS = json.load(f)
    except FileNotFoundError:
        print("Config file not file")
        exit()

def LoadDataBase():
    try:
        with open(CONFIGS["load"]["dirpath"] + CONFIGS["load"]["filename"], "r", newline="") as f:
            global BASE
            global RESULT

            BASE = []
            _r = csv.reader(f)
            for row in _r:
                BASE.append(row)
            
            RESULT = [[]*len(BASE)]
            RESULT[0] = BASE[0]

    except FileNotFoundError:
        print("Database file not file")
        exit()


def ParseColumns():
    global COLUMNS
    COLUMNS = dict()

    for i, val in enumerate(BASE[0]):
        COLUMNS[str(i)] = str(val)


def ParseLine(line, index):
    for i, val in enumerate(line):
        if str(i) in COLUMNS.keys():
            pass
        else:
            RESULT[index][i] = val


def main(url):
    LoadConfig()
    LoadDataBase()
    ParseColumns()




if __name__ == "__main__":
    main(input())
