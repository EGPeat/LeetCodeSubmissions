

class Solution:
    def add_edges(self, edges):
        for v, w in edges:
            self.adj_list[v].append(w)

    def canFinish(self, vertices, edges):
        self.vertices = vertices
        self.adj_list = defaultdict(list)
        result = []
        in_degree = [0] * self.vertices
        self.add_edges(edges)

        for i in range(self.vertices):
            for neighbor in self.adj_list[i]:
                in_degree[neighbor] += 1

        queue = deque()
        for i in range(self.vertices):
            if in_degree[i] == 0:
                queue.append(i)

        count = 0
        top_order = []

        while queue:
            u = queue.popleft()
            top_order.append(u)

            for neighbor in self.adj_list[u]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            count += 1
        if count != self.vertices:
            return False
        return True
