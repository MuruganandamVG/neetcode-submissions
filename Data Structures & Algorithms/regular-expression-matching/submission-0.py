class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        cache={}
        def dfs(i,j):
            if j==n:
                return i==m 
            key=(i,j)
            if key in cache:
                return cache[key]
            match=i<m and (s[i]==p[j] or p[j]==".")
            if j+1<n and p[j+1]=="*":
                cache[key]=(dfs(i,j+2) or (match and dfs(i+1,j)))
                return cache[key]
            if match:
                cache[key]=dfs(i+1,j+1)
                return cache[key]
            cache[key]=False
            return cache[key]
        return dfs(0,0)
        