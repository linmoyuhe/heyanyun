#!/usr/bin/env python3

import sys
print("program:", sys.argv[0])
print("Parameters: ")
for i, x in enumerate(sys.argv):
    if (i == 0):
          continue
    print(i, x)

