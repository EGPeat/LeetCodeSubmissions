class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        path_list = [item for item in path_list if item != "" and item != "."]
        path_list.reverse()
        newest_path = []
        while path_list:
            temp = path_list.pop()
            if temp == ".." and newest_path:
                newest_path.pop()
            elif temp == "..":
                pass
            else:
                newest_path.append(temp)
        output = "/" + "/".join(newest_path)
        return output