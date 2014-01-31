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
    start = min(i, j)
    end = max(i, j)
    max_cycle_length = 1
    for n in range(start, end+1) :
        cycles = collatz_cycles(n)
        if cycles > max_cycle_length: max_cycle_length = cycles 
    assert(max_cycle_length > 0)
    return max_cycle_length

# -------------
# collatz_cycles
# -------------
def collatz_cycles (num) :
    assert(num > 0)
    assert(num < 1000000)
    cycles = 1
    while(num != 1) :
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1
        cycles += 1
    assert(cycles > 0)
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
