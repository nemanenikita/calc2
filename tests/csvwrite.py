import pandas as pd


def csvwriter(input_df):
    """takes in a df from history and output to a csv file"""
    input_df.to_csv('tests/output_csv_files/output2.csv', mode='a', index=False, header=False)