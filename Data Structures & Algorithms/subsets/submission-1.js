class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        let n=nums.length;
        let subsets=[]
        function findsubsets(index,subset){
            if(index>=n){
                subsets.push([...subset]);
                return;
            }
            subset.push(nums[index])
            findsubsets(index+1,subset);
            subset.pop()
            findsubsets(index+1,subset)

        }
        findsubsets(0,[])
        return subsets
    }
}
