#!/usr/bin/env python3

import shutil
import glob
import re

pattern = "(\w+\s\w+)(\s\w+)?\s-\s\w+\s\d+\s-\s\d+\s-\s\d+\s\w+"
for name in glob.glob(r"/Users/philipzhan/Downloads/*"):
    m = re.search(pattern, name)
    if m is not None:

        print(m.group(1))


