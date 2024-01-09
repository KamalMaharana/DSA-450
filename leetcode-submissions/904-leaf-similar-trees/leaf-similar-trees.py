# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(node, num) -> list:
            if not node:
                return
            if node.left == None and node.right == None:
                if num:
                    self.a.append(node.val)
                else:
                    self.b.append(node.val)
                
            # print(node.val, node.left, node.right)
            getLeaves(node.left, num)
            getLeaves(node.right, num)
            
        self.a = []
        self.b = []
        getLeaves(root1, 0)
        getLeaves(root2, 1)
        # print(self.a, self.b)
        return self.a == self.b
        
