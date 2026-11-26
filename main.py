#!/usr/bin/env python3
"""Midnight Set — entry for Midnight Fridge Roast on make.fun.

Prints exactly one line roasting a fridge at midnight.
"""

LINE = "It is midnight and my fridge is doing stand-up again: bright lights, cold audience, and leftovers older than the warranty."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
