from cgitb import handler
from exiftool import ExifToolHelper as exif
import argparse

parser = argparse.ArgumentParser(description='Use this tool to \
                                process image exif information.')
# for positional arguments.
parser.add_argument('Image Path', metavar='Path', type=str,
                    nargs='?', help='Path of the single image', default=None)
# for options.
parser.add_argument('-i', '--info', action='store',
                    help='List selected info. * for all info.')
parser.add_argument('-a', '--add_info', action='store',
                    help='Add selected info.')
parser.add_argument('-d', '--del_info', action='store',
                    help='Remove selected info.')

parsed_args = parser.parse_args()
print(parsed_args)
