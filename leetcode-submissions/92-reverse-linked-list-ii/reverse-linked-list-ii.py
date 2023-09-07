# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        temp = head
        prev = None
        count = 1
        while count != left:
            prev = temp
            temp = temp.next
            count += 1
        
        def reverseLL(head, right, count):
            prev = None
            curr = head
            while count != right:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
                count += 1
                
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
            head.next = curr
            return prev
        if prev != None:
            prev.next = reverseLL(temp, right, count)
            return head
        else:
            return reverseLL(temp, right, count)