import numpy as np

file = open("input.txt")


def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))


curr = (0,0)
points = 0
edges = dict()
dirs = {"U": (0, -1), "D": (0, 1), "R": (1, 0), "L": (-1, 0)}
dir_arr = ["R", "D", "L", "U"]
xs = []
ys = []
for line in file:
    _, _, color = line.strip().split()
    dist = int(color[2:7], 16)
    dir_ = dir_arr[int(color[-2])]
    curr_dir = dirs[dir_]
    points += dist
    curr = (curr[0] + int(dist) * curr_dir[0], curr[1] + int(dist) * curr_dir[1])
    xs.append(curr[0])
    ys.append(curr[1])

print(PolyArea(xs, ys) - points / 2 + 1 + points)