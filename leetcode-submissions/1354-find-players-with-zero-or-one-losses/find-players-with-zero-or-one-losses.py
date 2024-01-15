class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losses = defaultdict(lambda: 0)
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] += 1
        
        result = [[],[]]
        for player in players:
            if player not in losses:
                result[0].append(player)
            elif losses[player] == 1:
                result[1].append(player)
        result[0].sort()
        result[1].sort()
        return result