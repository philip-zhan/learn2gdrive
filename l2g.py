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
        new_folder_name = match.group(1)
        files_in_gdrive = []
        for file_in_gdrive in glob.iglob(
                "/Users/{}/Google Drive/{}/**".format(user_name, new_folder_name),
                recursive=True):
            if os.path.isfile(file_in_gdrive):
                files_in_gdrive.append(file_in_gdrive[file_in_gdrive.rindex('/'):])

        for file_in_download in glob.glob("{}/**".format(folder_name), recursive=True):
            file_in_download = file_in_download.replace(folder_name, "")
            src = folder_name + file_in_download
            dst = "/Users/{}/Google Drive/{}{}".format(user_name, new_folder_name, file_in_download)
            if (file_in_download != "/Table of Contents.html") \
                    and (file_in_download not in files_in_gdrive) \
                    and (not os.path.exists(dst)):
                shutil.move(src, dst)
                print(file_in_download)
