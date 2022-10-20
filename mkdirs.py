import os
import glob
import os

dirs = glob.glob("*")
for dir in dirs:
    if dir != "mkdirs.py" and dir != "docAssets" and dir != "README.md":
        if not os.path.isfile(dir + "/test." + dir):
            with open(dir + "/test." + dir, "w") as file:
                file.write("")