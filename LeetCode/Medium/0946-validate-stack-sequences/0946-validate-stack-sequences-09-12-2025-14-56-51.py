class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        temp = []
        while pushed:
            #print(pushed, "\n", popped, "\n", temp, "\n#############")
            temp.append(pushed.pop(0))
            while temp and popped and temp[-1] == popped[0]:
                temp.pop()
                popped.pop(0)
        #print(pushed, "\n", popped, "\n", temp, "\n#############")  
        if len(pushed) + len(popped) + len(temp) == 0:
            return True
        return False