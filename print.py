# Retaining printing on the same line/position 
import time

for i in range(101):
    print(f"\r{i}", end="", flush=True)
    time.sleep(0.2)
