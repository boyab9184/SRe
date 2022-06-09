import calculations as cal
import parsing_file as pf

def create_dictionary_to_dump(file_path):

    df = pf.parsing_access_log(file_path)
    dictionary = {
        "Most frequent IP": cal.most_frequent_ip(df),
        "Least frequent IP": cal.least_frequent_ip(df),
        "Events per second": round(cal.events_per_second(df), 8),
        "Total amount of bytes exchanged": int(cal.total_bytes_exchanged(df))
    }

    return dictionary