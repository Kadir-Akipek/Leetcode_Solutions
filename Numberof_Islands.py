class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rowNumber = len(grid)
        columnNumber = len(grid[0])
        
        visited = set()
        
        islandCounter = 0
        
        def bfs(row,column):
            myQueue = []
            
            visited.add((row,column))
            myQueue.append((row,column))
            
            
            while len(myQueue) != 0:
                row,column = myQueue.pop(0)
                myDirections = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for rowDirection, columnDirection in myDirections:
                    newRow = row + rowDirection
                    newColumn = column + columnDirection
                    
                    if(newRow in range(rowNumber) and
                      newColumn in range(columnNumber) and
                       grid[newRow][newColumn] == "1" and
                       (newRow, newColumn) not in visited):
                        myQueue.append((newRow, newColumn))
                        visited.add((newRow, newColumn))
                        
            
        for row in range(rowNumber):
            for column in range(columnNumber):
                if grid[row][column] == "1" and (row,column) not in visited:
                    bfs(row,column)
                    islandCounter += 1
                        
        return islandCounter