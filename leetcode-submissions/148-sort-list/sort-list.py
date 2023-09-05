# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(a, b):
            if not a: return b
            if not b: return a
            
            if a.val < b.val:
                result = a
                result.next = merge(a.next, b)
            else:
                result = b
                result.next = merge(a, b.next)
            
            return result
        
        def getMiddle(node):
            slow = node
            fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def mergeSortLL(head):
            if not head or not head.next: return head
            
            middle = getMiddle(head)
            nextToMiddle = middle.next
            middle.next = None
            left = mergeSortLL(head)
            right = mergeSortLL(nextToMiddle)
            sortedList = merge(left, right)
            return sortedList
        
        return mergeSortLL(head)

            
            
            
            