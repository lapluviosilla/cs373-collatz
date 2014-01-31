#!/usr/bin/env python3

# ------------------------------
# projects/collatz/CollatzTestGenerator.py
# Copyright (C) 2014
# Paul Strong
# -------------------------------

import random

from Collatz import collatz_eval, collatz_print

in_file = open('pstrong-RunCollatz.in', 'w')
out_file = open('pstrong-RunCollatz.out', 'w')

for b in range(1, 1001) :
    start =  b * random.randint(1, 999)
    end = abs(start + random.randint(-2000, 2000))
    v = collatz_eval(start, end)
    in_file.write(str(start) + " " + str(end) + "\n")
    collatz_print(out_file, start, end, v)

in_file.close()
out_file.close()