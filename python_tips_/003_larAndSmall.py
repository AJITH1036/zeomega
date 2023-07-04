import heapq

scores = [56,86,84,57,93,75,94,58,67,49,78,85]

print(heapq.nlargest(3,scores))
print(heapq.nsmallest(3,scores))