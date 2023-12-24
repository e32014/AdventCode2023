from sympy import Symbol, solve_poly_system

file = open('input.txt')

bounds = (7, 27)
vectors = []
for line in file:
    start, vel = line.strip().split("@")
    vectors.append(([int(i) for i in start.strip().split(", ")], [int(i) for i in vel.strip().split(", ")]))

count = 0
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
dx = Symbol('dx')
dy = Symbol('dy')
dz = Symbol('dz')
equations = []
t_syms = []
for i in range(3):
    (x1, y1, z1), (dx1, dy1, dz1) = vectors[i]
    t = Symbol(f"t{i}")
    t_syms.append(t)
    equations.append(x + dx * t - x1 - dx1 * t)
    equations.append(y + dy * t - y1 - dy1 * t)
    equations.append(z + dz * t - z1 - dz1 * t)

result = solve_poly_system(equations, *([x, y, z, dx, dy, dz] + t_syms))
print(result)
print(result[0][0] + result[0][1] + result[0][2])