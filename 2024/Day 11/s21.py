from typing import *

STONES : List[str] = [i for i in open(r"2024/Day 11/d11.txt").read().split(" ")] # input

for blink in range(25):
    print(f"{blink + 1} / 25")
    new_stones : List[str] = [] # stones after blink
    for stone in STONES:
        if stone == "0": # 0 => 1
            new_stones.append("1")
        elif len(stone) % 2 == 0: # split into two
            a, b = stone[:len(stone) // 2], stone[len(stone) // 2:]
            new_stones.append(str(int(a)))
            new_stones.append(str(int(b)))
        else: # no rules: multiply by 2024
            new_stones.append(str(int(stone) * 2024))
    STONES = new_stones # superceed

print(len(STONES))

# naieve solution: brute force
# O(p^n), idk what exactly tho