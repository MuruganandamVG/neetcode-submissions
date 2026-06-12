class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s, t):
              charCount={}
              for i in range(len(s)):
                  if s[i] not in charCount:
                      charCount[s[i]]=1
                  else:
                      charCount[s[i]]+=1
              for i in range(len(t)):
                  if t[i] in charCount:
                      charCount[t[i]]-=1
                  else:
                      return False
              for key,val in charCount.items():
                  if(val!=0):
                      return False
              return True
        n=len(strs)
        res=[]
        visited=[False for _ in range(n)]
        for i in range(n):
            if(visited[i]):
                continue
            anagrams=[strs[i]]
            for j in range(i+1,n):
                if (isAnagram(strs[i],strs[j])):
                    visited[j]=True
                    anagrams.append(strs[j])
            res.append(anagrams)
        return res
        