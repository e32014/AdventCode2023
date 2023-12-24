import itertools as it
from fractions import Fraction

file = open('input.txt')

bounds = (7, 27)
vectors = []
for line in file:
    start, vel = line.strip().split("@")
    vectors.append(([int(i) for i in start.strip().split(", ")], [int(i) for i in vel.strip().split(", ")]))

pot_x = set(range(-1000, 1001))
pot_y = set(range(-1000, 1001))
pot_z = set(range(-1000, 1001))

for v1, v2 in it.combinations(vectors, 2):
    (x1, y1, z1), (dx1, dy1, dz1) = v1
    (x2, y2, z2), (dx2, dy2, dz2) = v2

    if dx1 == dx2:
        new_x = set()
        dist = x2 - x1
        for v in range(-1000, 1001):
            if v == dx1:
                continue
            if dist % (v - dx1) == 0:
                new_x.add(v)
        pot_x = pot_x & new_x
    if dy1 == dy2:
        new_y = set()
        dist = y2 - y1
        for v in range(-1000, 1001):
            if v == dy1:
                continue
            if dist % (v - dy1) == 0:
                new_y.add(v)
        pot_y = pot_y & new_y
    if dz1 == dz2:
        new_z = set()
        dist = z2 - z1
        for v in range(-1000, 1001):
            if v == dz1:
                continue
            if dist % (v - dz1) == 0:
                new_z.add(v)
        pot_z = pot_z & new_z

r_dx, r_dy, r_dz = pot_x.pop(), pot_y.pop(), pot_z.pop()
(x1, y1, z1), (dx1, dy1, dz1) = vectors[0]
(x2, y2, z2), (dx2, dy2, dz2) = vectors[1]
slope_1 = Fraction(dy1 - r_dy, dx1 - r_dx)
slope_2 = Fraction(dy2 - r_dy, dx2 - r_dx)
inter_1 = y1 - (slope_1 * x1)
inter_2 = y2 - (slope_2 * x2)
r_x = Fraction(inter_2 - inter_1, slope_1 - slope_2)
r_y = slope_1 * r_x + inter_1
time = Fraction(r_x - x1, dx1 - r_dx)
r_z = z1 + (dz1 - r_dz) * time
print(r_x, r_y, r_z)
print(r_x + r_y + r_z)