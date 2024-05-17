# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def isleaf(node):
            return node.left == None and node.right == None

        def dfs(node):
            node.left = dfs(node.left) if node.left else None
            node.right = dfs(node.right) if node.right else None
            if isleaf(node):
                if node.val == target:
                    return None
            return node
        return dfs(root)
