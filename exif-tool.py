from cgitb import handler
from exiftool import ExifToolHelper #type:ignore
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(description='Use this tool to \
                                    process image exif information.')
    # for positional arguments.
    parser.add_argument('Image Path', metavar='Path', type=str,
                        help='Path of the single image')
    # for options.
    parser.add_argument('-i', '--info', action='store',
                        help='List selected info. "all" for all info.')
    parser.add_argument('-a', '--add-info', action='store',
                        help='Add selected info.')
    parser.add_argument('-d', '--del-info', action='store',
                        help='Remove selected info.')
    parser.add_argument('-o','--original-info',action='store_true',help="See unformatted original\
                        information given by the pyExifTool Library")
    # originally args come with a Namespace, using vars() to change them into a dict. 
    parsed_args = vars(parser.parse_args())
    return parsed_args


def exif_process(args):
    # Info_flag is for showing formatted info when no parameter is specified.
    info_flag = True
    print(args) # Test Purposes.
    # Show detailed info. Do when flag is True or specified in arg with --info all. 
    if args["original-info"] is True:
        try:
            with ExifToolHelper() as exif:
                metadata = exif.get_metadata(args["Image Path"])
                # A dirty workaround to change metadata from (a dict inside) a list to a stand along dict
                metadata = metadata.pop(0)
                print(metadata,'\n')
        except:
            print("The file is not reachable.")

    # Copying codes from the first "if" straightaway. 
    if info_flag is True or args["info"] == "all":
        try:
            with ExifToolHelper() as exif:
                metadata = exif.get_metadata(args["Image Path"])
                metadata = metadata.pop(0)
                for key_entry in metadata.keys():
                    print(f"{key_entry} --- {metadata[key_entry]}")
        except:
            print("The file is not reachable.")
def info_collector():
    entry_info = str(input("Enter the new value for this key: "))
    return entry_info




if __name__ == "__main__":
    parsed_args = get_args()
    exif_process(parsed_args)
