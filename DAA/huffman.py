import heapq

class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def print_codes(node, code=""):
    # Base case: leaf node (symbol present)
    if not node.left and not node.right:
        print(f"{node.char} -> {code}")
        return
    # Recursive calls for left (add '0') and right (add '1')
    if node.left:
        print_codes(node.left, code + "0")
    if node.right:
        print_codes(node.right, code + "1")

# Example data
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freqs = [5, 9, 12, 13, 16, 45]
nodes = []

# Create node for each symbol and push to heap
for ch, fr in zip(chars, freqs):
    heapq.heappush(nodes, Node(fr, ch))

# Build the Huffman tree
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    merged = Node(left.freq + right.freq, None, left, right)
    heapq.heappush(nodes, merged)

# Output the codes
print_codes(nodes[0])
