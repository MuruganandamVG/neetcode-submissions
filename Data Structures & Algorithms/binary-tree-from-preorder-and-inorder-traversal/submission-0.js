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
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
   

    buildTree(preorder, inorder) {
         let inOrderMap=new Map();
         inorder.forEach((key,index)=>{
            inOrderMap.set(key,index)
         })
        function build(preStart,preEnd,inStart,inEnd){
            if(preStart>preEnd || inStart>inEnd){
                return null;
            }
            let rootVal=preorder[preStart]
            let inRoot=inOrderMap.get(rootVal);
            let root=new TreeNode(rootVal)
            let leftSize=inRoot-inStart;

            root.left=build(preStart+1,preStart+leftSize,inStart,inRoot-1);;
            root.right=build(preStart+leftSize+1,preEnd,inRoot+1,inEnd);
            return root
        }
        return build(0,preorder.length-1,0,inorder.length-1)

    }
}
