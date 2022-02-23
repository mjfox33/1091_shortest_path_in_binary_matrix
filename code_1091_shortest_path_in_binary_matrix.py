class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        m = len(grid[0])

        not_explored = [[True]*m for _ in range(n)]
        dp = [[float('inf')]*m for _ in range(n)]
        queue = []
        queue.append((0,0))

        def process_node(r0, c0, r1, c1):
            if r1<0 or r1>=n or c1<0 or c1>=m:
                return
            if grid[r1][c1] == 0 and not_explored[r1][c1]:
                queue.append((r1, c1))
                #not_explored[r1][c1] = False
                dp[r1][c1] = min(dp[r1][c1], dp[r0][c0] + 1)                

        while queue:
            node = queue.pop(0)
            row = node[0] #current_1d_index // m
            col = node[1] #current_1d_index % m
            not_explored[row][col] = False
            if row == 0 and col == 0:
                dp[row][col] = 1
            
            process_node(row, col, row-1, col-1)
            process_node(row, col, row-1, col)
            process_node(row, col, row-1, col+1)
            process_node(row, col, row, col-1)
            process_node(row, col, row, col+1)
            process_node(row, col, row+1, col-1)
            process_node(row, col, row+1, col)
            process_node(row, col, row+1, col+1)
                

        return dp[-1][-1]