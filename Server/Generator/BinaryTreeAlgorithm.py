from fastapi import APIRouter
from fastapi.responses import JSONResponse
import random

from Generator.Helper import GeneratorHelper

UP = 1
LEFT = 0

class BinaryTreeAlgorithm:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/Binary-Tree")
        def binary_tree(width: int, height: int):
            maze = GeneratorHelper.generate_empty_maze(width, height)
            width, height =  len(maze), len(maze[0])
            traces = []

            for y in range(height):
                for x in range(width):
                    # Skip walls
                    if x % 2 == 1: continue
                    if y % 2 == 1: break
                    
                    # Mark as visited current node
                    maze[y][x] = 0
                    traces.append((y, x))
                    if x == 0 and y == 0: continue
                    
                    # Choose direction to go next (up or left) and remove wall between them
                    direction = self.flip_coin((x, y))
                    if direction == UP:
                        maze[y-1][x] = 0
                        traces.append((y-1, x))
                    elif direction == LEFT:
                        maze[y][x-1] = 0
                        traces.append((y, x-1))

            return JSONResponse(status_code=200, content={"traces": traces, "maze": maze})
    
    def flip_coin(self, indexes):
        x, y = indexes
        if y == 0: return LEFT
        if x == 0: return UP
        return random.choice([LEFT, UP])