from collections import defaultdict


class Solution:
    def __init__(self):
        self.set = []

    def mergeArrays(self, items1, items2):
        merged_items = defaultdict(int)
        for lister in [items1, items2]:
            for item in lister:
                if not any(sublist[0] == item[0] for sublist in self.set):
                    self.set.append(item)
                    self.set.sort(key=lambda x: x[0], reverse=True)
                else:
                    self.set[sum(1 for x in self.set if x[0] > item[0])][1] += item[1]
        print(self.set)
        return self.set[::-1]
