import os

def create_output_directory():
    parent_dir = os.getcwd()
    output_dir = "outputs/"
    output_path = os.path.join(parent_dir, output_dir)

    try:
        os.mkdir(output_path)
    except OSError:
        return output_path
    
    return output_path

