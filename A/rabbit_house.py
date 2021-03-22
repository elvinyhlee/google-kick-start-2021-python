# Time complexity: O(R*C)


import copy

T = int(input())


def number_of_boxes_added(r, c, grid, original_grid):
    num = 0
    for ix in range(r):
        for jx in range(c):
            num += grid[ix][jx] - original_grid[ix][jx]
    return num


def update_grid(r, c, grid):
    updated_grid = copy.deepcopy(grid)

    # left/right[i][j] and top/bottom[j][i] are the
    # max(all cell's (height - distance) along the respective direction) of cell [i][j]
    left = []  # R X C
    for ix in range(r):
        row = []
        max_height = 0
        for jx in range(c):
            if grid[ix][jx] >= max_height:
                max_height = grid[ix][jx]
            row.append(max_height)
            max_height -= 1
        left.append(row)

    right = []  # R X C
    for ix in range(r):
        row = []
        max_height = 0
        for jx in range(c):
            if grid[ix][c - jx - 1] >= max_height:
                max_height = grid[ix][c - jx - 1]
            row.append(max_height)
            max_height -= 1
        row.reverse()
        right.append(row)

    top = []  # C X R
    for jx in range(c):
        column = []
        max_height = 0
        for ix in range(r):
            if grid[ix][jx] >= max_height:
                max_height = grid[ix][jx]
            column.append(max_height)
            max_height -= 1
        top.append(column)

    bottom = []  # C X R
    for jx in range(c):
        column = []
        max_height = 0
        for ix in range(r):
            if grid[r - ix - 1][jx] >= max_height:
                max_height = grid[r - ix - 1][jx]
            column.append(max_height)
            max_height -= 1
        column.reverse()
        bottom.append(column)

    for ix in range(r):
        for jx in range(c):
            updated_grid[ix][jx] = max(top[jx][ix], bottom[jx][ix], left[ix][jx], right[ix][jx])

    return updated_grid


for t in range(T):
    R, C = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(R)]

    NG = copy.deepcopy(G)
    for _ in range(2):
        NG = update_grid(R, C, NG)

    print(f'Case #{t+1}:', number_of_boxes_added(R, C, NG, G))
