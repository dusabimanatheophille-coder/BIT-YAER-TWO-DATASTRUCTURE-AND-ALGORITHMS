import heapq

# (priority, patient)
# Lower number = higher priority
patients = []
heapq.heappush(patients, (1,"Patient A - Critical"))
heapq.heappush(patients, (2,"Patient B - Serious"))
heapq.heappush(patients, (3,"Patient C - Normal"))

print("Serving order:")
while patients:
    print(heapq.heappop(patients))
