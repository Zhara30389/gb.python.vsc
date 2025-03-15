import json
import csv
import pickle

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)