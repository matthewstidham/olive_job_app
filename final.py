#!/usr/bin/python3

import datetime
import random
import string
import pandas as pd
import os

letters = string.ascii_letters
patients = [''.join(random.choice(letters) for _ in range(random.randint(0, 10))) for _ in range(0, 1000)]


# Generate input CSV files of random data
def generate_random_csv():
    data = list()
    for x in range(0, 100):
        patient = random.choice(patients)
        description = ''.join(random.choice(letters) for _ in range(random.randint(1, 20)))
        timestamp = datetime.datetime.now()
        data.append([patient, description, timestamp])
    df = pd.DataFrame(data)
    df.columns = ['id', 'description', 'timestamp']
    unique_name = ''.join(random.choice(letters) for _ in range(random.randint(10, 20)))
    # noinspection PyTypeChecker
    df.to_csv("input/%s.csv" % unique_name, index=False)
    return df


def read_data():
    files = os.listdir('input')
    dfs = [pd.read_csv('input/' + file) for file in files]
    for file, df in zip(files, dfs):
        df['source_filename'] = file
    df = pd.concat(dfs).reset_index(drop=True)
    final = df.sort_values('timestamp').drop_duplicates('id', keep='last')
    final.to_csv('output/id_descriptions.csv')
    return final


def main():
    [generate_random_csv() for _ in range(0, 100)]
    read_data()


if __name__ == "__main__":
    main()
