import sys
from fastapi import APIRouter
from fastapi.responses import JSONResponse

class Algorithms:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/bfs")
        def solve_with_bfs(array: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
            try:
                # Initialize variables for BFS algorithm
                graph = Helper.array_to_graph(array)
                traces = []
                visited = {(i, j): False for i, row in enumerate(array) for j in range(len(row))}
                queue = [start]
                visited[start] = True
                found = False

                # Run on all the elements in the array until it finds the target
                while queue:
                    node = queue.pop(0)

                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            traces.append(neighbor)

                            if neighbor == end:
                                found = True
                                break

                    if found:
                        return JSONResponse(status_code=200, content=traces)

                return JSONResponse(status_code=500, content="No path found")
            except Exception as e:
                return JSONResponse(status_code=500, content=f"An error occured in BFS algorithm: {e}")
            

        @self.router.post("/dfs")
        def solve_with_dfs(array: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
            try:
                # Initialize variables for DFS algorithm
                graph = Helper.array_to_graph(array)
                traces = []
                visited = {(i, j): False for i, row in enumerate(array) for j in range(len(row))}
                stack = [start]
                visited[start] = True
                found = False

                # Run on all the elements in the array until it finds the target
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                            traces.append(neighbor)

                            if neighbor == end:
                                found = True
                                break

                    if found:
                        return JSONResponse(status_code=200, content=traces)

                return JSONResponse(status_code=500, content="No path found")
            except Exception as e:
                return JSONResponse(status_code=500, content=f"An error occured in DFS algorithm: {e}")

        @self.router.post("/dijkstra")
        def solve_with_dijkstra(array: list[list[int]], start: tuple[int, int]):
            try:
                # Initialize variables for Dijkstra algorithm
                graph = Helper.array_to_graph(array)
                traces = {}
                visited = {(i, j): False for i, row in enumerate(array) for j in range(len(row))}
                # Save the shortest steps to a specific place
                shortest_table = {(i, j): sys.maxsize for i, row in enumerate(array) for j in range(len(row))}
                shortest_table[start] = 0
                all_nodes = set([start])

                # Run until all the elements in the array are visited
                while any(not visited[node] for node in all_nodes):
                    # Search the not visited element with the lowest steps
                    min_val = sys.maxsize
                    saved_idx = ()
                    for key, val in shortest_table.items():
                        if not visited[key]:
                            min_val = min(min_val, val)
                            if min_val == val: saved_idx = key

                    # Run on the neighbors of the element with the lowest steps and update the shortest table
                    visited[saved_idx] = True
                    for neighbor in graph[saved_idx]:
                        all_nodes.add(neighbor)
                        
                        if shortest_table[saved_idx] + 1 < shortest_table[neighbor]:
                            shortest_table[neighbor] = shortest_table[saved_idx] + 1
                            traces[neighbor] = shortest_table[neighbor]

                converted_traces = {str(key): value for key, value in traces.items()}
                return JSONResponse(status_code=200, content=converted_traces)
            except Exception as e:
                return JSONResponse(status_code=500, content=f"An error occured in Dijkstra algorithm: {e}")

        @self.router.post("/A*")
        def solve_with_aStar(array: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
            try:
                # Initialize variables for A* algorithm
                graph = Helper.array_to_graph(array)
                table = {(i, j): {"f_score": sys.maxsize, "g_score": sys.maxsize} for i, row in enumerate(array) for j in range(len(row))}
                table[start]["f_score"] = Helper.estimate_dist(start, end)
                table[start]["g_score"] = 0
                open = [start]
                traces = {}

                while open:
                    # Find the next minimum node to explore from the open nodes
                    current_node = open[0]
                    for node in open:
                        if table[node]["f_score"] < table[current_node]["f_score"]:
                            current_node = node
                    open.remove(current_node)
                    traces[current_node] = {}

                    if current_node == end:
                        break
                    
                    # Pass over the current node neighbors and change their data based on the current node's g score
                    for neighbor in graph[current_node]:
                        new_gscore = table[current_node]["g_score"] + 1

                        if new_gscore < table[neighbor]["g_score"]:
                            open.append(neighbor)
                            table[neighbor]["f_score"] = Helper.estimate_dist(neighbor, end) + new_gscore
                            table[neighbor]["g_score"] = new_gscore
                            traces[current_node][neighbor] = table[neighbor]
                
                # Convert traces to a format that is serializable
                converted_traces = {}
                for node, neighbors in traces.items():
                    converted_traces[str(node)] = {}
                    for neighbor, value in neighbors.items():
                        converted_traces[str(node)][str(neighbor)] = value
                
                return JSONResponse(status_code=200, content=converted_traces)
            except Exception as e:
                return JSONResponse(status_code=500, content=f"An error occured in A* algorithm: {e}")
        

class Helper:
    def array_to_graph(array: list[list[int]]):
        graph = {(i, j): [] for i, row in enumerate(array) for j in range(len(row))}

        for i, row in enumerate(array):
            for j in range(len(row)):
                # Check if the current element is empty or is it a wall
                if array[i][j] != 0:
                    continue

                # Check each side of the current element and if it's empty it will add it to the links in the graph
                if i+1 < len(array) and array[i][j] == 0 and array[i+1][j] == 0:
                    graph[(i, j)].append((i+1, j))
                if i-1 >= 0 and array[i][j] == 0 and array[i-1][j] == 0:
                    graph[(i, j)].append((i-1, j))
                if j+1 < len(row) and array[i][j] == 0 and array[i][j+1] == 0:
                    graph[(i, j)].append((i, j+1))
                if j-1 >= 0 and array[i][j] == 0 and array[i][j-1] == 0:
                    graph[(i, j)].append((i, j-1))

        return graph
    
    def estimate_dist(pos1: tuple[int, int], pos2: tuple[int, int]):
        (i1, j1) = pos1
        (i2, j2) = pos2
        dx = j2 - j1
        dy = i2 - i1
        return abs(dx) + abs(dy)