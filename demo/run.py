import sys
import os
import time
from scrapy.cmdline import execute

b = time.time()
execute(["scrapy", "crawl", "example"])
e = time.time()
print("-------------------")
print(str(e-b))
