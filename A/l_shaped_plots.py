# Time Complexity: O(R*C)


def number_of_l_shapes(len_1, len_2):
    if len_1 <= 1 or len_2 <= 1:
        return 0

    return min(len_1 // 2, len_2) + min(len_1, len_2 // 2) - 2


T = int(input())


for t in range(T):
    R, C = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(R)]

    # left/right/top/bottom[i][j] is the length of the respective segment when [i][j] is the endpoint
    left = []
    for i in range(R):
        row = [G[i][0]]
        for j in range(1, C):
            row += [0 if G[i][j] == 0 else row[j-1] + 1]
        left.append(row)

    right = []
    for i in range(R):
        revered_row = list(reversed(G[i]))
        row = [revered_row[0]]
        for j in range(1, C):
            row += [0 if revered_row[j] == 0 else row[j-1] + 1]
        right.append(list(reversed(row)))

    top = [[G[0][j] for j in range(C)]]
    for i in range(1, R):
        row = [
            0 if G[i][j] == 0 else top[i - 1][j] + 1
            for j in range(C)
        ]
        top.append(row)

    bottom = [[G[R-1][j] for j in range(C)]]
    for i in range(1, R):
        row = [
            0 if G[R - i - 1][j] == 0 else bottom[i - 1][j] + 1
            for j in range(C)
        ]
        bottom.append(row)
    bottom.reverse()

    ans = 0
    for i in range(R):
        for j in range(C):
            ans += number_of_l_shapes(top[i][j], right[i][j]) \
                   + number_of_l_shapes(top[i][j], left[i][j]) \
                   + number_of_l_shapes(bottom[i][j], right[i][j]) \
                   + number_of_l_shapes(bottom[i][j], left[i][j])

    print(f'Case #{t+1}:', ans)
