class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
         let n=temperatures.length;
    let answers=new Array(n).fill(0);
    let stack=[]
    for (let i=n-1;i>=0;i--){
        while(stack.length && temperatures[stack[stack.length-1]]<=temperatures[i]){
            stack.pop()
        }
        if(stack.length){
            answers[i]=stack[stack.length-1]-i
        }
        stack.push(i)

        
    }
    return answers
    }
}
