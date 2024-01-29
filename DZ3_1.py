import heapq
import copy
from collections import defaultdict


def dijkstra(edges, start, end):
    g = defaultdict(list)
    for s, e, w in edges:
        g[s].append((w, e))

    heap, visited, mins = [(0, start, [])], set(), {start: 0}
    while heap:
        (cost, v1, p) = heapq.heappop(heap)
        if v1 not in visited:
            visited.add(v1)
            path = copy.deepcopy(p)
            path.append(v1)
            if v1 == end:
                return (cost, path)

            for w, v2 in g.get(v1, ()):
                if v2 in visited:
                    continue
                prev = mins.get(v2, None)
                next = cost + w
                if prev is None or next < prev:
                    mins[v2] = next
                    heapq.heappush(heap, (next, v2, path))

    return float("inf"), None


if __name__ == "__main__":
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    G_description = [
        ("A", "B", 6),
        ("A", "C", 5),
        ("A", "G", 9),
        ("B", "H", 6),
        ("C", "E", 4),
        ("C", "H", 9),
        ("B", "D", 7),
        ("D", "E", 3),
        ("D", "F", 6),
        ("E", "F", 3),
        ("F", "H", 7),
        ("G", "I", 3),
        ("H", "I", 2),
        ("I", "J", 4),
        ("C", "J", 14),
    ]

    for n in nodes:
        cost, path = dijkstra(G_description, "A", n)
        print(f"Шлях з 'A' до '{n}': {', '.join(p for p in path):<12} вартість: {cost}")
