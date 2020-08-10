from util import Stack, Queue  # These may come in handy


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Use queues with breath-first-travsal
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        # size is a function
        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                visited.add(v)
                # debug
                print(v)

                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        # Use stacks with depth-first-travsal
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                # debug
                print(v)

                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        # plan -> call recursive dtf
        # when does recursion happen? -> when looping through get_neighbors
        pass

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            # remove vertex from queue
            path = q.dequeue()
            # get last vertex from 'path' (inside an array)
            v = path[-1]

            if v not in visited:
                # found our destination
                if v == destination_vertex:
                    return path
                # not found, add to visited
                else:
                    visited.add(v)
                    # debug
                    print(v)

                for next_vertex in self.get_neighbors(v):
                    # copy original path as new variable
                    new_path = path.copy()
                    new_path.append(next_vertex)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            # remove vertex from stack
            path = s.pop()
            # get last vertex from 'path' (inside an array)
            v = path[-1]

            if v not in visited:
                # add to visted set
                visited.add(v)
                # debug
                print(v)

                # search found destination
                if v == destination_vertex:
                    # return the search path
                    return path

                # continue search to neighbors
                else:
                    for next_vertex in self.get_neighbors(v):
                        # copy original path as new variable
                        new_path = path.copy()
                        new_path.append(next_vertex)
                        s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
