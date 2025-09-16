class Solution:
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        out = [[float('inf') for _ in range(len(mat[0]))] for _ in range(len(mat))]
        visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
        queue = deque()
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 0:
                    queue.append((x, y))
        
        print(queue)

        while queue:
            row, col = queue.popleft()
            #print((row, col), visited[row][col])
            if not visited[row][col]:
                visited[row][col] = True
                if mat[row][col] == 0:
                    out[row][col] = 0
                else:
                    curr_min = float('inf')
                    for neighbor in get_neighbors((row, col), r, c):
                        curr_min = min(curr_min, out[neighbor[0]][neighbor[1]])
                    out[row][col] = curr_min + 1
                for neighbor in get_neighbors((row, col), r, c):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
        return out



def get_neighbors(coord, r, c):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < r and 0 <= neighbor_col < c:
            res.append((neighbor_row, neighbor_col))
    return res