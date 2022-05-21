#!/usr/bin/python3
"""
    adding arguments to a list, as well as saving them in JSON format.
"""
import sys
save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

FORM = "add_item.json"

try:
    my_list = load_json(FORM)
except (FileNotFoundError, TypeError):
    my_list = []

for a in sys.argv[1:]:
    my_list.append(a)

save_json(my_list, FORM)