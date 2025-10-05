class Solution:
    def frequencySort(self, s: str) -> str:
        counted = Counter(s)
        true_list = [(item[1],item[0]) for item in counted.items()]
        true_list.sort(key=lambda x:x[0], reverse=True)
        print(true_list)
        temp = []
        curr_val = true_list[0][0]
        output = ""
        while true_list or temp:
            if true_list and true_list[0][0] == curr_val:
                tmp = true_list.pop(0)
                temp.append(tmp[1])
            else:
                #print(temp)
                temp.sort()
                #print(temp)
                for item in temp:
                    tempstr = item * curr_val
                    #print(tempstr)
                    output += tempstr
                temp = []
                if true_list:
                    curr_val = true_list[0][0]
                #print(output)
        return output