#!/usr/bin/env python3

import shutil
import glob
import re
import os
import getpass


folder_name_regex = "(\w+\s\w+)(\s\w+)?\s-\s\w+\s\d+\s-\s\d+\s-\s\d+\s\w+"
user_name = getpass.getuser()

for folder_name in glob.glob("/Users/{}/Downloads/*".format(user_name)):
    match = re.search(folder_name_regex, folder_name)
    if match is not None:
        for file_name in glob.glob("{}/**".format(folder_name), recursive=True):
            file_name = file_name.replace(folder_name, "")
            src = folder_name + file_name
            dst = "/Users/{}/Google Drive/{}{}".format(user_name, match.group(1), file_name)
            if not os.path.exists(dst):
                shutil.move(src, dst)
                print(dst)
