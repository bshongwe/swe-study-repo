#!/usr/bin/env python3


import sys
from collections import deque


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    infile = sys.argv[1] if len(sys.argv) >= 2 else 'input_file.csv'

    # Read the garden grid
    G = open(infile).read().strip().split('\n')
    R, C = len(G), len(G[0])

    SEEN = set()
    p1 = 0

    for r in range(R):
        for c in range(C):
            if (r, c) in SEEN:
                continue

            # BFS initialization
            Q = deque([(r, c)])
            area = 0
            perimeter = 0

            while Q:
                r2, c2 = Q.popleft()
                if (r2, c2) in SEEN:
                    continue
                SEEN.add((r2, c2))
                area += 1

                # Check all 4 neighbours
                for dr, dc in DIRS:
                    rr, cc = r2 + dr, c2 + dc
                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r2][c2]:
                        Q.append((rr, cc))
                    else:
                        perimeter += 1

            # Update total price
            p1 += area * perimeter

    print(p1)


if __name__ == '__main__':
    main()