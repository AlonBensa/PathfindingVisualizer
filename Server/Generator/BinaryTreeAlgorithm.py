from fastapi import APIRouter
from fastapi.responses import JSONResponse

import random

UP = 1
LEFT = 0

class BinaryTreeAlgorithm:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/Binary-Tree")
        def binary_tree(width: int, height: int):
            maze = self.generate_empty_maze(width, height)
            traces = []

            for y, row in enumerate(maze):
                for x in range(len(row)):
                    if len(row) % 2 == 0:
                        if x % 2 == 1 and y < height - 1:
                            continue
                    else:
                        if x % 2 == 1: continue

                    if len(maze) % 2 == 0:
                        if y % 2 == 1 and x < width - 1:
                            continue
                    else:
                        if y % 2 == 1: break

                    maze[y][x] = 0
                    traces.append((y, x))
                    if x == 0 and y == 0: continue
                    
                    direction = self.flip_coin((x, y))
                    if direction == UP:
                        maze[y-1][x] = 0
                        traces.append((y-1, x))
                    elif direction == LEFT:
                        maze[y][x-1] = 0
                        traces.append((y, x-1))

            return JSONResponse(status_code=200, content={"traces": traces, "maze": maze})

    def generate_empty_maze(self, width: int, height: int):
        maze = [[1 for _ in range(width)] for _ in range(height)]
        return maze
    
    def flip_coin(self, indexes):
        x, y = indexes
        if y == 0: return LEFT
        if x == 0: return UP
        return random.choice([LEFT, UP])