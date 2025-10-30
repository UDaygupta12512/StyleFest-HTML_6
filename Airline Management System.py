import sys
import heapq
from collections import deque

def process_announcements(N, Q, announcements):
    queue = deque(range(1, N + 1))  # People in FIFO order
    boarded_set = set()  # Track people who have boarded
    heap = []  # Min-heap for unboarded people

    result = []  # Store Type 3 announcement results

    for event in announcements:
        if event[0] == 1:
            # Type 1: Call the person who has waited the longest
            person = queue.popleft()
            heapq.heappush(heap, person)
        
        elif event[0] == 2:
            # Type 2 X: Mark person X as boarded
            boarded_set.add(event[1])
        
        elif event[0] == 3:
            # Type 3: Call the longest waiting person who has NOT boarded
            while heap and heap[0] in boarded_set:
                heapq.heappop(heap)  # Remove boarded people
            
            if heap:
                result.append(str(heap[0]))  # Append result as a string for fast output
    
    # Print all results at once for fast I/O
    sys.stdout.write("\n".join(result) + "\n")

# Read input
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split("\n")
    
    # Read N and Q
    N, Q = map(int, data[0].split())

    # Read the announcements and convert to list of tuples
    announcements = []
    for i in range(1, Q + 1):
        parts = list(map(int, data[i].split()))
        announcements.append(parts)

    # Process announcements
    process_announcements(N, Q, announcements)
