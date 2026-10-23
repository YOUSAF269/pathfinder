#deque
from collections import deque
q=deque()
q.append("a")
q.append("b")
q.append("c")
print(q)
x=q.popleft()
print(x)
print(q)
print(len(q))
#exercise
q1=deque()
q1.append(1)
q1.append(2)
q1.append(3)
q1.popleft()
q1.popleft()
print(q1)
n=5
while n>0:
    print(n)
    n=n-1
q2=deque([1,2,3])
while q2:
    print(q2.popleft())
#bfs skeleton
def get_neighbours(grid,cell):
    r,c=cell
    rows=len(grid)
    cols=len(grid[0])
    result=[]
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    for dr,dc in directions:
        nr=r+dr
        nc=c+dc
        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!=1:
            result.append((nr,nc))
    return result
def bfs(grid,start):
    queue=deque([start])
    visited={start}
    order=[]
    while queue:
        cell=queue.popleft()
        order.append(cell)
        for i in get_neighbours(grid,cell):
            if i not in visited:
                visited.add(i)
                queue.append(i)
    return order
grid=[[0]*5 for _ in range(5)]
ans=bfs(grid,(0,0))
print(ans)
grid[2][2]=1
ans=bfs(grid,(0,0))
print(ans)