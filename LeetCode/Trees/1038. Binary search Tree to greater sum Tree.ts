// Difficulty - MEDIUM
/*
function bstToGst(root: TreeNode | null): TreeNode | null {
    let sum = [0]

    function dfs_inorder(root){
        if(root == null) return

        dfs_inorder(root.right)
        root.val += sum[0]
        sum[0] = root.val
        dfs_inorder(root.left)
    }
    dfs_inorder(root)
    return root
};
*/
