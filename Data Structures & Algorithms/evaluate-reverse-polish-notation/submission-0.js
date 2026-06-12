class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let n=tokens.length;
        let stack=[];
        for (let i=0;i<n;i++){
            if(tokens[i]=='+' || tokens[i]=='*' || tokens[i]=='/' || tokens[i]=='-'){
                let b=stack.pop();
                let a=stack.pop();
                let res=eval(`${a} ${tokens[i]} ${b}`);
                if(tokens[i]=='/'){
                    res=Math.trunc(res)
                }
                stack.push(res)
            } else{
                stack.push(Number(tokens[i]))
            }
        }
        return stack.pop()
    }
}
