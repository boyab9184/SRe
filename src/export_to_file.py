import os
import json
import utils
from create_dictionary_to_dump import create_dictionary_to_dump


def export_to_file(user_input):

    input_list = user_input.split(" ")
    for item in input_list:
        if os.path.isfile(item):
            file_name = os.path.split(item)[-1]
            operations_dict = create_dictionary_to_dump(item)
            json_object = json.dumps(operations_dict, indent=len(operations_dict))

            output_dir = utils.create_output_directory()

            output_path = output_dir + file_name.split(".")[0] + ".json"
            with open(output_path, "w") as outfile:
                outfile.write(json_object)

        elif os.path.isdir(item):
            for filename in os.listdir(item):
                f = os.path.join(item, filename)
                if os.path.isfile(f):
                    operations_dict = create_dictionary_to_dump(f)
                    json_object = json.dumps(operations_dict, indent=len(operations_dict))

                    output_dir = utils.create_output_directory()
                    output_path = output_dir + filename.split(".")[0] + ".json"
                    with open(output_path, "w") as outfile:
                        outfile.write(json_object)
        else:
            print("Incorrect filename or directory. Please Enter again")
            return
    # all results in /outputs dir
    return output_dir
