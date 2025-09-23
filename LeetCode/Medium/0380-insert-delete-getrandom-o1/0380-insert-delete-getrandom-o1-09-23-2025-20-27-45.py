class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.reverse_hashmap = {}
        self.maxval = 0

    def insert(self, val: int) -> bool:
        if val in self.reverse_hashmap:
            return False
        self.hashmap[self.maxval] = val
        self.reverse_hashmap[val] = self.maxval
        self.maxval += 1      
        """print(self.hashmap)
        print("@@@@@@@@@@@@@@@@@@@@@@@")
        print(self.reverse_hashmap)
        print("#######################")"""
        return True

    def remove(self, val: int) -> bool:
        if val not in self.reverse_hashmap:
            return False
        
        #print(self.maxval)
        #print(self.reverse_hashmap)
        #print(self.hashmap)

        
        #print("#######################")
        loc_of_val = self.reverse_hashmap[val]
        val_of_last = self.hashmap[self.maxval-1]

        self.reverse_hashmap[val_of_last] = loc_of_val
        #self.reverse_hashmap[val] = self.maxval #will delete this
        #self.hashmap[self.maxval] = val #will delete this
        self.hashmap[loc_of_val] = val_of_last

        del self.reverse_hashmap[val] #will delete this
        del self.hashmap[self.maxval-1] #will delete this
        self.maxval -= 1
        return True

    def getRandom(self) -> int:
        return self.hashmap[random.randint(0, self.maxval-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()