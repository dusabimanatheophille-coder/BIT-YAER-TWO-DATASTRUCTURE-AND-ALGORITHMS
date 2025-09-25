# Airtel Shop Queue Simulation
# 7 clients join for SIM swap. After 3 are served, who is next?

from collections import deque

# Step 1: Represent the clients in arrival order
queue = deque([1, 2, 3, 4, 5, 6, 7])
print("Initial queue:", list(queue))

# Step 2: Serve first 3 clients (FIFO)
served_clients = []
for _ in range(3):
    served_clients.append(queue.popleft())

print("Served clients:", served_clients)
print("Queue after serving 3:", list(queue))

# Step 3: Show the next client to be served
next_client = queue[0]
print("Next client to be served:", next_client)
