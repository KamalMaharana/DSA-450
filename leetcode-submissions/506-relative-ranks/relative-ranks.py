class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new_score = sorted(score, reverse = True)
        rank = dict()
        
        for i,n in enumerate(new_score):
            if i == 0:
                curr_rank = "Gold Medal"
            elif i == 1:
                curr_rank = "Silver Medal"
            elif i == 2:
                curr_rank = "Bronze Medal"
            else:
                curr_rank = str(i + 1)

            rank[n] = curr_rank
        
        for i in range(len(score)):
            score[i] = rank[score[i]]
        return score