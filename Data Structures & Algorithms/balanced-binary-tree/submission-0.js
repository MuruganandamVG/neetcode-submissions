/**
 * Definition for a binary tree node.
 * class TreeNode {
 *      constructor(val = 0, left = null, right = null){
 *          this.data = val;
 *          this.left = null;
 *          this.right = null;
 *      }
 * }
 **/

class Solution {
  findDepth(root) {
    if (root == null) return 0;
    let left = this.findDepth(root.left);
    let right = this.findDepth(root.right);
    return 1 + Math.max(left, right);
  }
  isBalanced(root) {
    //your code goes here
    if (!root) return true;
    let leftDepth = this.findDepth(root.left);
    let rightDepth = this.findDepth(root.right);
    if (Math.abs(leftDepth - rightDepth) > 1) {
      return false;
    }
    return this.isBalanced(root.left) && this.isBalanced(root.right);
  }
}
