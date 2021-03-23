# Time Complexity: O(N^2)


def prim_mst(graph, nodes):
    # reference: https://cp-algorithms.com/graph/mst_prim.html#toc-tgt-5
    result = 0
    n = len(nodes)
    max_edge = [0] * n
    selected = [False] * n
    for _ in range(n):
        target = -1
        for k in range(n):
            if not selected[k] and (target == -1 or max_edge[k] > max_edge[target]):
                target = k
        selected[target] = True

        result += max_edge[target]
        for k in range(n):
            max_edge[k] = max(graph[nodes[target]][nodes[k]], max_edge[k])

    return result


T = int(input())

for t in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]
    R = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # First N nodes = rows
    # N nodes after = columns
    cost_graph = [[0] * (2 * N) for _ in range(2 * N)]
    total_cost_of_unknowns = 0
    nodes_with_unknowns = set()
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                cost_graph[i][j+N] = cost_graph[N+j][i] = B[i][j]
                nodes_with_unknowns.add(i)
                nodes_with_unknowns.add(j+N)
                total_cost_of_unknowns += B[i][j]

    ans = total_cost_of_unknowns - prim_mst(cost_graph, list(nodes_with_unknowns))

    print(f'Case #{t+1}:', ans)
