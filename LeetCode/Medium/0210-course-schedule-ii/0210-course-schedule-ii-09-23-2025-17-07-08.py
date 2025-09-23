class Solution:
    def find_indegree(self, graph):
        indegree = { node: 0 for node in graph }  # dict
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree
    def findOrder(self, tasks: int, requirements: List[List[int]]) -> List[int]:
        from collections import deque
        graph = {}
        for task in range(tasks):
            graph[task] = []
        for req in requirements:
            graph[req[0]].append(req[1])
        res = []
        q = deque()
        indegree = self.find_indegree(graph)
        #print(graph, indegree)
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
        while len(q) > 0:
            node = q.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return res[::-1] if len(graph) == len(res) else []