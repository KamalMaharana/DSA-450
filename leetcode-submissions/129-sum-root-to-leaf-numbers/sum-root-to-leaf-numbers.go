/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var sums int // Global variable

func sumNumbers(root *TreeNode) int {
    sums = 0 // Initialize sums
    dfs(root, 0)
    return sums
}

func dfs(node *TreeNode, currSum int) {
    if node.Left == nil && node.Right == nil {
        currSum = currSum*10 + node.Val
        sums += currSum
        return
    }
    currSum = currSum*10 + node.Val
    if (node.Left != nil) {
        dfs(node.Left, currSum)
    }
    if (node.Right != nil) {
        dfs(node.Right, currSum)
    }    
}
