import tkinter as tk
import matplotlib.pyplot as plt
from lz77 import lz77_compress, lz77_decompress
from vLZ77 import vlz77_compress, vlz77_decompress

def lz77_compress(data, window_size=10):
    compressed_data = []
    pos = 0

    while pos < len(data):
        max_length = 0
        max_offset = 0

        for i in range(1, min(window_size+1, pos+1)):
            substring = data[pos-i:pos]
            length = 0
            offset = 0

            while length < len(substring) and pos + length < len(data) and substring[length] == data[pos + length]:
                length += 1

            if length > max_length:
                max_length = length
                max_offset = i

        if max_length > 0:
            compressed_data.append((max_offset, max_length, data[pos + max_length]))
            pos += max_length + 1
        else:
            compressed_data.append((0, 0, data[pos]))
            pos += 1

    return compressed_data


def vlz77_compress(data):
    compressed_data = []
    pos = 0
    while pos < len(data):
        max_offset = 0
        max_length = 0
        for offset in range(1, MAX_OFFSET + 1):
            length = 0
            while length < MAX_LENGTH and pos + length < len(data) and data[pos + length] == data[pos - offset + length]:
                length += 1
            if length > max_length:
                max_length = length
                max_offset = offset
        compressed_data.append((max_offset, max_length, data[pos + max_length - 1]))  # Adjust the indexing here
        pos += max_length + 1
    return compressed_data


def run_proof():
    original_data = input_text.get("1.0", tk.END).strip()

    # Run LZ77 compression and decompression
    lz77_compressed_data = lz77_compress(original_data)
    lz77_decompressed_data = lz77_decompress(lz77_compressed_data)

    # Run vLZ77 compression and decompression
    vlz77_compressed_data = vlz77_compress(original_data)
    vlz77_decompressed_data = vlz77_decompress(vlz77_compressed_data)

    # Calculate compression ratios
    lz77_ratio = len(lz77_compressed_data) / len(original_data)
    vlz77_ratio = len(vlz77_compressed_data) / len(original_data)

    # Display the results graphically
    plt.bar(["LZ77", "vLZ77"], [lz77_ratio, vlz77_ratio])
    plt.xlabel("Compression Algorithm")
    plt.ylabel("Compression Ratio")
    plt.title("Compression Ratio Comparison")
    plt.show()

# Create the GUI window
window = tk.Tk()
window.title("vLZ77 vs LZ77 Compression Proof Comparison")

# Create input text box
input_text = tk.Text(window, height=10, width=50)
input_text.pack()

# Create Run Proof button
run_button = tk.Button(window, text="Run Proof", command=run_proof)
run_button.pack()

# Run the GUI event loop
window.mainloop()
