

def color_node(graph):
    color_map = {}
    for node in sorted(graph,key=lambda x : len(graph),reverse=True):
        neighbours_colors = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next(color for color in range(len(graph)) if color not in neighbours_colors)
    return color_map

graph = {'a':list('bcd'),'b' : list('ac'),'c' : list('abdef'),
         'd' : list('ace') , 'e' : list('def') , 'f' : list('ce')
         }

print(color_node(graph))