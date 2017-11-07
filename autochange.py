import os
import sys

import time

# time execution script
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print ("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

with Profiler() as p:
    path = 'e:\\cdr\\'

    lsdirs = os.listdir(path)
    print(lsdirs)

    for files in lsdirs:
        with open(os.path.join(path, files)) as rfile:
            list = []
            for row in rfile.readlines():
                convert = row.replace(",", ";")
                list.append(convert)
        with open(os.path.join(path, files), "w") as wfile:
            wfile.writelines(list)