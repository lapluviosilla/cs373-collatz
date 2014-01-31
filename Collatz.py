#!/usr/bin/env python3

# ----------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Paul Strong
# ----------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    r is a reader
    returns a generator over a list of ints of length 2
    """
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert(i > 0)
    assert(j > 0)
    # <your code>
    v = 1
    assert(v > 0)
    return v

# -------------
# collatz_cycles
# -------------
def collatz_cycles (num) :
    assert(num > 0)
    cycles = 1
    while(num != 1) :
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1
        cycles += 1
    return cycles


# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    v is the max cycle length
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    for m in collatz_read(r) :
        i, j = list(m)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
