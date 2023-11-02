# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node):
            if not node:
                return 0,0
            
            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)
            subtree_sum = (leftSum + rightSum + node.val)
            subtree_node_count = (leftCount + rightCount + 1)
            avg = subtree_sum // subtree_node_count
            if avg == node.val:
                self.result += 1
            return (subtree_sum, subtree_node_count)
        dfs(root)
        return self.result
