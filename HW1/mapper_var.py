#!/usr/bin/python
import sys
import csv

if __name__ == "__main__":
    input = csv.reader(sys.stdin)
    for i in input:
        print(f"1 {i[9]} 0")
