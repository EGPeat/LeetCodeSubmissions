class TrieNode:
     def __init__(self):
         self.children = {}
         self.isEnd = False



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        for index in range(len(searchWord)):
            temp_list = []
            for product in products:
                if product.startswith(searchWord[0:index+1]):
                    temp_list.append(product)
            temp_list.sort()
            if len(temp_list) >= 3:
                result.append(temp_list[:3])
            else:
                result.append(temp_list)


        return result