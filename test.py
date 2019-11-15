""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

import json


full_username_list = {"data": []}
with open('data.txt', 'r') as json_file:
    print('full_username_list', full_username_list)
    print('full_username_list["data"]', full_username_list["data"])
    try:
        full_username_list = json.load(json_file)
    except:
        print("[SKIP] Initial Username Data Load")

    print('full_username_list', full_username_list)
    print('full_username_list["data"]', full_username_list["data"])

    existing_username_list = [d['username']
                              for d in full_username_list["data"]]

    # print(existing_username_list)
