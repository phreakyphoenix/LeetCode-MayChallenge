class Solution:
    def dfs(self, start):
        if self.found_loop == 1: return        #early stop if we found odd cycle
    
        for neib in self.adj_list[start]:
            if self.dist[neib] > 0 and (self.dist[neib] - self.dist[start]) %2 == 0:
                self.found_loop = 1
            elif self.dist[neib] < 0:  #not visited yet
                self.dist[neib] = self.dist[start] + 1
                self.dfs(neib)
            
    def possibleBipartition(self, N, dislikes):
        self.adj_list = defaultdict(list)
        self.found_loop, self.dist = 0, [-1] *(N+1)
        
        for i,j in dislikes:
            self.adj_list[i].append(j)
            self.adj_list[j].append(i)
        
        for i in range(N):
            if self.found_loop: return False    #early stop if we found odd cycle
            
            if self.dist[i] == -1:    #not visited yet
                self.dist[i] = 0
                self.dfs(i)
        
        return True