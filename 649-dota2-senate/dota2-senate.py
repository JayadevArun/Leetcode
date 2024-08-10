class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        l=len(senate)
        r=deque()
        d=deque()
        for i in range(l):
            if senate[i]=='R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            ri=r.popleft()
            di=d.popleft()
            if ri<di:
                r.append(ri+l)
            else:
                d.append(di+l)
        return 'Radiant' if r else 'Dire'