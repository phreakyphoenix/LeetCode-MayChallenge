# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        
        minV,maxV = float('-inf'), float('inf')
        self.idx = 0 # just need the global index 
		
        def dfs(minV,maxV):
            # stop cond
            if self.idx>= len(preorder): return None
            
            val = preorder[self.idx]
            if val<minV or val>maxV: 
                return None            
            # process
            node = TreeNode(val)
            
            # next
            self.idx +=1
            node.left = dfs(minV, node.val)
            node.right = dfs(node.val,maxV)
                    
            return node
                    
        return dfs(float('-inf'),float('inf'))