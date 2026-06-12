class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        let result=[]
        function exploreCombinations(start,list,sum){

            if(sum==target){
                result.push([...list])
                return ;

            }
            if(sum>target){
                return ;
            }

            for (let i=start;i<nums.length;i++){
                list.push(nums[i])
                exploreCombinations(i,list,sum+nums[i])
                list.pop()
            }

        }
        exploreCombinations(0,[],0)
        return result
    }
}
