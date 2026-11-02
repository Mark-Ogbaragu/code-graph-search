import networkx as nx
import ast

def analyze_code(file_path):
    with open(file_path) as f:
        code = f.read()
    tree = ast.parse(code)
    G = nx.DiGraph()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            G.add_node(node.name)
            print(f"Found function: {node.name}")
    print(f"Total functions: {G.number_of_nodes()}")
    return G

# Test it
analyze_code("detector.py")
