import os
import re

import step

list = os.listdir(".")
for i in list:
    if i.endswith(".dat"):
        stage = step.parseSteps(i.replace(".dat", ""))
        files = [re.sub(".*?\\\\", "", s.imageName) for s in stage.steps if s.imageName is not None]
        dir = stage.name
        print(files)
        print(dir)
        allFiles = os.listdir(dir + "\\")
        for f in allFiles:
            if f not in files:
                os.remove(dir + "\\" + f)