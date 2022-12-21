from collections import deque
def bfs(start):
    queue = deque([start])
    # 처음 방문 완료
    visited[start] = True
    while queue:
        # 출력 할 왼쪽 거 1개 빼기
        v = queue.popleft()
        print(v, end=' ')
        # print(queue)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],         # 인접행렬
    [2, 3, 8],  # 01100001
    [1, 7],     # 10000010
    [1, 4, 5],  # 10011000
    [3, 5],     # 00101000
    [3, 4],     # 00110000
    [7],        # 00000010
    [2, 6, 8],  # 01000101
    [1, 7]      # 10000010
]

visited = [False] * 9
bfs(1)

