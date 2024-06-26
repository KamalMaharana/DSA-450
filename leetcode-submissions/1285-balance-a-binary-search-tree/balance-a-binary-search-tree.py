# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.vals = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.vals.append(node.val)
            dfs(node.right)
        dfs(root)

        self.root = None
        def formTree(arr, node = None):
            if not arr:
                return
            mid = len(arr) // 2
            val = arr[mid]
            new_node = TreeNode(val)
            if self.root == None:
                self.root = new_node
            else:
                if val > node.val:
                    node.right = new_node
                else:
                    node.left = new_node
            formTree(arr[:mid], new_node)
            formTree(arr[mid+1:], new_node)
        
        formTree(self.vals)
        return self.root

