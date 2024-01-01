#!/usr/bin/env python3
import random

hail = []
with open('input.txt') as infile:
    lines = infile.readlines()
    for line in lines:
        parts = line.strip().split(' @ ')
        pos = tuple([int(n) for n in parts[0].split(', ')])
        vel = tuple([int(n) for n in parts[1].split(', ')])
        hail.append((pos, vel))

pairs = []
for i in range(len(hail) - 1):
    for j in range(i + 1, len(hail)):
        pairs.append((hail[i], hail[j]))

def collide(h1, h2):
    (x1, y1, z1) = h1[0]
    (vx1, vy1, vz1) = h1[1]
    (x2, y2, z2) = h2[0]
    (vx2, vy2, vz2) = h2[1]
    if vx1 == 0 or vx2 == 0:
        return None
    s1 = vy1 / vx1
    s2 = vy2 / vx2
    if s1 == s2:
        return None
    c1 = y1 - s1 * x1
    c2 = y2 - s2 * x2
    x = (c2 - c1) / (s1 - s2)
    t1 = (x - x1) / vx1
    t2 = (x - x2) / vx2
    if t1 < 0 or t2 < 0:
        return None
    y = s1 * (x - x1) + y1
    return(x, y, int(t1))

def update(hail, dvx, dvy):
    return (hail[0], (hail[1][0] + dvx, hail[1][1] + dvy, hail[1][2]))
     
def predict(hail, t, dvz):
    return hail[0][2] + t * (hail[1][2] + dvz)

def solve():
    while True:
        sel = random.choices(hail, k=4)
        for dvx in range(-500, 500):
            for dvy in range(-500, 500):
                hail0 = update(sel[0], dvx, dvy)
                c1 = collide(hail0, update(sel[1], dvx, dvy))
                c2 = collide(hail0, update(sel[2], dvx, dvy))
                c3 = collide(hail0, update(sel[3], dvx, dvy))
                if c1 and c2 and c3 and c1[0] == c2[0] and c2[0] == c3[0] and \
                    c1[1] == c2[1] and c2[1] == c3[1]:
                    for dvz in range(-500, 500):
                        z1 = predict(sel[1], c1[2], dvz)
                        z2 = predict(sel[2], c2[2], dvz)
                        z3 = predict(sel[3], c3[2], dvz)
                        if z1 == z2 and z2 == z3:
                            return c1[0] + c1[1] + z1

total = 0

minrange = 200000000000000
maxrange = 400000000000000
for p in pairs:
    pos = collide(p[0], p[1])
    if pos:
        if pos[0] >= minrange and pos[0] <= maxrange and \
            pos[1] >= minrange and pos[1] <= maxrange:
            total += 1
print(total)
print(solve())
