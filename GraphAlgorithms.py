from collections import defaultdict, deque


class GraphAlgorithms:
    # adj_list is a hashmap of (key, value) pairs
    # key is the vertex and value is a list of adjacent vertexes
    # if value is simply a list then all edges are unweighted
    # if value is another hashmap then the key value pairs signify the weights

    def __init__(self, num_vertexes):
        self.vertexes = num_vertexes
        self.graph = defaultdict(list)

    def printGraph(self):
        print(self.graph)

    def addEdge(self, u, v, weight=1):
        self.graph[u].append((v, weight))

    def iterative_dfs(self, start=0):
        visited = [False] * self.vertexes
        path = []
        stack = [start]

        # dfs needs to work for disconnected graphs too
        while stack or False in visited:
            # if stack is empty we need to move to a new disconnected component
            if not stack:
                stack = [visited.index(False)]

            curr = stack.pop()
            if not visited[curr]:
                visited[curr] = True
                path.append(curr)
                for neighbor, _ in self.graph[curr]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

        return path

    def recursive_dfs(self, start=0):
        visited = [False] * self.vertexes
        path = []
        self.dfs_helper(start, visited, path)
        for i in range(self.vertexes):
            if not visited[i]:
                self.dfs_helper(i, visited, path)
        return path

    def dfs_helper(self, curr, visited, path):
        visited[curr] = True
        path.append(curr)

        for neighbor, _ in self.graph[curr]:
            if not visited[neighbor]:
                self.dfs_helper(neighbor, visited, path)

    def iterative_bfs(self, start=0):
        visited = [False] * self.vertexes
        path = []
        queue = deque()
        queue.append(start)

        while queue or False in visited:
            if not queue:
                queue.append(visited.index(False))

            curr = queue.popleft()
            if not visited[curr]:
                visited[curr] = True
                path.append(curr)
                for neighbor, _ in self.graph[curr]:
                    if not visited[neighbor]:
                        queue.append(neighbor)

        return path

    def recursive_bfs(self, start=0):
        visited = [False] * self.vertexes
        path = []

        self.bfs_helper(start, visited, path)
        for i in range(self.vertexes):
            if not visited[i]:
                self.bfs_helper(i, visited, path)

        return path
    def bfs_helper(self, curr, visited, path):
        visited[curr] = True
        path.append(curr)

        for neighbor, _ in self.graph[curr]:
            if not visited[neighbor]:
                self.bfs_helper(neighbor, visited, path)