class Solution {
    /**
     * @param {number} n
     * @return {string[][]}
     */
    solveNQueens(n) {
        let board=[]
        let strArray=new Array(n).fill('.')
        for (let i=0;i<n;i++){
            board.push([...strArray])
        }
        let ans=[]

        function placeQueen(row,board){
            if(row==n){
                ans.push([...board].map(r=>r.join("")))
                return ;
            }


            for (let col=0;col<n;col++){
                if(placeCheck(row,col,board)){
                    board[row][col]='Q'
                    placeQueen(row+1,board)
                    board[row][col]='.'
                }
            }
        }
        function placeCheck(row,col,board){
            let r=row;
             let c=col;
             while(r>=0){
                if(board[r][c]=='Q'){
                    return false
                }
                r--
             }
             r=row;
             c=col
             while(r>=0 && c>=0){
                if(board[r][c]=='Q'){
                    return false
                }
                r--;
                c--

             }
             r=row
             c=col
             while(r>=0 && c<n){
                if(board[r][c]=='Q'){
                    return false
                }
                r--;
                c++
             }
             return true

        }
        placeQueen(0,board)
        return ans
    }
}
