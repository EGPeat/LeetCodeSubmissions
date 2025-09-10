class Solution:
    def floodFill(self, image: List[List[int]], r: int, c: int, replacement: int) -> List[List[int]]:
        from collections import deque
        num_rows, num_cols = len(image), len(image[0])
        start_color = image[r][c]
        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    res.append((neighbor_row, neighbor_col))
            return res
        queue = deque([(r, c)])
        visited = set((r, c))
        while len(queue) > 0:
            node = queue.popleft()
            if image[node[0]][node[1]] == start_color:
                image[node[0]][node[1]] = replacement
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
        return image