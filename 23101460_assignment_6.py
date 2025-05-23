# -*- coding: utf-8 -*-
"""CSE221_Assignment_6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SDDSxKeQHi-QKTvdlXCMBSNHqoyoK9LB

A. Advising
"""

from collections import deque

n, m = input().split()
n, m = int(n), int(m)

adjList = [[] for _ in range (n+1)]
in_degree = [0]*(n+1)

for i in range (m):
    a, b = input().split()
    a, b = int(a), int(b)
    adjList[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range (1, n+1):
    if in_degree[i] == 0:
        q.append(i)

advisingOrder = []
while q:
    u = q.popleft()
    advisingOrder.append(u)
    for v in adjList[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            q.append(v)

if len(advisingOrder) != n:
    print(-1)
else:
    print(' '.join(map(str, advisingOrder)))

"""B. A Football Match"""

from collections import deque

n, m = map(int, input().split())

adjList = [[] for _ in range (n+1)]

for i in range (m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

visited = [0] * (n+1)
result = 0

for i in range (1, n+1):
    if visited[i] == 0:
        robot = 0
        human = 0
        q = deque([i])
        visited[i] = 1
        robot += 1
        bipartite = True

        while q and bipartite:
            u = q.popleft()
            for v in adjList[u]:
                if visited[v] == 0:
                    visited[v] = -visited[u]
                    if visited[v] == 1:
                        robot += 1
                    else:
                        human += 1
                    q.append(v)
                elif visited[v] == visited[u]:
                    bipartite = False

        if bipartite:
            result += max(robot, human)
        else:
            result += (robot + human)

print(result)

"""C. The Knight of Königsberg"""

from collections import deque

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

if not (1 <= x1 <= n and 1 <= y1 <= n and 1 <= x2 <= n and 1 <= y2 <= n):
    print(-1)
else:
    if (x1, y1) == (x2, y2):
        print(0)
    else:
        visited = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        visited[x1][y1] = 0
        q = deque()
        q.append((x1, y1, 0))
        found = False

        while q and not found:
            x, y, count = q.popleft()
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 1 <= nx <= n and 1 <= ny <= n and visited[nx][ny] == -1:
                    if (nx, ny) == (x2, y2):
                        print(count + 1)
                        found = True
                        break
                    visited[nx][ny] = count + 1
                    q.append((nx, ny, count + 1))

        if not found:
            print(-1)

"""D. Easy Tree Queries"""

import sys
sys.setrecursionlimit(2*10**5 + 5)

n, r = map(int, input().split())

adjList = [[] for _ in range (n+1)]

for i in range (n-1):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

treeSize = [0] * (n + 1)

def dfs(node, parent):
    size = 1
    for adj in adjList[node]:
        if adj != parent:
            size += dfs(adj, node)
    treeSize[node] = size
    return size

dfs(r, -1)

q = int(input())
for i in range(q):
    x = int(input())
    print(treeSize[x])

"""E. What's the Diameter?"""

from collections import deque

n = int(input())

adjList = [[] for _ in range (n+1)]

for i in range (n-1):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

def bfs(source):
    dist = [-1] * (n+1)
    dist[source] = 0
    q = deque([source])
    target = source
    diameter = 0

    while q:
        u = q.popleft()
        for v in adjList[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > diameter:
                    diameter = dist[v]
                    target = v

    return target, diameter

source, distance = bfs(1)
target, diameter = bfs(source)

print(diameter)
print(source, target)

"""F. An Ancient Ordering"""

from collections import defaultdict, deque

n = int(input())
words = []

for i in range (n):
    s = input()
    words.append(s)

graph = defaultdict(list)
in_degree = defaultdict(int)
chars = set()
valid = True

for i in range(n - 1):
    s1, s2 = words[i], words[i + 1]
    if len(s1) > len(s2) and s1[:len(s2)] == s2:
        valid = False
        break
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            graph[c1].append(c2)
            in_degree[c2] += 1
            chars.add(c1)
            chars.add(c2)
            break

if not valid:
    print(-1)
else:
    for word in words:
        chars.update(word)

    queue = deque([c for c in sorted(chars) if c not in in_degree])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        queue = deque(sorted(queue))

    if len(result) != len(chars):
        print(-1)
    else:
        print(''.join(result))

n = int(input())
words = [input().strip() for i in range(n)]

graph = [[] for i in range(26)]
indegree = [0] * 26
visited = [False] * 26

for word in words:
    for _ in word:
        visited[ord(_) - ord('a')] = True

for i in range(n - 1):
    w1, w2 = words[i], words[i + 1]
    minLen = min(len(w1), len(w2))
    found = False
    for j in range(minLen):
        if w1[j] != w2[j]:
            a = ord(w1[j]) - ord('a')
            b = ord(w2[j]) - ord('a')
            if b not in graph[a]:
                graph[a].append(b)
                indegree[b] += 1
            found = True
            break
    if not found and len(w1) > len(w2):
        print(-1)

result = []
for i in range(26):
    added = False
    for i in range(26):
        if visited[i] and indegree[i] == 0:
            result.append(chr(i + ord('a')))
            indegree[i] = -1
            for adj in graph[i]:
                indegree[adj] -= 1
            added = True
            break
    if not added:
        break

if len(result) == sum(visited):
    print("".join(result))
else:
    print(-1)
