import uuid
import networkx as nx
import matplotlib.pyplot as plt
from bokeh import palettes
from queue import Queue
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def calculate_number_of_nodes(root):
    # обраховує кількість вузлів в дереві для подальшого визначення шагу зміни кольору вузлів
    q = Queue()
    number_of_nodes = 0
    q.put(root)
    while not q.empty():
        vertex = q.get()
        number_of_nodes += 1

        if vertex.left:
            q.put(vertex.left)
        if vertex.right:
            q.put(vertex.right)
    return number_of_nodes


def new_color(number_of_nodes, counter):
    # повертає колбори з палітри Viridis256 у порядку від темніших до світліших
    lp = palettes.linear_palette(palettes.Viridis256, number_of_nodes)
    return lp[counter]


def bfs_iterative(root):
    # обходить дерево в ширину та змінює кольори вузлів
    q = Queue()
    q.put(root)
    number_of_nodes = calculate_number_of_nodes(root)
    counter = 1

    while not q.empty():
        vertex = q.get()
        vertex.color = new_color(number_of_nodes + 1, counter)
        counter += 1

        if vertex.left:
            q.put(vertex.left)
        if vertex.right:
            q.put(vertex.right)

    return


def dfs_iterative(root):
    # обходить дерево в глубину та змінює кольори вузлів
    q = deque()
    q.append(root)
    number_of_nodes = calculate_number_of_nodes(root)
    counter = 1

    while len(q) > 0:
        vertex = q.popleft()
        vertex.color = new_color(number_of_nodes + 1, counter)
        counter += 1

        if vertex.right:
            q.appendleft(vertex.right)
        if vertex.left:
            q.appendleft(vertex.left)

    return


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    dfs_iterative(root)
    draw_tree(root)

    bfs_iterative(root)
    draw_tree(root)
