class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c=0
        for item in items:
            if ((ruleKey=="type" and ruleValue==item[0]) or (ruleKey=="color" and ruleValue==item[1]) or (ruleKey=="name" and ruleValue==item[2])):
                c+=1
        return c