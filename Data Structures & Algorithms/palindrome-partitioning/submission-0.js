class Solution {
    /**
     * @param {string} s
     * @return {string[][]}
     */
    partition(s) {
        function checkPalindrome(str){
            let left=0;
            let right=str.length-1;
            while(left<=right){
                if(str[left]!==str[right]){
                    return false
                }
                left+=1
                right-=1
            }
            return true
        }
        let results=[]
        function generatePalindromeStrings(index,list){
            if(index==s.length){
                results.push([...list])
                return 

            }


            for (let i=index;i<s.length;i++){
                let substr=s.slice(index,i+1);
                if(checkPalindrome(substr)){
                    list.push(substr)
                    generatePalindromeStrings(i+1,list)
                    list.pop()
                }
                  
            }

        }
        generatePalindromeStrings(0,[])
        return results
    }
}
