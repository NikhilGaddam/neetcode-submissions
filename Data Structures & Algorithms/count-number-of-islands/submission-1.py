class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0
        
        r = len(grid)
        c = len(grid[0])
        island_count = 0

        def dfs(row, col):
            if row <0 or row>= r:
                return
            if col < 0 or col >=c:
                return 
            if grid[row][col] == '0':
                return 
            
            grid[row][col] = '0'

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for row in range(r):
            for col in range(c):
                if grid[row][col] == '1':
                    island_count += 1

                    dfs(row, col)
        return island_count

        