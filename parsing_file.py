from numpy import dtype
import pandas as pd


def parsing_access_log(file_path):

    # assign header columns
    header_list = ['Timestamp in seconds since the epoch', '1', '2', 'Response header size in bytes', 'Client IP address', 'HTTP response code', 'Response size in bytes', 'HTTP request method', 'URL', 'Username', 'Type of access/destination IP address', 'Response type']

    dtype_dict = {
        0: float,
        3: str,
        4: str,
        5: str,
        6: str,
        7: str,
        8: str,
        9: str,
        10: str,
        11: str
    }

    df = pd.read_csv(file_path, sep=' ', names=header_list,  on_bad_lines='skip', dtype=dtype_dict).drop(axis=1, columns=['1','2']).dropna()

    df['Response header size in bytes'] = df['Response header size in bytes'].astype(int)
    df['Response size in bytes'] = df['Response size in bytes'].astype(int)

    
    return df