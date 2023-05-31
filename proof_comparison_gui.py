import tkinter as tk
import matplotlib.pyplot as plt
from vlz77 import vlz77_compress
from lz77 import lz77_compress

def run_proof():
    # Original dataset
    original_data = "AAAAABBBCCCCCDDDDDEEEEE"

    # Perform vLZ77 compression
    vlz77_compressed_data = vlz77_compress(original_data)
    vlz77_compression_ratio = len(vlz77_compressed_data) / len(original_data)

    # Perform LZ77 compression
    lz77_compressed_data = lz77_compress(original_data)
    lz77_compression_ratio = len(lz77_compressed_data) / len(original_data)

    # Display the results graphically
    compression_ratios = [1, vlz77_compression_ratio, lz77_compression_ratio]
    algorithms = ['Original', 'vLZ77', 'LZ77']

    plt.bar(algorithms, compression_ratios)
    plt.ylabel("Compression Ratio")
    plt.title("vLZ77 vs LZ77 Compression")
    plt.show()

# Create the GUI window
window = tk.Tk()
window.title("vLZ77 vs LZ77 Compression Proof")
window.geometry("400x200")

# Create a button to run the proof
run_button = tk.Button(window, text="Run Proof", command=run_proof)
run_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()
