import json
import calculations as cal
import parsing_file as pf


def create_dictionary_to_dump(path_file):

    df = pf.parsing_access_log(path_file)

    dictionary = {
        "Most frequent IP": cal.most_frequent_ip(df),
        "Least frequent IP": cal.least_frequent_ip(df),
        "Events per second": cal.events_per_second(df),
        "Total amount of bytes exchanged": int(cal.total_bytes_exchanged(df))
    }

    return dictionary


def export_to_file(path_file):

    operations_dict = create_dictionary_to_dump(path_file)

    json_object = json.dumps(operations_dict, indent = len(operations_dict))

    file_path = "data/output.json"
    with open(file_path, "w") as outfile:
        outfile.write(json_object)

    return file_path

