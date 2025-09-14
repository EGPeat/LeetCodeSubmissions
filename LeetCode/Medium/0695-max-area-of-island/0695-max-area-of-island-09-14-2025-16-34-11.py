class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:

        biggestIslandArea = 0
        totalIslands = 0
        movement_options = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # print(matrix)
        # print(type(matrix[0][0]), matrix[0][0])
        for idx in range(len(matrix)):
            for idx2 in range(len(matrix[0])):
                # print("start of round", idx, idx2, matrix[idx][idx2], "totall islands", totalIslands)
                if matrix[idx][idx2] == 1:
                    land_area = 0
                    stack = [[idx, idx2]]
                    while stack:
                        location = stack.pop()
                        if matrix[location[0]][location[1]] == 1:
                            land_area += 1
                        # print(location, matrix[location[0]][location[1]])
                        matrix[location[0]][location[1]] = 0
                        for movement in movement_options:
                            x_val = location[0] + movement[0]
                            y_val = location[1] + movement[1]
                            # print("testing which are looked at", [idx, idx2], [x_val, y_val])
                            if (x_val < len(matrix) and x_val >= 0) and (
                                y_val < len(matrix[0]) and y_val >= 0
                            ):
                                # print("looking neighbors", ([location[0] + movement[0]],[location[1] + movement[1]]),matrix[location[0] + movement[0]][location[1] + movement[1]])
                                if matrix[x_val][y_val] == 1:
                                    stack.append(
                                        [
                                            location[0] + movement[0],
                                            location[1] + movement[1],
                                        ]
                                    )
                    if land_area > biggestIslandArea:
                        biggestIslandArea = land_area
        return biggestIslandArea
