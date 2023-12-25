from collections import defaultdict
import igraph

file = open("input.txt")

nodes = defaultdict(list)
connections = []
for line in file:
    source, dests = line.strip().split(": ")
    for dest in dests.split():
        nodes[source].append(dest)
        nodes[dest].append(source)
        connections.append((source, dest))

g = igraph.Graph()
for node in nodes.keys():
    g.add_vertex(node)
g.add_edges(connections)

cut = g.mincut()
print(len(cut.partition[0]) * len(cut.partition[1]))