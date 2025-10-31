import random

def knn_distance(arr, q, k):
    diffs = [(abs(x - q), x) for x in arr]
    def quickselect(lst, k):
        if len(lst) == 1:
            return lst[0]
        pivot = random.choice(lst)[0]
        left = [x for x in lst if x[0] < pivot]
        mid = [x for x in lst if x[0] == pivot]
        right = [x for x in lst if x[0] > pivot]

        if k <= len(left):
            return quickselect(left, k)
        elif k <= len(left) + len(mid):
            return mid[0]
        else:
            return quickselect(right, k - len(left) - len(mid))

    dist, point = quickselect(diffs, k)
    return (dist, point)
