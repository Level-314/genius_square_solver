# -*- coding: utf-8 -*-
"""
    ----
 -----------
- Level 314 -
 -----------
    ----

@author: Alexander Williams
date: Wed Nov 20 21:04:38 2019

Genuis Square game counter
"""

count = 0
peg = [0] * 7
N = 36

for peg[0] in range(N - 6):
    for peg[1] in range(peg[0] + 1, N - 5):
        for peg[2] in range(peg[1] + 1, N - 4):
            for peg[3] in range(peg[2] + 1, N - 3):
                for peg[4] in range(peg[3] + 1, N - 2):
                    for peg[5] in range(peg[4] + 1, N - 1):
                        for peg[6] in range(peg[5] + 1, N):
                            count += 1 # equivalent count = count + 1

print("Game count: {:,}".format(count))
