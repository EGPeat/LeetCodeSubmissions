class Solution:
    def helper(self, heights, queue, n, n2):
        visited = set(queue)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                temp = queue.popleft()
                for direction in directions:
                    new_val = (temp[0] + direction[0], temp[1] + direction[1])
                    if 0 <= new_val[0] < n and 0 <= new_val[1] < n2:
                        if new_val not in visited and heights[temp[0]][temp[1]] <= heights[new_val[0]][new_val[1]]:
                            visited.add(new_val)
                            queue.append(new_val)
        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pqueue = deque()
        aqueue = deque()
        n, n2 = len(heights), len(heights[0])
        for spot in range(n2):
            pqueue.append((0, spot))
            aqueue.append((n-1, spot))
        for spot in range(n):
            pqueue.append((spot, 0))
            aqueue.append((spot, n2-1))

        

        visited_p = self.helper( heights, pqueue, n, n2)
        visited_a = self.helper( heights, aqueue, n, n2)
        visited_b = visited_p & visited_a
        return list(visited_b)