class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build adjacency list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()  # tracks nodes in current DFS path

        def dfs(crs):
            
            # if already in current path → cycle
            if crs in visit:
                return False

            # if no prerequisites → safe
            if preMap[crs] == []:
                return True

            # mark as visiting
            visit.add(crs)

            # explore all prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # remove from current path
            visit.remove(crs)

            # mark as completed (optimization)
            preMap[crs] = []

            return True

        # check all courses
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True