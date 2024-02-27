class GeneratorHelper:
    def generate_empty_maze(width: int, height: int):
        if width % 2 == 0: width = width * 2 - 1
        else: width = width * 2 + 1
        if height % 2 == 0: height = height * 2 - 1
        else: height = height * 2 + 1
        
        maze = [[1 for _ in range(width)] for _ in range(height)]
        return maze