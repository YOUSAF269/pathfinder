#lists
nums=[10,20,30]
print(nums[0])
nums.append(40)
print(len(nums))
rows=[[0,0],[0,1]]
print(rows[1][1])
#loops
for n in nums:
  print(n)
for i in range(3):
  print(i)
#functions
def add(a,b):
  return a+b
print(add(2,3))
#excercise
l=[1,2,3,4,5]
for i in l:
  print(i)
def total(l):
  s=0
  for i in l:
    s=s+i
  return s
print(total(l))
l1=[[0,0,0],[0,0,0],[0,0,0]]
print(l1[2][1])
#build task grid
def make_grid(rows,cols):
  grid=[]
  for r in range(rows):
    row=[]
    for c in range(cols):
      row.append(0)
    grid.append(row)
  return grid
def print_grid(grid):
  for row in grid:
    line=""
    for cell in row:
      line=line+str(cell)+" "
    print(line)
grid=make_grid(5,5)
print_grid(grid)
print()
grid[2][2]=1
print_grid(grid)
