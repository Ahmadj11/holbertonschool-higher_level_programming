#!/usr/bin/python3
""" Returning the json format of a string """

import json


def to_json_string(my_obj):
    """ prototype to return json format"""
    return json.dumps(my_obj)