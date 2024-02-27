class Helper:
    def array_to_graph(array: list[list[int]]):
        graph = {(i, j): [] for i, row in enumerate(array) for j in range(len(row))}

        for i, row in enumerate(array):
            for j in range(len(row)):
                # Check if the current element is empty or is it a wall
                if array[i][j] != 0:
                    continue

                # Check each side of the current element and if it's empty it will add it to the links in the graph
                if i+1 < len(array) and array[i][j] == 0 and array[i+1][j] == 0:
                    graph[(i, j)].append((i+1, j))
                if i-1 >= 0 and array[i][j] == 0 and array[i-1][j] == 0:
                    graph[(i, j)].append((i-1, j))
                if j+1 < len(row) and array[i][j] == 0 and array[i][j+1] == 0:
                    graph[(i, j)].append((i, j+1))
                if j-1 >= 0 and array[i][j] == 0 and array[i][j-1] == 0:
                    graph[(i, j)].append((i, j-1))

        return graph
    
    def estimate_dist(pos1: tuple[int, int], pos2: tuple[int, int]):
        (i1, j1) = pos1
        (i2, j2) = pos2
        dx = j2 - j1
        dy = i2 - i1
        return abs(dx) + abs(dy)