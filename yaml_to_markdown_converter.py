#!/usr/bin/env python3

# currently only converts to raw text, will be modified to convert to markdown in the future

import requests, yaml

# Figoure out `Loader`, since plain calls are deprecated
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



url = "https://raw.githubusercontent.com/JarrodWoodard/TezMap/main/tezmap.yaml"
r = requests.get(url)
parsedData = yaml.load(r.content, Loader=Loader)

def print_data(parsed_data, indent_level=0):
    for key in parsed_data:
        val = parsed_data[key]
        if val==None:
            continue #do nothing
        else:
            if isinstance(val, dict):
                print("\t"*indent_level + key + "\n")
                print_data(val, indent_level+1)
            elif isinstance(val, list):
                print("\t"*indent_level + key + str(val) + "\n")
            else:
                print("\t"*indent_level + key + ": " + str(val) + "\n")
            

print_data(parsedData)
