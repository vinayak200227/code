import heapq
from collections import defaultdict

# Define a class to represent nodes in the Huffman tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman tree from a dictionary of character frequencies
def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    # Combine nodes to create the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(None, left.freq + right.freq)
        parent.left, parent.right = left, right
        heapq.heappush(heap, parent)

    return heap[0]

# Generate Huffman codes for characters in the tree
def generate_huffman_codes(root, current_code, codes):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = current_code
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

# Encode data using Huffman codes
def huffman_encoding(data):
    if len(data) == 0:
        return None, None

    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    root = build_huffman_tree(freq_dict)

    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data, root

# Decode Huffman-encoded data
def huffman_decoding(encoded_data, root):
    if encoded_data is None or root is None:
        return None

    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data

if __name__ == "__main__":
    # Example usage:
    data = "Vinayak"
    
    encoded_data, tree = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Decoded data: {decoded_data}")
