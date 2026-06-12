class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permute(nums) {
        let taken=new Array(nums.length).fill(0)
        let result=[]
        function explorePermutations(list,taken){
            console.log(list,taken)
            if(list.length==nums.length){
                result.push([...list])
                return ;
            }

            for (let i=0;i<taken.length;i++){
                if(!taken[i]){
                    list.push(nums[i])
                    taken[i]=1
                    explorePermutations(list,taken)
                    list.pop()
                    taken[i]=0
                }
            }

        }
        explorePermutations([],taken)
        return result
    }
}
