import heapq

file = open("input.txt")

graph = []
for line in file:
    graph.append([int(i) for i in line.strip()])

visited = dict()

heap = [(0, (0, 0, 0, -1))]

while heap:
    curr_score, (curr_x, curr_y, same_dirs, dir) = heapq.heappop(heap)
    if (curr_x, curr_y, same_dirs, dir) in visited:
        continue
    print((curr_x, curr_y, same_dirs), curr_score)
    visited[(curr_x, curr_y, same_dirs, dir)] = curr_score
    if curr_x == len(graph[0]) - 1 and curr_y == len(graph) - 1:
        print(curr_score + graph[curr_y][curr_x])
        break
    if dir == -1:
        if curr_x - 1 >= 0 and (curr_x - 1, curr_y) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y][curr_x - 1], (curr_x - 1, curr_y, same_dirs + 1, 2)))
        if curr_x + 1 < len(graph[0]) and (curr_x + 1, curr_y) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y][curr_x + 1], (curr_x + 1, curr_y, same_dirs + 1, 0)))
        if curr_y - 1 >= 0 and (curr_x, curr_y - 1) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y - 1][curr_x], (curr_x, curr_y - 1, same_dirs + 1, 3)))
        if curr_y + 1 < len(graph) and (curr_x, curr_y + 1) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y + 1][curr_x], (curr_x, curr_y + 1, same_dirs + 1, 1)))
    if dir == 0:
        if curr_x + 1 < len(graph[0]) and same_dirs < 10 and (curr_x + 1, curr_y) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y][curr_x + 1], (curr_x + 1, curr_y, same_dirs + 1, 0)))
        if curr_y - 1 >= 0 and same_dirs >= 4 and (curr_x, curr_y - 1) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y - 1][curr_x], (curr_x, curr_y - 1, 1, 3)))
        if curr_y + 1 < len(graph) and same_dirs >= 4 and (curr_x, curr_y + 1) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y + 1][curr_x], (curr_x, curr_y + 1, 1, 1)))
    if dir == 1:
        if curr_x - 1 >= 0 and same_dirs >= 4 and (curr_x - 1, curr_y) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y][curr_x - 1], (curr_x - 1, curr_y, 1, 2)))
        if curr_x + 1 < len(graph[0]) and same_dirs >= 4 and (curr_x + 1, curr_y) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y][curr_x + 1], (curr_x + 1, curr_y, 1, 0)))
        if curr_y + 1 < len(graph) and same_dirs < 10 and (curr_x, curr_y + 1) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y + 1][curr_x], (curr_x, curr_y + 1, same_dirs + 1, 1)))
    if dir == 2:
        if curr_x - 1 >= 0 and same_dirs < 10 and (curr_x - 1, curr_y) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y][curr_x - 1], (curr_x - 1, curr_y, same_dirs + 1, 2)))
        if curr_y - 1 >= 0 and same_dirs >= 4 and (curr_x, curr_y - 1) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y - 1][curr_x], (curr_x, curr_y - 1, 1, 3)))
        if curr_y + 1 < len(graph) and same_dirs >= 4 and (curr_x, curr_y + 1) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y + 1][curr_x], (curr_x, curr_y + 1, 1, 1)))
    if dir == 3:
        if curr_x - 1 >= 0 and same_dirs >= 4 and (curr_x - 1, curr_y) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y][curr_x - 1], (curr_x - 1, curr_y, 1, 2)))
        if curr_x + 1 < len(graph[0]) and same_dirs >= 4 and (curr_x + 1, curr_y) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y][curr_x + 1], (curr_x + 1, curr_y, 1, 0)))
        if curr_y - 1 >= 0 and same_dirs < 10 and (curr_x, curr_y - 1) not in visited:
            heapq.heappush(heap, (curr_score + graph[curr_y - 1][curr_x], (curr_x, curr_y - 1, same_dirs + 1, 3)))