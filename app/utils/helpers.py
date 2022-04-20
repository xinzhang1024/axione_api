
import os
import csv
import json

from config import ROOT_PATH


def load_json_file(file_path, file_name):
    path = os.path.join(os.path.join(ROOT_PATH, file_path), f'{file_name}.json')
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def load_csv_file(file_path, file_name):
    path = os.path.join(os.path.join(ROOT_PATH, file_path), f'{file_name}.csv')
    data = []
    with open(path, encoding='ISO-8859-1') as file:
        reader = csv.reader(file)
        for line in reader:
            data.append(line)
    return data
