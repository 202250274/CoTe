import sys
from collections import deque

# 입력 받기
n = int(input())
tree = [[] for _ in range(n+1)]  # 인접 리스트로 트리 표현

# 트리 연결 정보 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)  # 양방향 연결

# 각 노드의 부모를 저장할 배열
parent = [0] * (n+1)

# BFS를 사용하여 루트(1)에서부터 탐색하며 부모 노드 찾기
def find_parent():
    queue = deque([1])  # 루트 노드부터 시작
    visited = [False] * (n+1)
    visited[1] = True
    
    while queue:
        current = queue.popleft()
        
        for neighbor in tree[current]:
            if not visited[neighbor]:
                parent[neighbor] = current  # current는 neighbor의 부모
                visited[neighbor] = True
                queue.append(neighbor)

# 부모 노드 찾기 함수 실행
find_parent()

# 2번 노드부터 순서대로 부모 노드 출력
for i in range(2, n+1):
    print(parent[i])