class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visit = set()
        components = 0

        # DFS traversal (standard for undirected graph)
        def dfs(cur): 
            # Base case (until all nodes are visited)
            if cur in visit:
                return

            # Marking current node as visited
            visit.add(cur)
            for nei in graph[cur]:
                # Do not explore the nodes we have visited
                if nei not in visit:
                    dfs(nei)
            
        # Creating the undirected graph
        for cur, nei in edges:
            graph[cur].append(nei)
            graph[nei].append(cur)

        # Calling DFS on each node in the graph
        for i in range(n):
            if i not in visit:
                components += 1
                dfs(i)

        return components