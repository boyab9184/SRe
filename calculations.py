
def total_bytes_exchanged(df):
    return df['Response header size in bytes'].sum() + df['Response size in bytes'].sum()

def most_frequent_ip(df):
    return df['Client IP address'].value_counts().idxmax()

def least_frequent_ip(df):
    return df['Client IP address'].value_counts().idxmin()


def events_per_second(df):

    # try catch deleting by zero
    events_per_second = df['Timestamp in seconds since the epoch'].count() / (df['Timestamp in seconds since the epoch'].max() - df['Timestamp in seconds since the epoch'].min())
    return round(events_per_second, 2)
