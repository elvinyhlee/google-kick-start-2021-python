# Time Complexity: O(N)

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    S = input()

    current_score = sum(1 if S[ix] != S[N-ix-1] else 0 for ix in range(N // 2))

    print(f'Case #{t+1}:', abs(current_score - K))
