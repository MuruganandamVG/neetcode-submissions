class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    
    isValid(s) {
        let characters={
        ')':'(',
        ']':'[',
        '}':'{'
    }
        let stack=[];
        let n=s.length;
        for (let i=0;i<n;i++){
            if(s[i]==')' || s[i]=='}' || s[i]==']'){
                if(stack.pop()!==characters[s[i]]){
                    return false
                }
            } else{
                stack.push(s[i])
            }
        }
        if(stack.length){
            return false
        }

        return true
    }
}
