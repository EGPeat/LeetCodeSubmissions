class Solution:
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        out = [[-1 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        queue = deque()
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if mat[x][y] == 0:
                    queue.append((x, y, 0))
                    out[x][y] = 0
        
        #print(queue)

        while queue:
            row, col, height = queue.popleft()
            #print((row, col), visited[row][col])
            for neighbor in get_neighbors((row, col), r, c, out):
                queue.append((neighbor[0], neighbor[1], out[row][col]))
                out[neighbor[0]][neighbor[1]] = out[row][col] + 1
        return out



def get_neighbors(coord, r, c, out):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < r and 0 <= neighbor_col < c and out[neighbor_row][neighbor_col] == -1:
            res.append((neighbor_row, neighbor_col))
    return res