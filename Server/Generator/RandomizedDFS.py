from fastapi import APIRouter
from fastapi.responses import JSONResponse
import random

from Generator.Helper import GeneratorHelper

class RandomizedDFS:
    def __init__(self):
        self.router = APIRouter()
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/Iterative-Randomized-DFS")
        def iterative_randomized_dfs(width: int, height: int):
            maze = GeneratorHelper.generate_empty_maze(width, height)
            width, height =  len(maze), len(maze[0])
            traces = []

            stack = [(0, 0)]
            visited = {(x, y): False for y in range(height) for x in range(width)}
            visited[(0, 0)] = True
            maze[0][0] = 0

            while stack:
                node = stack.pop()

                # Get the neighbors of the current node and add them to the stack
                possible_directions = self.get_possible_directions(node, width, height, visited)
                for possible_direction in possible_directions:
                    stack.append(possible_direction)
                
                if not possible_directions:
                    continue
                
                # Choose a random direction from the possible directions and make it as the next node
                direction = random.choice(possible_directions)
                stack.remove(direction)
                stack.append(direction)

                # Mark as visited the next node and update its value on the maze and remove the wall between the current and next node
                traces.append(direction)
                visited[direction] = True
                x, y = direction
                maze[y][x] = 0
                x, y = self.get_mid_direction(node, direction)
                maze[y][x] = 0

            return JSONResponse(status_code=200, content={"traces": traces, "maze": maze})

        @self.router.post("/Recursive-Randomized-DFS")
        def recursive_randomized_dfs(width: int, height: int):
            pass

    def get_possible_directions(self, indexes, width, height, visited):
        x, y = indexes
        possible_directions = []

        # Iterate though neighbors of current node without taking attentions to the walls
        for neighbor in [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]:
            if not self.is_valid(neighbor, width, height, visited):
                continue

            possible_directions.append(neighbor)

        return possible_directions

    def is_valid(self, indexes, width, height, visited):
        x, y = indexes

        if (x < 0) or (y < 0) or (x >= width) or (y >= height) or (visited[indexes] == True):
            return False
        
        return True
    
    def get_mid_direction(self, start, end):
        start_x, start_y = start
        end_x, end_y = end
        mid_x = int((start_x + end_x) / 2)
        mid_y = int((start_y + end_y) / 2)
        return (mid_x, mid_y)