class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        tripleSet = set()

        for i in range(n):
            hashSet = set()
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in hashSet:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    tripleSet.add(":".join(map(str, temp)))  # convert to string for set
                hashSet.add(nums[j])

        # convert back to list of int triplets
        return [list(map(int, triplet.split(":"))) for triplet in tripleSet]

        