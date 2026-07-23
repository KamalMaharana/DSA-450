# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            cnt = 0
            stack = []
            temp = head
            while temp and cnt < k:
                stack.append(temp)
                temp = temp.next
                cnt += 1
            
            if cnt != k:
                return head
            else:
                next_head = stack[-1].next
                dummy_head = ListNode(-1)
                temp = dummy_head
                while stack:
                    node = stack.pop()
                    temp.next = node
                    temp = node
                dummy_head = dummy_head.next
            temp.next = reverse(next_head)
            return dummy_head
        return reverse(head)
