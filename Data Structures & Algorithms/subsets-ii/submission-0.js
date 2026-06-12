class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        let subsets=[]
        let n=nums.length;
        nums.sort((a,b)=>a-b)
        function generatesubsets(index,subset){
            if(index>=n){
                subsets.push([...subset])
                return ;
            }
            subset.push(nums[index])
            generatesubsets(index+1,subset)
            subset.pop()
            for (let j=index+1;j<=n;j++){
                if(nums[j]!==nums[index]){
                    generatesubsets(j,subset)
                    break
                }
            }

        }
        generatesubsets(0,[])
        return subsets
    }
}
