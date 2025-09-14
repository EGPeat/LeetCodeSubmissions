class Solution:
    def convert_num(self, num):
        num = str(num)
        output = 0
        for char in num:
            output += int(char) * int(char)
        return output


    def isHappy(self, num):
        list_of_nums = [num]
        switch = 0
        fast = num
        slow = None
        while True:
            if num == 1:
                return True
            elif fast == slow:
                return False
            num = self.convert_num(num)
            list_of_nums.append(num)
            switch += 1
            slow = list_of_nums[switch//2]
            fast = num
        