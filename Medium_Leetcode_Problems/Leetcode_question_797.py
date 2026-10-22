
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:

        # ## Logic:
        # ## Start from node 0 and explore every possible path.
        # ## Use DFS (Depth-First Search) to visit connected nodes.
        # ## When the last node is reached, save the current path.
        # ## Backtrack to explore other possible paths.

        # ## Store all possible paths from node 0 to node n - 1.
        result = []

        # ## The last node is the destination.
        target = len(graph) - 1

        # ## Define a recursive DFS function.
        def dfs(node, path):

            # ## If the destination is reached, save this path.
            if node == target:
                result.append(path.copy())
                return

            # ## Explore every neighbor of the current node.
            for neighbor in graph[node]:

                # ## Add the neighbor to the current path.
                path.append(neighbor)

                # ## Recursively explore paths from this neighbor.
                dfs(neighbor, path)

                # ## Backtrack by removing the last node.
                # ## This allows exploration of another path.
                path.pop()

        # ## Start DFS from node 0.
        dfs(0, [0])

        # ## Return all discovered paths.
        return result


# ## Example:
# ## Input:
# ## graph = [[1, 2], [3], [3], []]
# ##
# ## Output:
# ## [[0, 1, 3], [0, 2, 3]]


# ## DRY RUN:
# ## Start with path = [0].
# ##
# ## Step 1: Visit neighbor 1.
# ## Path = [0, 1]
# ##
# ## Step 2: Visit neighbor 3.
# ## Path = [0, 1, 3]
# ## Node 3 is the destination, so save this path.
# ## Backtrack and remove node 3, then node 1.
# ##
# ## Step 3: Visit neighbor 2.
# ## Path = [0, 2]
# ##
# ## Step 4: Visit neighbor 3.
# ## Path = [0, 2, 3]
# ## Node 3 is the destination, so save this path.
# ##
# ## Final Output:
# ## [[0, 1, 3], [0, 2, 3]]


# ## ALGORITHM:
# ## Step 1: Create an empty result list.
# ## Step 2: Set target = len(graph) - 1.
# ## Step 3: Start DFS from node 0 with path [0].
# ## Step 4: If the current node is the target, save a copy of path.
# ## Step 5: Otherwise, visit each neighbor of the current node.
# ## Step 6: Append the neighbor to path and recursively call DFS.
# ## Step 7: Remove the neighbor after returning from DFS.
# ## Step 8: Return result after exploring all paths.


# ## INTERVIEW EXPLANATION:
# ## I use Depth-First Search (DFS) with backtracking.
# ## I start from node 0 and explore each possible neighbor.
# ## Whenever I reach the destination node n - 1,
# ## I save a copy of the current path.
# ## After exploring a branch, I remove its last node
# ## so I can explore other possible paths.
# ## Finally, I return all the paths found.


# ## KEY TRICK:
# ## path.append(neighbor) adds a node to the current path.
# ## path.pop() removes it during backtracking.
# ## path.copy() saves the path independently in the result.


# ## TIME AND SPACE COMPLEXITY:
# ## Let P be the number of paths and V be the number of nodes.
# ## Time Complexity: O(P * V) in the worst case for storing paths.
# ## Space Complexity: O(V) auxiliary space for recursion and the path,
# ## excluding the result list.
