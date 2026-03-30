class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        graph = defaultdict(list)

        def dfs(cur, prev):
           # failure cases
           # self loop or discovered a new edge
           if cur in visit:
             return 0
            
           visit.add(cur)
           # recursive case: visiting each unvisited neighbor
           for nei in graph[cur]:
             if nei == prev:
               continue
            
             if dfs(nei, cur) == 0:
               return 0

           return len(visit)

        # Creating a graph
        # Assumption: there are no duplicate nodes
        for cur, nei in edges:
            # Adding connection from cur -> nei
            graph[cur].append(nei)
            # Adding connection from nei -> cur
            graph[nei].append(cur)

        # Call dfs on a random graph node
        res = dfs(0, -1)

        # Checking if visited nodes count is less or equal. Return accordingly
        # True if visited is equal to path length
        return res == n