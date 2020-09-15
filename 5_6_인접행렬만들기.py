INF =9999999999

graph = [
    [0,7,5],    #0은
    [7,0,INF],  # INF는 노드간 연결되지 않아 갈 수 없는 부분 표현
    [5,INF,0]
]
print(graph)