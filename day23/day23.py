#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import defaultdict

# Step 1: Read the input file and parse the connections
def read_input(filename):
    with open(filename, 'r') as file:
        connections = [line.strip().split('-') for line in file.readlines()]
    return connections

# Step 2: Build an undirected graph from the connections
def build_graph(connections):
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph

# Step 3: Find triangles (sets of three interconnected nodes)
def find_triangles(graph):
    triangles = set()
    for node in graph:
        neighbors = list(graph[node])
        n = len(neighbors)
        for i in range(n):
            for j in range(i + 1, n):
                if neighbors[j] in graph[neighbors[i]]:
                    triangle = tuple(sorted([node, neighbors[i], neighbors[j]]))
                    triangles.add(triangle)
    return triangles

# Step 4: Filter triangles containing nodes starting with 't'
def filter_triangles(triangles):
    return [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]

# Step 5: Main function to execute all steps
def main():
    try:
        connections = read_input('input23.txt')  # Adjust the file name as needed
        graph = build_graph(connections)
        triangles = find_triangles(graph)
        filtered_triangles = filter_triangles(triangles)
        print("Total triangles with 't':", len(filtered_triangles))
    except FileNotFoundError:
        print("The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()


# In[4]:


from collections import defaultdict

def read_input(file_name):
    """Reads input from the specified file."""
    with open(file_name, 'r') as file:
        connections = [line.strip().split('-') for line in file]
    return connections

def bron_kerbosch(graph, r, p, x, cliques):
    """Bron-Kerbosch algorithm to find maximal cliques."""
    if not p and not x:
        cliques.append(r)
        return
    for v in list(p):
        bron_kerbosch(
            graph,
            r.union({v}),
            p.intersection(graph[v]),
            x.intersection(graph[v]),
            cliques
        )
        p.remove(v)
        x.add(v)

def find_maximal_cliques(graph):
    """Finds all maximal cliques in the graph."""
    cliques = []
    bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
    return cliques

def find_largest_clique(cliques):
    """Finds the largest clique among all cliques."""
    return max(cliques, key=len)

def generate_password(clique):
    """Generates the password from the largest clique."""
    return ",".join(sorted(clique))

def main():
    # Input file name
    input_file = "input23.txt"

    # Read input connections
    connections = read_input(input_file)

    # Build the adjacency list
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)

    # Find all maximal cliques
    cliques = find_maximal_cliques(graph)

    # Find the largest clique
    largest_clique = find_largest_clique(cliques)

    # Generate the password
    password = generate_password(largest_clique)
    print(f"Password to the LAN party: {password}")

if __name__ == "__main__":
    main()


# In[ ]:




