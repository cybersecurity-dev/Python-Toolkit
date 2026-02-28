import os
import hashlib

from pathlib import Path

def calculate_sha256(fpath : Path):
    sha256_hash = hashlib.sha256()
    with open(fpath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    # Frequency distribution of byte values (0-255)
    freq = [0] * 256
    for byte in data:
        # Ensure `byte` is treated as an integer
        freq[byte] += 1
    # Calculate entropy
    entropy = 0.0
    for count in freq:
        if count > 0:
            p = count / len(data)
            entropy -= p * math.log2(p)
    return entropy