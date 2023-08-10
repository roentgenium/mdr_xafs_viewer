import shutil, pathlib
import json

def find_raw_data(filename):
    dir_name = pathlib.Path(filename).stem
    shutil.unpack_archive(filename, dir_name)

    fname = pathlib.Path(dir_name + "/" + "metadata.all.json" )

    with open(fname, encoding = 'utf-8') as f:
        metadata = json.load(f)
        return  dir_name, metadata["local"]["xafs_filename_list"]

if __name__ == "__main__":
    find_raw_data("c247dv91k.zip")



