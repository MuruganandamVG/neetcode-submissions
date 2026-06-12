class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroup={}
        for i in range(len(strs)):
            key="".join(sorted(strs[i]))
            print(key)
            if key not in anagramGroup:
                anagramGroup[key]=[]
            anagramGroup[key].append(strs[i])
        print(anagramGroup.values())

        return list(anagramGroup.values())
        