# Define the dictionary with codes for each letter
codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '$', 'c': '1',
    'D': '^', 'd': '2', 'E': '&', 'e': '3', 'F': '*', 'f': '4',
    'G': '(', 'g': '5', 'H': ')', 'h': '6', 'I': '-', 'i': '7',
    'J': '_', 'j': '8', 'K': '=', 'k': '0', 'L': '+', 'l': '!', 
    'M': '[', 'm': ']', 'N': '{', 'n': '}', 'O': '|', 'o': '\\',
    'P': ':', 'p': ';', 'Q': '"', 'q': "'", 'R': '<', 'r': '>',
    'S': ',', 's': '.', 'T': '/', 't': '?', 'U': '`', 'u': '~',
    'V': 'z', 'v': 'y', 'W': 'x', 'w': 'w', 'X': 'v', 'x': 'u',
    'Y': 't', 'y': 's', 'Z': 'r', 'z': 'q',
}

def encrypt_file(infile_name, outfile_name):
    with open(infile_name, 'r') as infile:
        content = infile.read()

    encrypted_content = ""

    for char in content:
        encrypted_content += codes.get(char, char)  # Use .get() to handle missing keys

    with open('encrypted.txt', 'w') as outfile:
        outfile.write(encrypted_content)

encrypt_file('info_security-1.txt', 'encrypted.txt')
