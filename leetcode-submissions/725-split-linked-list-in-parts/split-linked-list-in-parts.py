# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head: return [None] * k
        def findLength(head):
            length = 0
            temp = head
            while temp:
                length += 1
                temp = temp.next
            return length
        
        l = findLength(head)
        split_size = l // k
        extra = l % k
        result = [None] * k
        i = 0
        l1 = head
        for i in range(k):
            req = split_size
            temp = l1
            prev = None
            while req:
                prev = l1
                l1 = l1.next if l1 else None
                req -= 1
            
            if extra:
                prev = l1
                l1 = l1.next if l1 else None
                extra -= 1
            # print(result)
            if temp != None:
                prev.next = None
            result[i] = temp
        return result
        
