
class BFS:
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue

    def bfs(visited, graph, node):
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)


def crawltill():
    out = [n.name]
    while node !=

