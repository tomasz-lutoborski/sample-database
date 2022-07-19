import json
import csv
import sqlite3

from flask import jsonify


# create a function that convert a csv file to json file
def csv_to_json(csv_file, json_file):
    # open the csv file
    with open(csv_file, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data = []
        # loop through the csv reader
        for line in csv_reader:
            # append the data to the list
            data.append(line)

        with open(json_file, 'w') as json_file:
            # create a json writer
            json_writer = json.dump(data, json_file)
            # return the json writer
            return json_writer

# create function that convert a json file to list


def json_to_list(json_file):
    # open the json file
    with open(json_file, 'r') as json_file:
        # load the json file
        data = json.load(json_file)
        # return the data
        return data


print(json_to_list('data.json')[0])

# con = sqlite3.connect('data.db')
# cur = con.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS data
#             (country TEXT PRIMARY KEY,
