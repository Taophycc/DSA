// Difficulty - EASY
/*
function increasingBST(root: TreeNode | null): TreeNode | null {
    const result: number[] = [] 

    function inorder(root){
        if (root == null) return
        inorder(root.left)
        result.push(root.val)
        inorder(root.right)
    }
    inorder(root)

    let newRoot = new TreeNode(result.shift())
    let curr = newRoot

    while(result.length !== 0){
        curr.right = new TreeNode(result.shift())
        curr = curr.right
    }
    return newRoot
};
*/
