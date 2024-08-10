class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate=list(senate)
        radiant=deque()
        dire=deque()
        for i,ch in enumerate(senate):
            if ch=='R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            ri=radiant.popleft()
            di=dire.popleft()
            if ri<di:
                radiant.append(ri+len(senate))
            else:
                dire.append(di+len(senate))
        return 'Radiant' if radiant else 'Dire'