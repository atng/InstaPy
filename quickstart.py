""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

import json
# set workspace folder at desired location (default is at your home folder)
# set_workspace(path="./")

# get an InstaPy session!

insta_username = "footnootes"
insta_password = 'roundTngable'

# get a session!
session = InstaPy(username=insta_username, password=insta_password)
# headless_browser=True,
# multi_logs=True)

seed_username = "ohsofickle"
min_followers = 700
max_followers = 8000


def get_followers_recursive(full_username_list, username, min_followers,
                            max_followers):
    print(f"Session Start for {username}")
    followers = session.grab_followers(username=username, amount="full")
    existing_username_list = [d['username'] for d in full_username_list]
    for follower in followers:
        if follower not in existing_username_list:
            followers_num = session.get_follower_num(username=follower)
            if followers_num > min_followers and followers_num < max_followers:
                full_username_list = get_followers_recursive(
                    full_username_list, follower, min_followers, max_followers)
                print(f"[APPENDING] {follower}")
                full_username_list.append({
                    "username": follower,
                    "followers": followers_num
                })
        else:
            print(f"[USER SKIPPED] {follower}")

    return full_username_list


full_username_list = []
with open('data.txt', 'r') as json_file:
    try:
        full_username_list = json.load(json_file)["data"]
    except:
        print("[SKIP] Initial Username Data Load")

    with smart_run(session):
        # general settings
        # session.set_dont_include(["friend1", "friend2", "friend3"])

        # activity
        get_followers_recursive(full_username_list, seed_username,
                                min_followers, max_followers)

with open('data.txt', 'w') as json_file:
    json.dump({"data": full_username_list}, json_file)
