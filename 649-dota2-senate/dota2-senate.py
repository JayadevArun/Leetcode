class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        radiant=deque()
        dire=deque()
        for i in range(n):
            if senate[i]=='R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            ri=radiant.popleft()
            di=dire.popleft()
            if ri<di:
                radiant.append(ri+n)
            else:
                dire.append(di+n)
        return 'Radiant' if radiant else 'Dire'