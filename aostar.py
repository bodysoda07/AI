def ao_star():

    graph = {
        'A': [[('B', 1), ('C', 1)], [('D', 1)]],
        'B': [[('E', 1), ('F', 1)]],
        'C': [[('G', 1)]],
        'D': [[('H', 1)]],
        'E': [],
        'F': [],
        'G': [],
        'H': []
    }

    cost = {
        'E': 0,
        'F': 0,
        'G': 0,
        'H': 0
    }

    def solve(node):

        if node in cost:
            return cost[node]

        print("Visiting:", node)

        options = []

        for group in graph[node]:

            total = 0

            for child, edge in group:
                total += edge + solve(child)

            options.append(total)

        cost[node] = min(options)

        print("Best cost for", node, "=", cost[node])

        return cost[node]

    result = solve('A')

    print("Minimum Cost =", result)


ao_star()