"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Approach
# Here's how the 1st algorithm goes.
# Consider l1 as a node on the 1st list and l2 as the corresponding node on 2nd list.
# Step 1:
# Build the 2nd list by creating a new node for each node in 1st list. 
#  While doing so, insert each new node after it's corresponding node in the 1st list.
# Step 2:
#  The new head is the 2nd node as that was the first inserted node.
#  Step 3:
#  Fix the random pointers in the 2nd list: (Remember that l1->next is actually l2)
#  l2->random will be the node in 2nd list that corresponds l1->random, 
# which is next node of l1->random.
# Step 4:
# Separate the combined list into 2: Splice out nodes that are part of second list. 
# Return the new head that we saved in step 2.



class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None: return None
        l1 = head
        while l1 != None:
            # Create new duplicate node
            l2 = Node(l1.val)
            # Preserve next
            l2.next = l1.next
            # Attach the duplicate to main LinkList
            l1.next = l2
            # Go to next value from 1st LinkList
            l1 = l1.next.next
        
        newHead = head.next
        l1 = head
        while l1 != None:
            if l1.random:
                # As duplicate nodes are l1.next
                # Duplicate OG Node's Random -> Duplicate Random Node
                l1.next.random = l1.random.next
            l1 = l1.next.next
        
        # Remove duplicates, 1 based explanation
        l1 = head
        while l1:
            l2 = l1.next
            # 1.next -> 3rd node
            l1.next = l2.next
            if l2.next:
                # Go to 4th node that is part of 2nd LinkList
                # 2.next = 2.next.next = 3.next = 4th node
                l2.next = l2.next.next
            l1 = l1.next
        return newHead