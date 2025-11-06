import heapq

# Define Huffman Tree Node class
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''  # 0 or 1

    # for heapq to compare nodes by frequency
    def __lt__(self, nxt):
        return self.freq < nxt.freq


# Function to build Huffman Tree
def build_huffman_tree(symbols, frequencies):
    nodes = []

    # Convert all characters and their frequencies into nodes
    for i in range(len(symbols)):
        heapq.heappush(nodes, Node(frequencies[i], symbols[i]))

    # Build the tree until one node remains (root)
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    return nodes[0]  # root node


# Function to print Huffman Codes
def print_codes(node, val=''):
    new_val = val + str(node.huff)
    if node.left:
        print_codes(node.left, new_val)
    if node.right:
        print_codes(node.right, new_val)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {new_val}")


# Function to take user input and generate Huffman Codes
def huffman_user_input():
    n = int(input("Enter number of characters: "))
    symbols = []
    frequencies = []

    for i in range(n):
        ch = input(f"Enter character {i+1}: ")
        freq = int(input(f"Enter frequency of '{ch}': "))
        symbols.append(ch)
        frequencies.append(freq)

    # Build and print Huffman Codes
    root = build_huffman_tree(symbols, frequencies)
    print("\nHuffman Codes:")
    print_codes(root)


# Main driver code
if __name__ == "__main__":
    huffman_user_input()
