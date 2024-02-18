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
                        break

                return JSONResponse(status_code=200, content=traces)
            except:
                return JSONResponse(status_code=500, content="An error occured in BFS algorithm")
            

        @self.router.post("/dfs")
        def solve_with_dfs(array: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
            pass

        @self.router.post("/dijkstra")
        def solve_with_dijkstra(array: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
            pass

        @self.router.post("/A*")
        def solve_with_aStar(array: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
            pass

class Helper:
    def array_to_graph(array: list[list[int]]):
        graph = {(i, j): [] for i, row in enumerate(array) for j in range(len(row))}

        for i, row in enumerate(array):
            for j in range(len(row)):
                # Check if the current element is empty or is it a wall
                if array[i][j] != 0:
                    break

                # Check each side of the current element and if it's empty it will add it to the links in the graph
                if i+1 < len(array) and array[i][j] == 0 and array[i+1][j] == 0:
                    graph[(i, j)].append((i+1, j))
                if i-1 > 0 and array[i][j] == 0 and array[i-1][j] == 0:
                    graph[(i, j)].append((i-1, j))
                if j+1 < len(row) and array[i][j] == 0 and array[i][j+1] == 0:
                    graph[(i, j)].append((i, j+1))
                if j-1 > 0 and array[i][j] == 0 and array[i][j-1] == 0:
                    graph[(i, j)].append((i, j-1))

        return graph