from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0 , left= None, right=None):
        self.left= left
        self.right= right
        self.val = val

n= int(input())
adjList = defaultdict(list)
for i in range(n-1):
    a, b=map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
def bfs(start):
    queue = deque()
    queue.append(start)
    vis = set()
    dist= [0 for i in range(n+1)]

    vis.add(start)
    dist[start] = 0
    farthestNode= 0
    dis= 0
    while queue:
        node = queue.popleft()
        for neib in adjList[node]:
            if neib not in vis:
                vis.add(neib)
                queue.append(neib)
                if dist[neib]<dist[node]+1:
                    dist[neib]= 1+dist[node]
                    farthestNode = neib
    # print(dist)
    return farthestNode, dist
res= [0]*(n+1)
# for i in range(1, n+1):
farthNode, distFromFirst = bfs(1)
print(distFromFirst)
secondFarthestNode , distFromFarthestNode = bfs(farthNode)
_, distFromSecondFarthestNode= bfs(secondFarthestNode)

for i in range(n+1):
    res[i]= max(distFromFarthestNode[i], distFromSecondFarthestNode[i])

    # res.append(distanceOfFarthestNode)
print(*res[1:])