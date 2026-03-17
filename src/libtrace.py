import tracemalloc

def start_memory_tracking():
    tracemalloc.start()

def log_max_memory(label="Max Memory Usage"):
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\n{'='*40}")
    print(f"  {label}")
    print(f"  Current : {current / 1024 / 1024:.2f} MB")
    print(f"  Peak    : {peak / 1024 / 1024:.2f} MB")
    print(f"{'='*40}\n")
    return peak

if __name__ == "__main__":
  start_memory_tracking()

  # --- sample script ---
  data = [i for i in range(1000000)]
  # ------------------------

  log_max_memory("Python Functions to Track and log Maximum Memory Usage:")
