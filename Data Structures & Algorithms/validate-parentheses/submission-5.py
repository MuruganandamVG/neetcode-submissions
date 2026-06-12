class Solution:
    def isValid(self, s: str) -> bool:
        match={')':'(','}':'{',']':'['}
        stack=[]
        for ch in s:
            if ch in match :
                if not stack or match[ch]!=stack.pop():
                    return False
            else:
                stack.append(ch)
        return len(stack)==0
