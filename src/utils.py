import os
import json
from create_dictionary_to_dump import create_dictionary_to_dump

def create_output_directory():
    parent_dir = os.getcwd()
    output_dir = "outputs/"
    output_path = os.path.join(parent_dir, output_dir)

    try:
        os.mkdir(output_path)
    except OSError:
        return output_path
    
    return output_path


def write_to_file(f, filename):
    operations_dict = create_dictionary_to_dump(f)
    json_object = json.dumps(operations_dict, indent=len(operations_dict))
    output_dir = create_output_directory()
    output_path = output_dir + filename.split(".")[0] + ".json"
    with open(output_path, "w") as outfile:
        outfile.write(json_object)

    return output_dir