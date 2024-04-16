/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    if (depth == 1) {
        newNode := &TreeNode{Val: val, Left: root, Right: nil}
        return newNode
    }
    dfs(root, 1, depth, val)
    return root
}

func dfs(node *TreeNode, currDepth int, depth int, val int) {
    if currDepth == depth - 1 {
        newNode1 := &TreeNode{Val: val, Left: node.Left, Right: nil}
        newNode2 := &TreeNode{Val: val, Left: nil, Right: node.Right}
        node.Left = newNode1
        node.Right = newNode2
        return
    }
    if node.Left != nil {
        dfs(node.Left, currDepth + 1, depth, val)
    }
    if node.Right != nil {
        dfs(node.Right, currDepth + 1, depth, val)
    }
}