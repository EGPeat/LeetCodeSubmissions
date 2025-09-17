class Solution:
    def findMinHeightTrees(self, nodes: int, edges: List[List[int]]) -> List[int]:
        if nodes <= 0:
            return []
        if nodes == 1:
            return [0]

        inDegree = {i: 0 for i in range(nodes)}
        graph = {i: [] for i in range(nodes)}

        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
            inDegree[parent] += 1
            inDegree[child] += 1

        leaves = deque()
        for i in range(nodes):
            if inDegree[i] == 1:
                leaves.append(i)

        total_nodes = nodes
        print(leaves)
        while total_nodes > 2:
            leaves_count = len(leaves)
            total_nodes -= leaves_count
            new_leaves = deque()

            while leaves:
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 1:
                        new_leaves.append(neighbor)

            leaves = new_leaves
        return list(leaves)