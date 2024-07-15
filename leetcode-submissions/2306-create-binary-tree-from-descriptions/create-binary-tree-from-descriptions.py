# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, des: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childs = set()
        for p, c, l in des:
            childs.add(c)
            if p not in nodes:
                node = TreeNode(p)
                nodes[p] = node
            else:
                node = nodes[p]
            
            if c not in nodes:
                child = TreeNode(c)
                nodes[c] = child
            else:
                child = nodes[c]

            if l:
                node.left = child
            else:
                node.right = child
        
        for node in nodes:
            if node not in childs:
                return nodes[node]
