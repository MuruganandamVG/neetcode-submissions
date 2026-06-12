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

class Codec {
    /**
     * Encodes a tree to a single string.
     *
     * @param {TreeNode} root
     * @return {string}
     */
    serialize(root) {
        if(!root) return "" ;
        let result=[];
        let queue=[root];
        while(queue.length>0){
            let node=queue.shift();
            if(node==null){
                result.push('#')
            } else {
                 result.push(node.val)
            queue.push(node.left);
            queue.push(node.right)

            }
        
        }
        return result.join(",")
    }

    /**
     * Decodes your encoded data to tree.
     *
     * @param {string} data
     * @return {TreeNode}
     */
    deserialize(data) {
        if(data=="") return null;
        let nodes=data.split(",");
        let root=new TreeNode(nodes.shift());
        let queue=[root];
        while(queue.length){
            let node=queue.shift();
            let leftval=nodes.shift();
            let rightval=nodes.shift()
            if(leftval!=='#'){
                 let leftnode=new TreeNode(leftval)
                  node.left=leftnode;
                   queue.push(leftnode);
                
                
            }

            if(rightval!=='#'){
                  let rightnode=new TreeNode(rightval)
            node.right=rightnode;
             queue.push(rightnode)

            }
           
        }
        return root
    }
}
