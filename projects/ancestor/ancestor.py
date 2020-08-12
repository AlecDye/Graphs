# lazy import queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


# lazy import graph
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)  # parent
        graph.add_vertex(child)  # child
        graph.add_edge(child, parent)  # connection between child -> parent

    # Do a BFS storing the path
    # COULD return just the last node to be visited
    # EDGE CASE: what if 2 parents at the same level?
    # EDGE CASE: what if our input is 11? Should return -1

    q = Queue()
    q.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    # [6, 3, 1, 10] -> want to return 10
    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]

        if len(path) == longest_path_length:
            if current_node < earliest_ancestor:
                longest_path_length = len(path)
                earliest_ancestor = current_node

        # if path is longer than current longest path, replace with path
        if len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        neighbors = graph.vertices[current_node]
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            q.enqueue(path_copy)

    return earliest_ancestor


# test
print(
    earliest_ancestor(
        [
            (1, 3),
            (2, 3),
            (3, 6),
            (5, 6),
            (5, 7),
            (4, 5),
            (4, 8),
            (8, 9),
            (11, 8),
            (10, 1),
        ],
        6,
    )
)
# 10

