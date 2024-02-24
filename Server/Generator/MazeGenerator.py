from fastapi import APIRouter

class Algorithms:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

        @self.router.post("/Randomized-DFS")
        def randomized_DFS(widht: int, height: int):
            pass

        @self.router.post("/Iterative-randomized-Kruskals")
        def iterative_randomized_Kruskals(widht: int, height: int):
            pass

        @self.router.post("/Iterative-randomized-Prims")
        def iterative_randomized_Prims(widht: int, height: int):
            pass
        
        @self.router.post("/Recursive-division")
        def recursive_division(widht: int, height: int):
            pass

        @self.router.post("/Sidewinder")
        def sidewinder(widht: int, height: int):
            pass

        @self.router.post("/Wilsons")
        def Wilsons(widht: int, height: int):
            pass

        @self.router.post("/Aldous-Broder")
        def Aldous_Broder(widht: int, height: int):
            pass

        @self.router.post("/Tessellation")
        def tessellation (widht: int, height: int):
            pass