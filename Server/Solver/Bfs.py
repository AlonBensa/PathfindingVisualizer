from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Helper import Helper

class Bfs:
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