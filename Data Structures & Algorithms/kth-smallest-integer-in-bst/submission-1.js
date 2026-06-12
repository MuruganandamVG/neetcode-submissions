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
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        let result=null;
        let count=k;
        function inorderTraversal(root){
            if(root==null) return ;
            inorderTraversal(root.left)
            count-=1
            if(count==0){
                result=root.val
                return ;
            }
            inorderTraversal(root.right)

        }
        inorderTraversal(root)
        return result
    }
}
