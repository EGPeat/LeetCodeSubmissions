from heapq import *


class FreqStack:
    def __init__(self):
        self.heap = []
        self.hashmap = {}
        self.counter = 0

    def push(self, num):
        val_get = self.hashmap.get(num, 0) + 1
        self.hashmap[num] = val_get
        heappush(self.heap, (-val_get, num, self.counter))
        self.counter += 1
        return

    def pop(self):
        temp = []
        output = heappop(self.heap)
        temp.append(output)
        output2 = heappop(self.heap)
        if (
            output[0] == output2[0]
        ):  # i can simplify down to just a single while loop with temp.append first then heappop
            temp.append(output2)
            while self.heap and output[0] == output2[0]:
                output2 = heappop(self.heap)
                if output[0] == output2[0]:
                    temp.append(output2)
            if not self.heap and output[0] != output2[0]:
                heappush(self.heap, output2)
        else:
            heappush(self.heap, output2)
        temp.sort(key=lambda x: x[2])
        output = temp.pop()
        while temp:
            heappush(self.heap, temp.pop())

        self.hashmap[output[1]] = self.hashmap.get(output[1], 0) - 1
        return output[1]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()