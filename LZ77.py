def lz77_compress(data):
    compressed_data = []
    pos = 0

    while pos < len(data):
        max_length = 0
        max_offset = 0

        for offset in range(1, pos+1):
            length = 0
            while length < len(data) - pos and data[pos+length] == data[pos-length]:
                length += 1

            if length > max_length:
                max_length = length
                max_offset = offset

        if max_length > 0:
            compressed_data.append((max_offset, max_length, data[pos+max_length]))
            pos += max_length + 1
        else:
            compressed_data.append((0, 0, data[pos]))
            pos += 1

    return compressed_data

def lz77_decompress(compressed_data):
    data = ""
    for entry in compressed_data:
        offset, length, char = entry
        if length > 0:
            start = len(data) - offset
            for i in range(length):
                data += data[start + i]
        data += char

    return data
