class Solution:
    def isValid(self, s: str) -> bool:
        match={')':'(','}':'{',']':'['}
        stack=[]
        for ch in s:
            if ch in match and len(stack)==0:
                return False
            if ch in match and  match[ch]==stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0
