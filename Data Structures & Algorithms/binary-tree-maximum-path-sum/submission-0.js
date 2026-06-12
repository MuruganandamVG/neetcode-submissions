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
    maxPathSum(root) {
        let maxSum=-Infinity;
        function findPathSum(root){
            if(root==null) return 0;
            let leftSum=Math.max(0,findPathSum(root.left));
            let rightSum=Math.max(0,findPathSum(root.right));
            maxSum=Math.max(maxSum,leftSum+rightSum+root.val);
            return Math.max(leftSum,rightSum)+root.val
        }
        findPathSum(root);
        return maxSum
    }
}
