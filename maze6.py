import numpy as np
N = 6
m= np.arange(1, N*N + 1).reshape(N, N)

print (m)
block_cells = {(1, 0), (1, 1),(3, 1), (3, 2), (3, 3),(4, 4),(5, 1)}
print ("Blocked celss:",block_cells)

print("\nMaze view (██ = blocked):")
for i in range(N):
    row = ""
    for j in range(N):
        if (i, j) in block_cells:
            row += "██  "
        else:
            row += f"{m[i, j]:3d} "
    print(row)

start = (0, 0)    
end   = (5, 5)

visited = []
rows = N
cols = N
visited = np.zeros((N, N), dtype=int)

shortest_path = []
shortest_len  = float('inf')

def move(i, j, direction):
    if direction == "north": 
      return i-1, j
    if direction == "south": 
      return i+1, j
    if direction == "west": 
       return i, j-1
    if direction == "east":  
      return i, j+1

def search(i, j, path):
    global shortest_path, shortest_len
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return
    if (i, j) in block_cells:
        return
    if visited[i][j] == 1:
        return

    if (i, j) == end:
        path.append((i, j))
        if len(path) < shortest_len:
            shortest_len = len(path)
            shortest_path = path.copy()
        path.pop()
        return

    visited[i][j] = 1
    path.append((i, j))

    for direction in ["north", "south", "west", "east"]:
        i1, j1 = move(i, j, direction)
        search(i1, j1, path) #recursion

    visited[i][j] = 0
    path.pop()

search(start[0], start[1], [])

if shortest_path is None:
    print("No path found.")
else:
    print("Shortest path length:", shortest_len)
    print("Path as (i,j) coordinates:", shortest_path)

    path_numbers = [int(m[i, j]) for (i, j) in shortest_path]
    print("Path as cell numbers:", path_numbers)
