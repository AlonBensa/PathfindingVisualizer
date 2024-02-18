from fastapi import APIRouter

class Algorithms:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/bfs")
        def solve_with_bfs(array: list[list]):
            pass

        @self.router.post("/dfs")
        def solve_with_bfs(array: list[list]):
            pass

        @self.router.post("/dijkstra")
        def solve_with_bfs(array: list[list]):
            pass

        @self.router.post("/A*")
        def solve_with_bfs(array: list[list]):
            pass