"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node):
        #with a normal node, make a copy of it (before stack)
        #then check all the neighbors, make a copy of them and link via dict
        #add neighbors to stack, also add the copies into the currnode
        if not node:
            return 
        if node:
            stack = []
            copy_dict = {}
            clone_node = Node(node.val, [])
            backup_clone = clone_node
            copy_dict[node] = clone_node
            stack.append(node)
        while stack:
            #print(stack)
            curr_node = stack.pop()
            #print(curr_node, curr_node.val)
            clone_node = copy_dict[curr_node] 
            for neighbor in curr_node.neighbors:
                if neighbor not in copy_dict.keys():    
                    clone_neighbor_node = Node(neighbor.val, [])
                    copy_dict[neighbor] = clone_neighbor_node
                    stack.append(neighbor)
                else:
                    clone_neighbor_node = copy_dict[neighbor]
                clone_node.neighbors.append(clone_neighbor_node)
                
            #print(clone_node, clone_node.val)
        return backup_clone