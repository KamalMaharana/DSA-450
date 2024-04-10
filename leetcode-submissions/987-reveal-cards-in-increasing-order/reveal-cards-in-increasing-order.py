class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        deck.sort(reverse = True)
        queue.append(deck[0])
        for i in deck[1:]:
            val = queue.pop()
            queue.appendleft(val)
            queue.appendleft(i)
        return queue

