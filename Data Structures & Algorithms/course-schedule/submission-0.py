class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Assumptions
        # If there is no pre-req defined for the course, you can take it
        # Pseudocode
        # 1. Convert the list to a graph (as a hashmap), node -> pre,requisites
        # 2. Check for cycles in the graph.

        graph = defaultdict(list)
        path = set()

        # Checking for cycles: Going through the pre-requisites one by one
        # Check the key value, and each prereq
        # Recursively check the prereq
        # Failure case: prereq contains itself
        # If reaches NULL, return True
        def dfs(cur):
            # base case (success case): empty prereq list
            if graph[cur] == []:
                return True
            # base case (failure case): cycle identified
            if cur in path:
                return False
            
            # Calling dfs function on all the neighbors
            path.add(cur)

            for prereq in graph[cur]:
                if not dfs(prereq):
                    return False
            
            # Cleaning up the path
            path.pop()
            
            # Modifying prereq to be empty
            graph[cur] = []

            return True

        # Creating the graph
        for node, prereq in prerequisites:
            graph[node].append(prereq)

        # Checking all the nodes
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True