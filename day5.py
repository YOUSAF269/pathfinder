from collections import deque
#walking backward with a while loop
parent={"c":"b","b":"a","a":None}
node="c"
while node is not None:
    print(node)
    node=parent[node]
#reverse a list
path=["c","b","a"]
path.reverse()
print(path)
#exercise
parents={"c":"b","b":"a","a":None}
node1="c"
l=[]
while node1 is not None:
    l.append(node1)
    node1=parents[node1]
l.reverse()
print(l)
def walk_back(parents,end):
    l1=[]
    while end is not None:
        l1.append(end)
        end=parents[end]
    l1.reverse()
    return l1
ans=walk_back({"c":"b","b":"a","a":None},"c")
print(ans)
#build task
def build_path(came_from,goal):
    path=[]
    cell=goal
    while cell is not None:
        path.append(cell)
        cell=came_from[cell]
        pass
    path.reverse()
    return path
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
def bfs(grid,start,goal):
    queue=deque([start])
    visited={start}
    came_from={start:None}
    order=[]
    while queue:
        cell=queue.popleft()
        order.append(cell)
        if cell==goal:
            return order,build_path(came_from,goal)
        for i in get_neighbours(grid,cell):
            if i not in visited:
                visited.add(i)
                came_from[i]=cell
                queue.append(i)
    return order,[]
grid=[[0]*3 for _ in range(3)]
order,path=bfs(grid,(0,0),(2,2))
print(path)
print(bfs(grid,(0,0),(0,0))[1])
grid[1][1]=1
order,path=bfs(grid,(0,0),(2,2))
print(len(path))
grid[0][1]=1
grid[1][0]=1
order,path=bfs(grid,(0,0),(2,2))
print(path)