class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #check does the grid even exist
        if not grid:
            return 0

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r,c):
            #BFS is normally a queue
            q = collections.deque() #idk what this means
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1], [0,-1]]
                for dr, dc in directions: #goal is to check if there are any more ones in surronding area connected to that one so make sure its even in range and then if it is check if is a one and if it has not already been visited
                    r = row + dr
                    c = col + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r, c)) 
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

        