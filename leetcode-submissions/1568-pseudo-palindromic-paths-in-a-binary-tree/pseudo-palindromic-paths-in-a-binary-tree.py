# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isPalindrome(freq):
            odd = 0
            even = 0
            for val in freq:
                if val % 2 == 1:
                    odd += 1
                    if odd > 1:
                        return False
            return True
                    
        self.result = 0
        def dfs(node, freq):
            freq[node.val] += 1
            if not node.left and not node.right:
                if isPalindrome(freq):
                    self.result += 1
            if node.left:
                dfs(node.left, freq[:])
            if node.right:
                dfs(node.right, freq[:])
        
        dfs(root, [0,0,0,0,0,0,0,0,0,0])
        return self.result