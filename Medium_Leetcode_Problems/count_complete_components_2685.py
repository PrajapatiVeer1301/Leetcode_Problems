# Logic:
#
# 1. Build the graph using an adjacency list.
#
# 2. Use DFS to find every connected component.
#
# 3. Count the number of nodes in the component.
#
# 4. Count the total edges inside the component.
#
# 5. A complete component with k nodes
#    must have k * (k - 1) / 2 edges.
#
# 6. If actual edges equal expected edges,
#    increase the answer.
#
# 7. Return the final count.


# Algorithm:
#
# 1. Create an adjacency list.
#
# 2. Mark all nodes as unvisited.
#
# 3. Traverse every node.
#
# 4. If a node is unvisited,
#    perform DFS.
#
# 5. Collect all nodes in the component.
#
# 6. Count the number of edges.
#
# 7. Compare actual edges with expected edges.
#
# 8. If equal,
#    increment the answer.
#
# 9. Return the answer.

from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete = 0

        def dfs(node, component):
            visited[node] = True
            component.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, component)

        for i in range(n):

            if not visited[i]:

                component = []
                dfs(i, component)

                nodes = len(component)

                edge_count = 0

                for node in component:
                    edge_count += len(graph[node])

                edge_count //= 2

                expected = nodes * (nodes - 1) // 2

                if edge_count == expected:
                    complete += 1

        return complete
    
# Interview Explanation:
#
# 1. I first built the graph using an adjacency list.
#
# 2. Then I used DFS to find every connected component.
#
# 3. For each component,
#    I counted the number of nodes.
#
# 4. I also counted the total number of edges.
#
# 5. A complete graph with k nodes
#    must contain k*(k-1)/2 edges.
#
# 6. If the actual edges matched the expected edges,
#    I counted it as a complete component.
#
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)