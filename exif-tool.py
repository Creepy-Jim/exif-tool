from cgitb import handler
from exiftool import ExifToolHelper
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
                        help='List selected info. * for all info.')
    parser.add_argument('-a', '--add_info', action='store',
                        help='Add selected info.')
    parser.add_argument('-d', '--del_info', action='store',
                        help='Remove selected info.')
    parsed_args = vars(parser.parse_args())
    return parsed_args


def exif_process(args):
    try:
        with ExifToolHelper() as exif:
            metadata = exif.get_metadata([args["Image Path"]])
            print(metadata)
    except IOError:
        print(os.getcwd())
        print("The file is not reachable.")


if __name__ == "__main__":
    parsed_args = get_args()
    print(parsed_args)
    exif_process(parsed_args)