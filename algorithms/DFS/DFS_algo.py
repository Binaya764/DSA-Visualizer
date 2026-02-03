def dfs_fun(graph, start):
    visited = set()
    steps = []

    def dfs(u):
        visited.add(u)

        steps.append(("push", u))
        steps.append(("visit", u))

        for v in graph[u]:
            if v not in visited:
                steps.append(("edge", u, v))
                dfs(v)
                steps.append(("back-edge", u, v))


        steps.append(("pop", u))   # backtrack


    dfs(start)
    return steps
