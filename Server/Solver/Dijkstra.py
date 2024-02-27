import sys
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Solver.Helper import Helper

class Dijkstra:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
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