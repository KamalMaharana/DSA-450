# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        count = 0
        temp = head
        result = []
        tlist = []
        while temp:
            if count == k:
                result += reversed(tlist)
                tlist = []
                count = 0
            tlist.append(temp.val)
            temp = temp.next
            count += 1
        if count == k:
            result += reversed(tlist)
        else:
            result += tlist
        print(result)
        newHead = None
        for i in result:
            newNode = ListNode(i)
            if newHead == None:
                newHead = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        return newHead
            