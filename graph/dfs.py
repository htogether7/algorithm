graph = {1:[2,3], 2:[4,5], 3: [6,7], 4:[],5:[],6:[],7:[]};
visited = [False] * 8;
path = [];
def dfs(graph, v, visited):
    visited[v] = True;
    # print(v);
    path.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited);
print(path)