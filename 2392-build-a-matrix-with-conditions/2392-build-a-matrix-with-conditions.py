class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        row_iterator,col_iterator = set(),set()
        for above,blow in rowConditions:
            row_graph[blow].append(above)
            row_iterator.update({above,blow})
        for left,right in colConditions:
            col_graph[right].append(left)
            col_iterator.update({left,right})
        row = []
        done = set()
        def dfs(num):
            if num in done:
                return True
            if num in cycle:
                return False
            cycle.add(num)
            for i in row_graph[num]:
                if not dfs(i):
                    return False
            cycle.remove(num)
            done.add(num)
            row.append(num)
            return True
        for i in row_iterator:
            cycle = set()
            if not dfs(i):
                return []
        col = []
        done = set()
        def dfs(num):
            if num in done:
                return True
            if num in cycle:
                return False
            cycle.add(num)
            for i in col_graph[num]:
                if not dfs(i):
                    return False
            cycle.remove(num)
            done.add(num)
            col.append(num)
            return True
        for i in col_iterator:
            cycle = set()
            if not dfs(i):
                return []
        dic = {}
        for i in range(len(row)):
            dic[row[i]] = [i,-1]
        for i in range(len(col)):
            if col[i] in dic:
                dic[col[i]][1] = i
            else:
                dic[col[i]] = [-1,i]
        grid = [[0 for i in range(k)] for j in range(k)]
        current_col,current_row = 0,0
        for i in dic:
            r,c = dic[i]
            if r == -1:
                r = current_row
            if c == -1:
                c = current_col
            grid[r][c] = i
            current_col,current_row = c+1,r+1
        for i in range(1,k+1):
            if i not in dic:
                grid[current_row][current_col] = i
                current_col += 1
                current_row += 1
        return grid
        