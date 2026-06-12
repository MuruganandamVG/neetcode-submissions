/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    goodNodes(root) {
        
        let count=0;
    let maxEle=-Infinity
    function traverseNodes(root,maxEle){
        if(root==null) return ;
       
        if(root.val>=maxEle){
            maxEle=root.val;
            console.log(root.val)
            count+=1
        }
        traverseNodes(root.left,maxEle);
        traverseNodes(root.right,maxEle)

    }
    if(!root) return 0
    traverseNodes(root,maxEle);
    return count
    }
}
