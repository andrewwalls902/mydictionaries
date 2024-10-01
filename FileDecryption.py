# Define the original encryption dictionary
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

decryption_codes = {v: k for k, v in codes.items()}

def decrypt_file(encrypted_filename):
    with open(encrypted_filename, 'r') as infile:
        encrypted_content = infile.read()

    decrypted_content = ""

    for char in encrypted_content:
        decrypted_content += decryption_codes.get(char, char) 

    print(decrypted_content)

decrypt_file('encrypted.txt')
