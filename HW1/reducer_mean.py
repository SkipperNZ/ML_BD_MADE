#!/usr/bin/python
import sys


def main() -> None:
    mj, cj = None, None

    for i in sys.stdin:
        i = i.strip()
        try:
            ck, mk = map(float, i.split(" "))
        except ValueError:
            continue

        if mj is None or cj is None:
            mj, cj = mk, ck
        else:
            mi = (cj * mj + ck * mk) / (cj + ck)
            ci = ck + cj
            print(f"{ci} {mi}")
            mj = mi
            cj = ci


if __name__ == "__main__":
    main()
