class Solution:
    def helper(self, heights, can_flow, queue, n, n2):
        visited = set(queue)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                temp = queue.popleft()
                for direction in directions:
                    new_val = (temp[0] + direction[0], temp[1] + direction[1])
                    #print(temp, new_val)
                    if 0 <= new_val[0] < n and 0 <= new_val[1] < n2:
                        #print("In correct range")
                        if new_val not in visited and heights[temp[0]][temp[1]] <= heights[new_val[0]][new_val[1]]:
                            #print("not inside visited")
                            visited.add(new_val)
                            queue.append(new_val)
                        #print(temp, new_val)
                        #print(f"{heights[temp[0]][temp[1]], heights[new_val[0]][new_val[1]]} heights[temp[0]][temp[1]] >= heights[new_val[0]][new_val[1]], {heights[temp[0]][temp[1]] >= heights[new_val[0]][new_val[1]]}")
                        #if heights[temp[0]][temp[1]] >= heights[new_val[0]][new_val[1]]:
                        #    can_flow[temp[0]][temp[1]] = max(can_flow[temp[0]][temp[1]], can_flow[new_val[0]][new_val[1]])
        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pqueue = deque()
        aqueue = deque()
        n, n2 = len(heights), len(heights[0])
        print(n, n2)
        can_flow_p = [ [0 for _ in range(n2)] for _ in range(n)]
        can_flow_a = [ [0 for _ in range(n2)] for _ in range(n)]
        for row in heights:
            print(row)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        for spot in range(n2):
            pqueue.append((0, spot))
            aqueue.append((n-1, spot))
            can_flow_p[0][spot] = 1
            can_flow_a[n-1][spot] = 1
        for spot in range(n):
            pqueue.append((spot, 0))
            aqueue.append((spot, n2-1))
            can_flow_p[spot][0] = 1
            can_flow_a[spot][n2-1] = 1
        

        visited_p = self.helper( heights, can_flow_p, pqueue, n, n2)
        #for row in can_flow_p:
        #    print(row)
        #print("####################")

        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        visited_a = self.helper( heights, can_flow_a, aqueue, n, n2)

        visited_b = visited_p & visited_a

        #for row in can_flow_a:
        #    print(row)
        #print("####################")
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        output = []
        #can_flow_both = [ [0 for _ in range(n2)] for _ in range(n)]
        #for row in range(n):
        #    for col in range(n2):
        #        if can_flow_a[row][col] and can_flow_p[row][col]:
        #            output.append([row, col])         
        #            can_flow_both[row][col] = 2
        #        elif can_flow_a[row][col] or can_flow_p[row][col]:
        #            can_flow_both[row][col] = 1
        
        #for row in can_flow_both:
        #    print(row)
        #print("####################")
        return list(visited_b)