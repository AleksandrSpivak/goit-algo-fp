import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


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
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def heap_to_tree(hp, level):
    """
    Convert a heap to a binary tree.

    Args:
        hp: A list representing the heap.
        left: An integer representing the number of left nodes.

    Use global variable that contains number of nodes at the lowest level of a tree

    Returns:
        Node: The root node of the binary tree.
    """
    global low

    root = Node(heapq.heappop(hp))
    if level > 1:
        root.left = heap_to_tree(hp, level - 1)
    elif level == 1 and low:
        low -= 1
        root.left = heap_to_tree(hp, level - 1)
    else:
        return root
    if root.left:
        if level > 1:
            root.right = heap_to_tree(hp, level - 1)
        elif level == 1 and low:
            low -= 1
            root.right = heap_to_tree(hp, level - 1)
    return root


def tree_estimate(hp):
    """
    Calculate the number of levels and number of nodes on the lowest level of a tree based on the given hp list.

    Parameters:
    hp (list): The list representing the hit points of the tree nodes.

    Returns:
    tuple: A tuple containing the level and low of the tree.
    """
    n = len(hp)
    level = 0
    while n > 1:
        n = n // 2
        level += 1

    low = len(hp)
    n = level - 1
    while n >= 0:
        low = low - 2**n
        n -= 1

    return level, low


if __name__ == "__main__":
    hp = [12, 17, 4, 7, 15, 40, 16, 25, 1, 9, 3, 5]
    level, low = tree_estimate(hp)

    heapq.heapify(hp)
    root = heap_to_tree(hp, level)

    draw_tree(root)
