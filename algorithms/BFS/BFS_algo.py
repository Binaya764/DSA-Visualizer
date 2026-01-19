from collections import deque
def bfs_fun(self, graph, start):
    visited = set()
    queue = deque()
    steps = []

    queue.append(start)
    visited.add(start)
    steps.append(("enqueue", start))

    while queue:
        node = queue.popleft()
        steps.append(("dequeue", node))
        steps.append(("visit", node))

        for neighbor in graph[node]:
            if neighbor not in visited:
                # EDGE IS BEING TRAVERSED HERE
                steps.append(("edge", node, neighbor))

                visited.add(neighbor)
                queue.append(neighbor)
                steps.append(("enqueue", neighbor))

    return steps

