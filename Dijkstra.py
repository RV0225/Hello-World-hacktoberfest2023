import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []
    
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > shortest_paths[current_node]:
            continue
        
        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 7)
    g.add_edge("C", "D", 3)

    start_node = "A"
    shortest_paths = dijkstra(g, start_node)

    for node, distance in shortest_paths.items():
        print(f"Shortest distance from {start_node} to {node}: {distance}")
