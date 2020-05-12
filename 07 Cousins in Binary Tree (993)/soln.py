# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSibling(root, a , b): 
        # Base Case 
    if root is None: 
        return 0
    if root.left is None:
        return isSibling(root.right, a , b)
    if root.right is None:
        return isSibling(root.left, a , b)    
    return ((root.left.val == a and root.right.val ==b) or 
            (root.left.val == b and root.right.val == a)or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b))
    
def level(root, ptr, lev): 
    # Base Case  
    if root is None : 
        return 0 
    if root.val == ptr:  
        return lev 

    # Return level if Node is present in left subtree 
    l = level(root.left, ptr, lev+1) 
    if l != 0: 
        return l 

    # Else search in right subtree 
    return level(root.right, ptr, lev+1) 

class Solution:      
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        print(level(root, x, 1))
        print(level(root, y, 1))
        print (isSibling(root, x, y))
        if ((level(root,x,1) == level(root, y, 1)) and not (isSibling(root, x, y))): 
            return 1
        else: 
            return 0