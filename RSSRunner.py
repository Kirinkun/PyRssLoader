import time
import os

from settings import timeout

while True:
    os.system('python2 RSSLoader.py')
    time.sleep(timeout)
