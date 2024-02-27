import sys
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Solver.Helper import Helper

class Astar:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
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