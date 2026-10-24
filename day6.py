import time
#timing code with time
t0=time.perf_counter()
total=0
for i in range(1000000):
    total=total+i
t1=time.perf_counter()
print((t1-t0)*1000)
#import from your own files
from day4 import bfs
#returning a dict
result={"path":[1,2],"time_ms":0.5}
print(result["path"])
print(result["time_ms"])
#exercise
t2=time.perf_counter()
s=0
for i in range(100000):
    s=s+1
t3=time.perf_counter()
print((t3-t2)*1000)
from day5 import double
#dict
d={"name":"yousaf","age":19}
print(d["name"],d["age"])
#build task
from algorithms import bfs
grid = [[0] * 3 for _ in range(3)]
result = bfs(grid, (0, 0), (2, 2))
print(len(result["path"]))    
print(len(result["order"]))   
print(result["time_ms"])      
grid[1][1] = 1
result = bfs(grid, (0, 0), (2, 2))
print(len(result["path"]))    
print(len(result["order"]))   
grid[0][1] = 1
grid[1][0] = 1
result = bfs(grid, (0, 0), (2, 2))
print(result["path"])         
