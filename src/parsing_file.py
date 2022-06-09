from numpy import float64, int64
import pandas as pd

def parsing_access_log(file_path):

    # assign header columns
    header_list = ['Timestamp in seconds since the epoch', 'Response header size in bytes', 'Client IP address', 'HTTP response code', 
                    'Response size in bytes', 'HTTP request method', 'URL', 'Username', 'Type of access/destination IP address', 'Response type']

    dtype_dict = {
        'Timestamp in seconds since the epoch': "float64",
        "Response header size in bytes": "int",
        'Client IP address': "string",
        'HTTP response code': "string",
        'Response size in bytes': "int",
        'HTTP request method': "string",
        'URL': "string",
        'Username': "string",
        'Type of access/destination IP address': "string",
        'Response type': "string"
    }

    df = pd.read_csv(file_path, sep="\s+|   | ", names=header_list,  on_bad_lines='skip', dtype=dtype_dict, engine='python')

  
    return df

