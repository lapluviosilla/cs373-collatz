#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Paul Strong
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

# -------
# imports
# -------

import io
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycles

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = io.StringIO("1 10\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_2 (self) :
        r = io.StringIO("3245 1451\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  3245)
        self.assertTrue(j == 1451)

    def test_read_3 (self) :
        r = io.StringIO("820000 999999\n")
        m = collatz_read(r)
        i, j = list(next(m))
        self.assertTrue(i ==  820000)
        self.assertTrue(j == 999999)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)

    # -----
    # cycles
    # -----
    def test_cycles_1 (self) :
        v = collatz_cycles(4)
        self.assertTrue(v == 3)

    def test_cycles_2 (self) :
        v = collatz_cycles(3)
        self.assertTrue(v == 8)

    def test_cycles_3 (self) :
        v = collatz_cycles(18)
        self.assertTrue(v == 21)

    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print2 (self) :
        w = io.StringIO()
        collatz_print(w, 800000, 1000000, 45)
        self.assertTrue(w.getvalue() == "800000 1000000 45\n")

    def test_print3 (self) :
        w = io.StringIO()
        collatz_print(w, -5, 10, 45)
        self.assertTrue(w.getvalue() == "-5 10 45\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = io.StringIO("9 10\n1 20\n1 17\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "9 10 20\n1 20 21\n1 17 20\n")

    def test_solve3 (self) :
        r = io.StringIO("")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
