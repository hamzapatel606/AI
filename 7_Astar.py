import heapq

def is_valid(row, col):
    return 0 <= row < ROW and 0 <= col < COL

def is_unblocked(grid, row, col):
    return grid[row][col] == 1

def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

def trace_path(parents, dest):
    print("The Path is ")
    path = []
    while dest in parents:
        path.append(dest)
        dest = parents[dest]
    path.reverse()
    for i in path:
        print("->", i, end=" ")
    print()

def a_star_search(grid, src, dest):
    if not (is_valid(src[0], src[1]) and is_valid(dest[0], dest[1])):
        print("Source or destination is invalid")
        return
    if not (is_unblocked(grid, src[0], src[1]) and is_unblocked(grid, dest[0], dest[1])):
        print("Source or the destination is blocked")
        return

    closed_set = set()
    parents = {}
    open_list = [(0, src)]
    found_dest = False

    while open_list:
        f, (i, j) = heapq.heappop(open_list)
        if is_destination(i, j, dest):
            print("The destination cell is found")
            trace_path(parents, dest)
            found_dest = True
            return
        closed_set.add((i, j))
        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_i, new_j = i + dir[0], j + dir[1]
            if (is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and 
                (new_i, new_j) not in closed_set):
                g_new = f + 1.0
                h_new = calculate_h_value(new_i, new_j, dest)
                f_new = g_new + h_new
                heapq.heappush(open_list, (f_new, (new_i, new_j)))
                parents[(new_i, new_j)] = (i, j)

    if not found_dest:
        print("Failed to find the destination cell")

ROW, COL = 9, 10

grid = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
]
src, dest = (8, 0), (0, 0)

a_star_search(grid, src, dest)
