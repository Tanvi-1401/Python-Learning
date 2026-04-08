from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph.get(node, []):
                queue.append(neighbor)


def dfs(graph, start):
    visited = set()
    stack = [start]

    print("\nDFS Traversal:", end=" ")

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph.get(node, [])):
                stack.append(neighbor)


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ").strip()
    neighbors = input(f"Enter neighbors of {node}: ").split()
    neighbors = [n.strip() for n in neighbors]
    graph[node] = neighbors

start = input("Enter starting node: ").strip()

print("\nGraph:", graph)

bfs(graph, start)
dfs(graph, start)