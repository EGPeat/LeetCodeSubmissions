class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        q = deque()

        visited[source] = True
        q.append(source)

        while q:
            currentVertex = q.popleft()

            for neighbor in graph[currentVertex]:
                if not visited[neighbor]:   
                    visited[neighbor] = True
                    q.append(neighbor)



            if visited[destination]:
                return True
        return False