class Solution {
    /**
     * @param {character[][]} board
     * @param {string} word
     * @return {boolean}
     */
    exist(board, word) {

        const visited=new Set()


        function findWord(row,col,index){ 
            if(row<0 || col<0 || row>=rows || col>=cols){
                return false ;
            }
            let key=row+'-'+col;
            if(visited.has(key)) return false
          
            if(board[row][col]!==word[index]){
                return false;
            }
            if(index==word.length-1) return true
            visited.add(key)

            const found=findWord(row,col+1,index+1) || findWord(row,col-1,index+1) || findWord(row+1,col,index+1) || findWord(row-1,col,index+1) 
            visited.delete(key)
            return found

        }
        let rows=board.length;
        let cols=board[0].length;
        for (let i=0;i<rows;i++){
            for (let j=0;j<cols;j++){
                if(findWord(i,j,0)){
                    return true
                }
            }
        }
        return false
    }
}
