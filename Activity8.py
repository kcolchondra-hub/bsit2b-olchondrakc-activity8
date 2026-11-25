import heapq
import random


# ==========================================
# Activity 1: Min-Heap
# ==========================================
class MinHeap:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def peek(self):
        return self.data[0] if self.data else None

    def insert(self, val):
        self.data.append(val)
        self._sift_up(len(self.data) - 1)

    def extract(self):
        if not self.data:
            return None
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return top

    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.data[idx] < self.data[parent]:
                self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.data)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest != idx:
                self.data[idx], self.data[smallest] = self.data[smallest], self.data[idx]
                idx = smallest
            else:
                break


# ==========================================
# Activity 2: Max-Heap
# ==========================================
class MaxHeap(MinHeap):
    def _sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.data[idx] > self.data[parent]:
                self.data[idx], self.data[parent] = self.data[parent], self.data[idx]
                idx = parent
            else:
                break

    def _sift_down(self, idx):
        n = len(self.data)
        while True:
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self.data[left] > self.data[largest]:
                largest = left
            if right < n and self.data[right] > self.data[largest]:
                largest = right
            if largest != idx:
                self.data[idx], self.data[largest] = self.data[largest], self.data[idx]
                idx = largest
            else:
                break


# ==========================================
# Activity 3: Heap Sort (using Max-Heap)
# ==========================================
def heap_sort(arr):
    heap = MaxHeap()
    for x in arr:
        heap.insert(x)
    sorted_asc = []
    while heap.size() > 0:
        sorted_asc.append(heap.extract())
    sorted_asc.reverse()  
    return sorted_asc


# ==========================================
# Activity 4: Kth Largest (Min-Heap of size k)
# ==========================================
def kth_largest(nums, k):
    if k <= 0 or k > len(nums):
        return None
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


# ==========================================
# Activity 5: Merge k Sorted Arrays
# ==========================================
def merge_k_sorted_arrays(arrays):
    heap = []
    for arr_idx, arr in enumerate(arrays):
        if arr: 
            heapq.heappush(heap, (arr[0], arr_idx, 0))

    merged = []
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        merged.append(val)
        next_idx = elem_idx + 1
        if next_idx < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][next_idx], arr_idx, next_idx))
    return merged


# ==========================================
# Activity 6: Priority Scheduler (Stretch)
# ==========================================
def run_priority_scheduler(jobs):
    pq = []
    for priority, name in jobs:
        heapq.heappush(pq, (-priority, name))  

    release_order = []
    while pq:
        neg_prio, name = heapq.heappop(pq)
        release_order.append((name, -neg_prio))
    return release_order


# ==========================================
# Tests
# ==========================================
if __name__ == "__main__":
    # Activity 1 test
    min_h = MinHeap()
    for x in [5, 9, 11, 14, 19, 17, 18, 13]:
        min_h.insert(x)
    out1 = [min_h.extract() for _ in range(min_h.size())]
    assert out1 == [5, 9, 11, 13, 14, 17, 18, 19]

    # Activity 2 test
    max_h = MaxHeap()
    for x in [5, 9, 11, 14, 19, 17, 18, 13]:
        max_h.insert(x)
    out2 = [max_h.extract() for _ in range(max_h.size())]
    assert out2 == [19, 18, 17, 14, 13, 11, 9, 5]

    # Activity 3 test cases
    test_arrays = [
        [],
        [42],
        [4, 10, 3, 5, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 3, 1, 2],
        [random.randint(-50, 50) for _ in range(20)],
    ]
    for arr in test_arrays:
        assert heap_sort(arr) == sorted(arr)

    # Activity 4 test & verification
    sample = [7, 10, 4, 3, 20, 15, 10]
    for k in range(1, len(sample) + 1):
        expected = sorted(sample, reverse=True)[k - 1]
        assert kth_largest(sample, k) == expected

    # Activity 5 test (3 sorted arrays of different lengths)
    a1 = [1, 4, 7, 10]
    a2 = [2, 5]
    a3 = [0, 3, 6, 8, 9, 12]
    merged = merge_k_sorted_arrays([a1, a2, a3])
    assert merged == sorted(a1 + a2 + a3)

    # Activity 6 test
    jobs = [(2, "Backup"), (10, "CrashHandler"), (5, "UIUpdate"), (10, "SecurityAlert")]
    order = run_priority_scheduler(jobs)
    print("Release order:", order)
    print("All tests passed!")