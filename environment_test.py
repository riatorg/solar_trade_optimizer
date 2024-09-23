import networkx as nx
import pytesseract

# Create a simple graph
G = nx.Graph()
G.add_edge("Earth", "Mars")
print(G.edges())

# Check if pytesseract is working
print(pytesseract.get_tesseract_version())
