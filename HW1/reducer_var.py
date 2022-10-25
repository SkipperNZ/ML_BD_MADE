#!/usr/bin/python
import sys


def main() -> None:
    mj, cj, vj = None, None, None

    for i in sys.stdin:

        i = i.strip()
        try:
            ck, mk, vk = map(float, i.split(' '))
        except ValueError:
            continue

        if mj is None or cj is None:
            mj, cj, vj = mk, ck, vk
        else:
            mi = (cj * mj + ck * mk) / (cj + ck)
            vi = ((cj * vj + ck * vk) / (cj + ck)) + cj * ck * ((mj - mk) / (cj + ck)) ** 2
            ci = ck + cj
            print(f"{ci} {mi} {vi}")
            mj = mi
            cj = ci
            vj = vi


if __name__ == "__main__":
    main()

