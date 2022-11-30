import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

gem_list = [list(map(int,input().split())) for _ in range(n)]
bag_list = [int(input()) for _ in range(k)]
gem_list.sort()
bag_list.sort()


result = 0
heap = []

for c in bag_list:
    #정렬 했기 때문에 뒤에 bag_list 뒤에 있는 값은 무조건 가방에 넣을수 있음.
    while gem_list and c >= gem_list[0][0]:
        heapq.heappush(heap, -gem_list[0][1])
        heapq.heappop(gem_list)
    if heap:
        result += heapq.heappop(heap)

print(-result)