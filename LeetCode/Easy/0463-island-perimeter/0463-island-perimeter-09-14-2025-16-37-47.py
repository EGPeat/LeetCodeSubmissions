
class Solution:
    def floodfill(self, matrix, checking_grid, x, y):
        total_perimeter = 0
        movement_options = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        base_val = matrix[x][y]
        stack = [[x, y]]
        while stack:
            location = stack.pop()
            if checking_grid[location[0]][location[1]] == 1:
                continue
            #print(location, matrix[location[0]][location[1]])
            checking_grid[location[0]][location[1]] = 1
            count_neighbors = 0
            for movement in movement_options:
                x_val = location[0] + movement[0]
                y_val = location[1] + movement[1]
                # #print("testing which are looked at", [idx, idx2], [x_val, y_val])
                if (x_val < len(matrix) and x_val >= 0) and (
                    y_val < len(matrix[0]) and y_val >= 0
                ):
                    if matrix[x_val][y_val] == base_val:
                        count_neighbors += 1
                        if checking_grid[x_val][y_val] == 0:
                            stack.append(
                                [location[0] + movement[0], location[1] + movement[1]]
                            )
            total_perimeter += 4 - count_neighbors
        return total_perimeter

    def islandPerimeter(self, matrix):
        checking_grid = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        best_perimeter = 0

        for idx in range(len(matrix)):
            for idx2 in range(len(matrix[0])):
                #print("################\nNEW ROUND\n#######################")
                #print(idx, idx2)
                if matrix[idx][idx2] == 1 and checking_grid[idx][idx2] == 0:
                    peri = self.floodfill(matrix, checking_grid, idx, idx2)
                    if peri > best_perimeter:
                        best_perimeter = peri
        return best_perimeter
