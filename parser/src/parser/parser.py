# Here we are, the parser
import network, machine, plugins
import yaml

import sys

def parse(file: str):

    try:
        with (open(file, "r") as f):
            parsed = yaml.safe_load(f)
    except FileNotFoundError:
        print("Couldn't load", file, ": file not found")
        exit(1)
    except IsADirectoryError:
        print("Couldn't load", file, ": is a directory")
        exit(1)


                

parse(sys.argv[1])