class Solution {
    /**
     * @param {string} digits
     * @return {string[]}
     */
    letterCombinations(digits) {
        let arr=digits
          let keyMap=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

function getWord(number){
  return keyMap[number]
}
let res=[]
let n=arr.length

function generateWords(index,str){
  if(index==n){
    res.push(str)
    return ;
  }
  
  let word=getWord(arr[index])
  if (word === '') {
                generateWords(index + 1, str); // skip 0 or 1
                return;
            }
  
      for (let ch of word){
    generateWords(index+1,str+ch)
  }
      
  
  
}
if (digits==""){
    return res
}
generateWords(0,'')
return res
    }
}
