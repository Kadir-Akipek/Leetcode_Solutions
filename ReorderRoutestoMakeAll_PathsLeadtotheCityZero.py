class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set()

        for a,b in connections:
            edges.add((a,b))

        neighbours = {}

        for city in range(n):
            neighbours[city] = []

        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()

        counter = 0

        def dfs(city):
            nonlocal edges, neighbours, visited, counter
            for neighbour in neighbours[city]:
                if neighbour in visited:
                    continue
                if (neighbour, city) not in edges:
                    counter += 1
                visited.add(neighbour)
                dfs(neighbour)

        visited.add(0)
        dfs(0)
        return counter





