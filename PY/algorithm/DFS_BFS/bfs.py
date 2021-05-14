#너비 우선 탐색(그래프에서 가까운노드부터 우선 탐색)
#큐 구조를 이용
#1. 탐색노드를 큐에 삽입하고 방문처리
#2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접노드 중 방문하지 않은 노드를
# 가장가까운 노드를 모두 큐에 삽입->방문처리
#3. 2의 과정을 반복
#특정 조건에서의 최단경로로 쓰임(간선이 동일할 때)
#자주나옴
from collections import deque
def bfs_recursive(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end='')
        for i in graph[start]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True