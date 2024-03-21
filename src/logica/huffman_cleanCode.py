import heapq
from collections import defaultdict



class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self, text):
        self.huffman_code = {}
        self.text = text
        self.freq = defaultdict(int)
        self.heap = []
        self.codes = {}
        self.reverse_codes = {}
        
        if not self.text:
            raise ValueError("Input text is empty")

        self._build_freq()
        self._build_heap()

    def _build_freq(self):
        # Construye un diccionario de frecuencias de caracteres en el texto
        for char in self.text:
            self.freq[char] += 1

    def _build_heap(self):
        # Construye un heap de nodos basado en las frecuencias de los caracteres
        self.heap = [Node(char, freq) for char, freq in self.freq.items()]
        heapq.heapify(self.heap)

    def _build_tree(self):
        # Construye el árbol Huffman combinando los nodos del heap
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def _build_codes(self, node, code):
        # Construye los códigos Huffman recursivamente
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = code
            self.reverse_codes[code] = node.char
            return
        self._build_codes(node.left, code + "0")
        self._build_codes(node.right, code + "1")

    def encode(self):
        # Codifica el texto de entrada utilizando el árbol Huffman
        
        """EXCEPCIONES CASOS DE ERROR POSIBLES"""
        if not isinstance(self.text, str):
            raise TypeError("Input text must be a string")
        if len(self.text) < 2:
            raise ValueError("Input text is too short")
        if not self.heap:
            raise ValueError("Invalid tree structure")

        self._build_tree()
        root = self.heap[0]
        self._build_codes(root, "")
        encoded_text = "".join(self.codes[char] for char in self.text)

        return encoded_text

    def decode(self, encoded_text):
        # Decodifica el texto codificado utilizando los códigos Huffman inversos
        if not all(bit in ('0', '1') for bit in encoded_text):
            raise ValueError("Invalid encoded data")
        if not encoded_text:
            raise ValueError("Encoded text is empty")

        curr_code = ""
        decoded_text = ""

        for bit in encoded_text:
            curr_code += bit
            if curr_code in self.reverse_codes:
                decoded_text += self.reverse_codes[curr_code]
                curr_code = ""
            else:
                if len(curr_code) > max(len(code) for code in self.reverse_codes):
                    raise ValueError("Invalid bit sequence")

        return decoded_text
