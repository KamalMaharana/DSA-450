# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        is_even = True
        while queue:
            l = len(queue)
            maxi = 0
            mini = 0
            for i in range(l):
                node = queue.pop(0)
                if not maxi:
                    maxi = -inf
                if not mini:
                    mini = inf
                
                # On EVEN, check for ODD values
                if is_even:
                    if node.val % 2 == 0 or node.val <= maxi:
                        return False

                # On ODD, check for EVEN values
                else:
                    if node.val % 2 != 0 or node.val >= mini:
                        return False
                
                maxi = max(node.val, maxi)
                mini = min(node.val, mini)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            is_even = not is_even
        return True