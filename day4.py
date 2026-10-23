from collections import deque
#comparing results
print((1,1)==(1,1))
print((1,1)==(1,2))
#returning two values
def min_max(nums):
    return min(nums),max(nums)
lo,hi=min_max([4,9,12])
print(lo,hi)
#stopping early
def find(nums,target):
    for n in nums:
        if n==target:
            return True
    return False
print(find([1,2,3],2))
print(find([1,4,5],6))
#exercise
def min_max(nums):
    a=nums[0]
    for i in nums:
        if i<a:
            a=i
    a1=nums[0]
    for i in nums:
        if i>a1:
            a1=i
    return a,a1
mi,ma=min_max([1,5,8])
print(mi,ma)
def find_index(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
print(find_index([1,2,4],4))
print((2,3)==(2,3))
print((2,3)==(3,2))
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
def bfs(grid,start,goal):
    queue=deque([start])
    visited={start}
    order=[]
    while queue:
        cell=queue.popleft()
        order.append(cell)
        if cell==goal:
            return order,True
        for i in get_neighbours(grid,cell):
            if i not in visited:
                visited.add(i)
                queue.append(i)
    return order,False
grid=[[0]*3 for _ in range(3)]
print(bfs(grid,(0,0),(1,1)))
print(bfs(grid,(0,0),(0,0)))
grid[0][1]=1
grid[1][0]=1
print(bfs(grid,(0,0),(2,2)))
order,found=bfs(grid,(0,0),(2,2))
print(len(order),found)