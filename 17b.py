import heapq, sys

def add_tup(a, b):
    return (a[0] + b[0], a[1] + b[1])

city = []
for line in sys.stdin.readlines():
    city.append(line.strip())

# store dist, y, x, dir, dir_steps 
queue = [(0, 0, 0, (0,0), 0)]
# store (y, x, dir, dir_steps) -> min dist
visited = {}

i = 0
while queue and i < 10:
#    print(queue)
#    print(visited)
    dist, y, x, dir, dir_steps = heapq.heappop(queue)

    if (y, x, dir, dir_steps) in visited:
        if visited[(y, x, dir, dir_steps)] > dist:
            visited[(y, x, dir, dir_steps)] = dist
        continue
    visited[(y, x, dir, dir_steps)] = dist

    for new_dir in ((1,0),(-1,0),(0,1),(0,-1)):
        # cant go backwards
        if new_dir[0] == -dir[0] and new_dir[1] == -dir[1]:
#            print('cant go backwards')
            continue
        elif new_dir == dir and dir_steps >= 10:
            continue
        # only allow turns after 4 straight moves
        elif dir != (0,0) and new_dir != dir and dir_steps < 4:
            continue
        else:
            new_y, new_x = add_tup((y, x), new_dir)
            if new_dir == dir:
                new_steps = dir_steps + 1
            else: 
                new_steps = 1
            # in bounds?
            if new_y in range(len(city)) and new_x in range(len(city[0])):
                heapq.heappush(queue, ((dist + int(city[new_y][new_x]), new_y, new_x, new_dir, new_steps)))

end = (len(city) - 1, len(city[0]) - 1)
heat = 1e10
winner = None
for node in visited.keys():
    y, x, dir, dir_steps = node
    if (y,x) == end and dir_steps >= 4 and dir_steps <= 10:
        if visited[node] < heat:
            heat = visited[node]
        heat = min(heat, visited[node])

print(heat)
