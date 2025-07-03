class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        number_of_ops = len(matrix[0])*len(matrix)
        triggered_last = 'TL'
        
        curr_width = 0
        curr_height = 0
        min_width = 0
        min_height = 0
        width = len(matrix[0]) -1
        height = len(matrix) - 1

        for idx in range(number_of_ops):
            #print(f"{idx+1}: ({curr_height}, {curr_width}) = {matrix[curr_height][curr_width]}")
            
            result.append(matrix[curr_height][curr_width])

    
            if triggered_last == "TL" and curr_width == width:
                triggered_last = "TR"
                min_height +=1
            elif triggered_last == "TR" and curr_height == height:
                triggered_last = "BR"
                width -= 1
            elif triggered_last == "BR" and curr_width == min_width:
                triggered_last = "BL"
                height -= 1
            elif triggered_last == "BL" and curr_height == min_height:
                triggered_last = "TL"
                min_width += 1

            match triggered_last:
                case "TL":
                    curr_width += 1
                case "TR":
                    curr_height += 1
                case "BL":
                    curr_height -= 1
                case "BR":
                    curr_width -= 1
        return result