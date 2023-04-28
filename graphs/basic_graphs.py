def _input(message):
    return input(message).strip().split(" ")


def initialize_unweighted_directed_graph(
    node_count: int, edge_count: int
) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y = (int(i) for i in _input(f"Edge {e + 1}: <node1> <node2> "))
        graph[x].append(y)
    return graph


def initialize_unweighted_undirected_graph(
    node_count: int, edge_count: int
) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y = (int(i) for i in _input(f"Edge {e + 1}: <node1> <node2> "))
        graph[x].append(y)
        graph[y].append(x)
    return graph


def initialize_weighted_undirected_graph(
    node_count: int, edge_count: int
) -> dict[int, list[tuple[int, int]]]:
    graph: dict[int, list[tuple[int, int]]] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y, w = (int(i) for i in _input(f"Edge {e + 1}: <node1> <node2> <weight> "))
        graph[x].append((y, w))
        graph[y].append((x, w))
    return graph


def dfs(g, s):
    """
    Depth First Search.
    Args:   G - Dictionary of edges
            s - Starting Node
    Vars :  vis - Set of visited nodes
            S - Traversal Stack
    """

    vis, _s = {s}, [s]
    print(s)
    while _s:
        flag = 0
        for i in g[_s[-1]]:
            if i not in vis:
                _s.append(i)
                vis.add(i)
                flag = 1
                print(i)
                break
        if not flag:
            _s.pop()
