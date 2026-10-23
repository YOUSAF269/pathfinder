#tuples
cell=(2,3)
r,c=cell
print(r,c)
#set
visited=set()
visited.add((0,0))
visited.add((0,0))
print((0,0) in visited)
print((1,1) in visited)
print(len(visited))
#dictionary
came_from={}
came_from[(0,1)]=(0,0)
print(came_from[(0,1)])
print((0,5) in came_from)
#nested loop over cell
grid=[[0,0,0],[0,1,0],[0,0,0]]
for r in range(len(grid)):
    for c in range(len(grid[0])):
        print(r,c,grid[r][c])
#directions
directions=[(-1,0),(1,0),(0,-1),(0,1)]
for dr,dc in directions:
    print(dr,dc)
#exercise
l=(4,7)
a,b=l
print(a,b)
l1=set()
l1.add((0,0))
l1.add((0,1))
l1.add((0,0))
print(len(l1))
l2=[[1,0,0],[0,1,0],[0,0,1]]
c=0
for i in range(len(l2)):
    for j in range(len(l2[i])):
        if l2[i][j]==1:
            c=c+1
print(c)
l3={}
l3[(0,1)]=(0,0)
l3[(0,2)]=(0,1)
print(l3[(0,2)])
#build task
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
grid=[[0]*5 for _ in range(5)]
grid[2][2]=1
print(get_neighbours(grid,(0,0)))
print(get_neighbours(grid,(2,1)))