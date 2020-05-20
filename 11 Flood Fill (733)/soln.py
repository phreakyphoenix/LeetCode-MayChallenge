class Solution:
    def floodFill(self, img: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        new_c = new_color
        prv_c = img[sr][sc]
        n_col = len(img[0])
        n_row = len(img)
        if new_c == prv_c:
            return img
        
        def kill(x, y):
            if img[x][y] == new_c or img[x][y] != prv_c:
                return 
            img[x][y] = new_c
            # print (f'Killed {x}, {y}')
            if y!=n_col-1: kill(x, y+1)
            if y!=0: kill(x, y-1)
            if x!=0: kill(x-1, y)
            if x!=n_row-1: kill(x+1, y)
        
        kill(sr, sc)
        
        return img