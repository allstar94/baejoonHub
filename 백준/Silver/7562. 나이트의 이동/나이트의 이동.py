from collections import deque
N = int(input())

def bfs():
    queue = deque()
    queue.append([startX,startY])

    dx = [2,1,-2,-1,2,-1,-2,1]
    dy = [1,2,-1,-2,-1,2,1,-2]

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] +1
                    queue.append([nx,ny])

for _ in range(N):
    M = int(input())
    graph = [[0 for _ in range(M)] for _ in range(M)]

    startX, startY = map(int,input().split())
    endX, endY = map(int, input().split())

    graph[startX][startY] = 1

    bfs()
    print(graph[endX][endY]-1)