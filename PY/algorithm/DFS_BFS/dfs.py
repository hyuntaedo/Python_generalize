#깊이 우선 탐색 (깊은 부분을 우선적으로 탐색하는 알고리즘이다)
#탐색 시작 노드를 스택에 넣고 방문
#인접노드가 있으면 그 노드를 스택에 넣고 방문처리
#방문하지않은것이없으면 그 스택에서 최 상단 노드를 꺼냄
def dfs_recursive(graph,v,visited=[]):
    visited.append(v) # start
    for node in graph[v]: #노드 탐색
        if node not in visited: # 방문을 해서 더 찾을게 없다면
            dfs_recursive(graph, v,visited) #다음 반복
    return visited 

dfs_recursive(graph, 'A')