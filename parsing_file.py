import pandas as pd


def parsing_access_log(file_path):

    # check skip bad lines!!!!
    df = pd.read_csv(file_path, on_bad_lines='skip', sep = ' ').dropna(axis=1, how='all')

    # assign header columns
    headerList = ['Timestamp in seconds since the epoch', 'Response header size in bytes', 'Client IP address', 'HTTP response code', 'Response size in bytes', 'HTTP request method', 'URL', 'Username', 'Type of access/destination IP address', 'Response type']


    df.to_csv("data/access_test1.csv", header=headerList, index=False)

    df1 = pd.read_csv("data/access_test1.csv")


    return df1