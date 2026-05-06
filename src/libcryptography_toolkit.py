import hashlib
import math

from pathlib import Path
from collections import Counter
from typing import Union

def calculate_sha256(path: Path) -> str:
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()

def shannon_entropy(data: Union[bytes, bytearray, memoryview]) -> float:
    """
    Compute Shannon entropy (in bits per byte) for a bytes-like object.

    Entropy H = -∑ p(x) * log2(p(x)), where p(x) is the empirical probability
    of each byte value in the input.

    Returns:
        float: entropy in [0.0, 8.0] for typical byte data.
    """
    # Normalize to a bytes-like, zero-copy view of 0..255 ints
    if not isinstance(data, (bytes, bytearray, memoryview)):
        raise TypeError("data must be bytes, bytearray, or memoryview")

    mv = memoryview(data).cast("B")
    n = len(mv)
    if n == 0:
        return 0.0

    counts = Counter(mv)
    inv_n = 1.0 / n

    # Only iterate over symbols that actually occur
    entropy = 0.0
    for c in counts.values():
        p = c * inv_n
        entropy -= p * math.log2(p)
    return entropy
