#!/usr/bin/python3
##################
# Author:Toshiki Hirao
# CreatedOn: 2016/01/26
# Summary: pick-san method
##################

### Import lib
import sys
import csv
import time
from collections import defaultdict

### Define dictionary structure
expertiseLineDict = defaultdict(lambda: [])

### Register expertise information into expertiseLineDict
for line in open(sys.argv[1], "r"):
    values = line.strip().split(",")
    expertiseLineDict[values[0]].append(values)
