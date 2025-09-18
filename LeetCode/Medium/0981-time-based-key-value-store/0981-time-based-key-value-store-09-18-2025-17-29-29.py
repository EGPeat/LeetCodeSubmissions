class TimeMap:

    def __init__(self):
        self.timekeydict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timekeydict[key].append((timestamp, value))
        #self.timekeydict.sort(lambda x:x[0], reverse=True)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timekeydict.keys():
            return ""
        
        for i in range(len(self.timekeydict[key])):
            print(timestamp, self.timekeydict[key][i])
            if timestamp < self.timekeydict[key][i][0]:
                if i == 0:
                    return ""
                else:
                    return self.timekeydict[key][i-1][1]
        
        return self.timekeydict[key][-1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)