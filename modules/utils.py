import csv
import json


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


def without_keys(dict, keys):
    return {x: dict[x] for x in dict if x not in keys}


def reformat_data_entry(data):
    data = without_keys(data, ['Country Code', 'Country Name', 'Series Name', 'Series Code'])
    return_data = {}
    for key, value in data.items():
        new_key = key.split()[0]
        return_data[new_key] = data[key]
    return return_data


def transform_data(data):
    '''transform data to a list of dictionaries each containing a country's data'''
    data_per_country = {}

    for data_entry in data:
        country = data_entry['Country Name']
        if country not in data_per_country:
            data_per_country[country] = {}
        data_per_country[country][data_entry['Series Name']] = reformat_data_entry(data_entry)

    return data_per_country
