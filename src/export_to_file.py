import os
import utils

def export_to_file(user_input):

    input_list = user_input.split(" ")
    for item in input_list:
        if os.path.isfile(item):
            file_name = os.path.split(item)[-1]
            output_dir = utils.write_to_file(item, file_name)
        elif os.path.isdir(item):
            for filename in os.listdir(item):
                f = os.path.join(item, filename)
                if os.path.isfile(f):
                    output_dir = utils.write_to_file(f, filename)
        else:
            print("Incorrect filename or directory!")
            return
    # all results in /outputs dir
    return output_dir