import os
import json
import utils
import create_dictionary_to_dump as dtd

def export_to_file(file_path):

    # assuming all data files are in one dir
    for filename in os.listdir(file_path):
        f = os.path.join(file_path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            operations_dict = dtd.create_dictionary_to_dump(f)
            json_object = json.dumps(operations_dict, indent = len(operations_dict))

            output_dir =  str (utils.create_output_directory())
            output_path = output_dir + filename.split(".")[0] + ".json"
            with open(output_path, "w") as outfile:
                outfile.write(json_object)

    #all results in /outputs dir
    return output_dir

