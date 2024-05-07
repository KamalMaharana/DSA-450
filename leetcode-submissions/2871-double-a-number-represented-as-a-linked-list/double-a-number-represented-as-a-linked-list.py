# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node, n):
            if not node:
                return n * 2
            val = dfs(node.next, n * 10 + node.val)
            node.val = val % 10
            return val // 10
        val = dfs(head, 0)
        if val:
            new_node = ListNode(val)
            new_node.next = head
            head = new_node
        return head